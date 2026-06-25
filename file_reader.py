#STEP 2

# file_reader.py

#we need to read the code files inside the cloned repository.
#First we must:
# Repository
#    ↓
#Read Files
#    ↓
#Extract Code
#    ↓
#Create Embeddings
#This step is the Data Ingestion Layer of our RAG pipeline.



# os helps us traverse folders and files
import os


def read_repository(repo_path):
    """
    Reads all supported source code files
    from a cloned repository.
    """

    # File types we want to process
    supported_extensions = (
            ".py",
            ".js",
            ".jsx",
            ".ts",
            ".tsx",
            ".java",
            ".cpp",
            ".c",
            ".cs",
            ".go",
            ".rs",
            ".php",
            ".rb",
            ".swift",
            ".kt",
            ".html",
            ".css",
            ".json",
            ".xml",
            ".yaml",
            ".yml",
            ".toml",
            ".md",
            ".txt"
        )
    # Store all code documents
    documents = []

    # Walk through every folder and file
    for root, dirs, files in os.walk(repo_path):

        for file in files:

            # Check if file is a supported code file
            if file.endswith(supported_extensions):

                # Full path to file
                file_path = os.path.join(root, file)

                try:

                    # Open file and read content
                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        code = f.read()

                    # Save file path and content
                    documents.append(
                        {
                            "file_path": file_path,
                            "content": code
                        }
                    )

                except Exception as e:

                    print(
                        f"Error reading {file_path}: {e}"
                    )

    return documents