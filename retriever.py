#STEP 5: Create a Retriever
'''
User asks:

How is Flask application initialized?

FAISS searches all 801 chunks and returns:

app.py
Chunk #52

Contains:
class Flask:
...

What is Retrieval?

Retrieval means:

Find the most relevant chunks
for a user's question.


What is Similarity Search?

Suppose:

Question Vector:
[1.2, 3.5, 0.8]

Stored vectors:

Chunk A:
[1.1, 3.6, 0.9]

Chunk B:
[8.5, 1.2, 7.4]

Chunk C:
[0.9, 3.4, 1.0]

Which is closest?

Question
 ↓
Chunk A
Chunk C
Chunk B

FAISS performs this calculation automatically.

What is Top-K?

Suppose:

801 chunks

User asks a question.

Should we return all 801?

No.

Instead:

k = 3

means:

Return top 3 most relevant chunks

This is called Top-K Retrieval.

'''

# retriever.py

# FAISS database
import faiss

# Used to load saved chunks
import pickle

# Embedding model
from sentence_transformers import SentenceTransformer


def retrieve_chunks(
    query,
    repo_name,
    top_k=3
):

    """
    Finds the most relevant chunks
    for a user question.
    """

    # Load the SAME model used during indexing
    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    # Convert question into embedding
    # Example:
    # "How is authentication implemented?"
    # →
    # [0.12, 0.44, ...]
    query_embedding = model.encode(
        [query]
    )

    # Load FAISS index
    index = faiss.read_index(
        f"vector_db/{repo_name}.index"
    )

    # Load chunk data
    with open(
        f"vector_db/{repo_name}.pkl",
        "rb"
    ) as f:

        chunks = pickle.load(f)

    # Search FAISS
    # Returns:
    # distances = similarity scores
    # indices = chunk numbers
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(
            chunks[idx]
        )

    return results

'''
What Happens Internally?

Let's trace one question.

User:

How is Flask application initialized?
Step 1

Convert question into embedding:

Question
 ↓
Vector
Step 2

Search FAISS:

801 vectors
 ↓
Find closest vectors
Step 3

Get matching chunk IDs:

Chunk 45
Chunk 101
Chunk 233
Step 4

Load actual code:

chunks.pkl
 ↓
Retrieve code
Step 5

Return results:

app.py
relevant code

factory.py
relevant code

config.py
relevant code
'''


'''
If an interviewer asks:

Why did you use all-MiniLM-L6-v2?

You can answer:

"I used the Sentence Transformer model all-MiniLM-L6-v2 to 
generate embeddings for repository code chunks. 
It converts source code and user queries into dense 
vector representations so that semantically similar content can be retrieved using FAISS."
'''