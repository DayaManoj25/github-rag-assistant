#STEP 7-Optimize the Vector Database
'''
What should happen?

When your app starts:

if vector_db.index exists:
    load existing index
else:
    create new index
'''
# index_manager.py

# Check whether files exist
import os

# Create FAISS if needed
from vector_store import create_vector_store


def get_or_create_index(chunks, repo_name):

    """
    If vector database already exists,
    reuse it.

    Otherwise create it.
    """

    # Check saved files
    if (
    os.path.exists(
        f"vector_db/{repo_name}.index"
    )
    and
    os.path.exists(
        f"vector_db/{repo_name}.pkl"
    )
    ):

        print(
            f"\nUsing existing vector database for {repo_name}..."
        )

        return

    print(
        f"\nCreating vector database for {repo_name}..."
    )

    create_vector_store(
        chunks,
        repo_name
    )

'''
Expected Result
First Run
Creating vector database...
Generating embeddings...
Vector database created!
Second Run
Using existing vector database...

No embedding generation.

No FAISS creation.

Much faster.

New Concept: Indexing
What is Indexing?
Documents
 ↓
Embeddings
 ↓
FAISS Database

This preprocessing step is called:

Indexing

It usually happens only once.
'''