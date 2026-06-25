#STEP 4: Create a Vector Store

# vector_store.py

#Repository
#    ↓
#Files
#    ↓
#Chunks
#Now we convert each chunk into a vector (embedding).
#These vectors help the AI find similar code even when exact keywords don't match.
#Embedding search understands semantic meaning




# Embedding model from HuggingFace
from sentence_transformers import SentenceTransformer

# FAISS vector database
import faiss

# Used for saving/loading
import pickle

# Numerical arrays
import numpy as np


def create_vector_store(
    chunks,
    repo_name
):

    """
    Creates embeddings for all chunks
    and stores them in FAISS.
    """

    print("Loading embedding model...")

    # Small, fast, free model
    #all-MiniLM-L6-v2 is a pretrained embedding model.
    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    texts = []

    for chunk in chunks:

        texts.append(
            chunk.page_content
        )

    print("Generating embeddings...")

    print(f"Total chunks: {len(chunks)}")
    print(f"Total texts: {len(texts)}")
    if len(texts) == 0:
        raise Exception("No chunks found. Repository contains no readable documents.")
    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    # Dimension of embeddings
    dimension = embeddings.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatL2(
        dimension
    )

    # Add embeddings
    index.add(
        np.array(embeddings)
    )

    # Save index
    faiss.write_index(
    index,
    f"vector_db/{repo_name}.index"
    )

    # Save chunk metadata
    with open(
    f"vector_db/{repo_name}.pkl",
    "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )

    print("Vector database created!")
    print(
        f"Saving index for {repo_name}"
    )
    print(
        f"Saving to vector_db/{repo_name}.index"
    )
    return index
    

#Hugging face stores ai models that can be used to convert text into vectors. 
# These vectors capture the meaning of the text, allowing for semantic search. 
# FAISS is a library that enables efficient similarity search and clustering of dense vectors. 
# By creating a vector store, we can quickly find relevant chunks of code based on their semantic content rather than just keyword matching.
#An embedding converts text into a list of numbers.

#Why do we need FAISS?
# Imagine: 1000 code chunks
# Each chunk becomes:
# [0.21, 0.44, ...]
# Now user asks:
# How does login work?
# Question also becomes a vector:
# [0.20, 0.41, ...]
# We must find:
# Which chunk vector is closest?
# among thousands of vectors.
#FAISS does this very fast.

"""
Why Not Use a Database?

Normal databases search:

WHERE text LIKE '%login%'

This is keyword matching.

RAG needs:

Meaning matching

Example:

User asks:

How is authentication implemented?

Repository contains:

JWT token generation

No keyword match.

But FAISS finds it because embeddings are similar.
"""