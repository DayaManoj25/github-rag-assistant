import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_repo_summary(documents):

    # Collect a sample of repository text
    repository_text = ""

    for doc in documents[:30]:

        repository_text += (
            doc["content"] + "\n\n"
        )

    prompt = f"""
You are a senior software engineer.

Analyze the following GitHub repository.

Provide the output in exactly this format.

# Repository Overview

## Purpose
Explain what this project does in 3-4 sentences.

## Architecture
Explain the major modules/components.

## Technology Stack

List the technologies used as bullet points.

Example format:

• Programming Language: Python
• Frontend: React
• Backend: Flask
• Database: Supabase
• Machine Learning: TensorFlow
• APIs: Gemini API
• Vector Database: FAISS
• Embedding Model: all-MiniLM-L6-v2

Only include technologies that actually exist in the repository.

## Folder Structure
Explain the important folders.

## Main Features
• Feature 1
• Feature 2
• Feature 3
• Feature 4

## Application Workflow
Explain how the application works from start to finish.

## Interesting Observations
Mention anything notable such as authentication,
REST APIs, RAG pipeline,
machine learning models,
vector databases or design patterns.

Repository Files:

{repository_text}
"""

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text

