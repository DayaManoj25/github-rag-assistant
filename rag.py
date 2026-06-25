
#Step 6
'''
gives user friendly responses to questions
using gemini llm and code chunks retrieved from a repository.

What is RAG?

RAG means:

Retrieval
+
Augmented
+
Generation
Retrieval - FAISS finds relevant chunks.

Augmented - Those chunks are attached to the prompt.

Generation - Gemini generates the answer.

'''

'''
Why Are We Creating a Prompt?

LLMs don't automatically know:

Which repository?
Which code?
What should I answer?

So we provide:

Question
+
Relevant Code
+
Instructions

This is called Prompt Engineering.
'''


# rag.py

# Load API key from .env
from dotenv import load_dotenv

# Access environment variables
import os

# Gemini SDK
import google.generativeai as genai


# Load variables from .env
load_dotenv()

# Read Gemini API key
api_key = os.getenv(
    "GEMINI_API_KEY"
)

# Configure Gemini
genai.configure(
    api_key=api_key
)


def generate_answer(
    query,
    retrieved_chunks,
    chat_history=""
):
    """
    Uses Gemini to answer questions
    based on retrieved code chunks.
    """

    # Combine all retrieved chunks
    context = ""

    for chunk in retrieved_chunks:

        context += (
            chunk.page_content
            + "\n\n"
        )

    # Prompt sent to Gemini
    prompt = f"""
    You are an expert software engineer.

    Previous Conversation:

    {chat_history}

    Repository Context:

    {context}

    User Question:

    {query}

    Answer using only the repository information provided.
    """

    # Create Gemini model
    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    # Generate response
    response = model.generate_content(
        prompt
    )

    return response.text

'''
Context

Context is the information we give Gemini.

Example:

Relevant Code
+
Question
Prompt Engineering

Designing prompts so the LLM gives better answers.

Example:

You are a senior software engineer.
Answer only using the repository code.
Hallucination

Sometimes an LLM invents answers.

We reduce hallucination by giving:

Retrieved Chunks

from the repository.

This is one of the main reasons RAG exists.

'''

'''
This is a very common interview question:

"Do you regenerate embeddings for every query?"

Correct answer:

"No. Embeddings are generated once and stored in FAISS. 
Subsequent queries reuse the existing vector index."

Why is this important?

Imagine a repository with:

5000 files

Generating embeddings every time would take minutes.

In real RAG systems:

Embeddings are generated once
Queries reuse the index
'''