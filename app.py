from repo_loader import clone_repo
from file_reader import read_repository
from document_processor import create_chunks
from vector_store import create_vector_store
from retriever import retrieve_chunks
from rag import generate_answer

# Repository to test
repo_url = "https://github.com/pallets/flask"

# Clone repository
repo_path = clone_repo(repo_url)

print("\nRepository cloned successfully.")

# Read repository files
documents = read_repository(repo_path)

print("\nTotal Files Found:")
print(len(documents))

# Display first few files
for doc in documents[:5]:

    print("\nFile:")
    print(doc["file_path"])

    print("Characters:")
    print(len(doc["content"]))

# Create chunks
chunks = create_chunks(documents)

print("\nTotal Chunks Created:")
print(len(chunks))

# Display first chunk
print("\nFirst Chunk Preview:\n")

print(
    chunks[0].page_content[:500]
)

print("\nChunk Source:")
print(
    chunks[0].metadata["source"]
)
from index_manager import (
    get_or_create_index
)

get_or_create_index(
    chunks
)

query = input(
    "\nAsk a question about the repository:\n"
)

results = retrieve_chunks(query)

answer = generate_answer(
    query,
    results
)

print("\nAnswer:\n")
print(answer)