#STEP 3: Convert our code files into LangChain Documents and split them into chunks

#Right now we have:
#Repository
#   ↓
#Read Files
#   ↓
#Python Dictionary
#But LangChain works with Documents.
#So we'll convert our code files into LangChain Documents and 
# split them into smaller chunks. so it becomes easier for 
# our model to process them and create better embeddings.

#what is langchain?
#Think of LangChain as a framework that helps you build applications 
# using LLMs (Gemini, GPT, Claude, Grok, etc.).
#
#Instead of manually writing everything yourself, LangChain provides ready-made components for:
#Loading data
#Splitting text
#Creating embeddings
#Storing vectors
#Retrieving relevant information
#Connecting to LLMs
#Maintaining chat memory



# document_processor.py

# LangChain document object
from langchain_core.documents import Document

# Text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):
    """
    Converts repository files into LangChain documents
    and splits them into chunks.
    """

    langchain_docs = []

    # Convert our dictionaries to LangChain documents
    for doc in documents:

        langchain_docs.append(
            Document(
                page_content=doc["content"],

                # metadata helps us know
                # which file a chunk came from
                metadata={
                    "source": doc["file_path"]
                }
            )
        )

    # Split large files into chunks
    splitter = RecursiveCharacterTextSplitter(

        # each chunk size
        chunk_size=1000,

        # overlap helps preserve context
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        langchain_docs
    )

    return chunks