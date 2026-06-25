# GitHub Repository RAG Assistant

An AI-powered GitHub Repository Assistant built using Retrieval-Augmented Generation (RAG). The application analyzes any public GitHub repository, generates a repository overview, and allows users to interact with the codebase through a conversational chatbot.

---

## Features

- Clone any public GitHub repository
- Read and process source code files
- Split source code into semantic chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in FAISS vector database
- Generate an AI-powered repository summary
- Chat with the repository using Gemini
- Multi-turn conversation support
- Retrieve relevant source code for every query
- Clean Streamlit-based user interface

---

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Google Gemini API
- GitPython
- python-dotenv

---

## Project Structure

```
github-rag-assistant/
│
├── streamlit_app.py
├── repo_loader.py
├── file_reader.py
├── document_processor.py
├── vector_store.py
├── index_manager.py
├── retriever.py
├── rag.py
├── summary_generator.py
├── vector_db/
├── cloned_repos/
├── requirements.txt
└── README.md
```

---

## How It Works

1. Enter a public GitHub repository URL.
2. The repository is cloned locally.
3. Source code files are read and processed.
4. Code is split into smaller chunks.
5. Sentence Transformers generate embeddings.
6. Embeddings are stored in a FAISS vector database.
7. Gemini generates a repository overview.
8. Users can ask questions through the chatbot.
9. The assistant retrieves relevant code chunks and generates responses using Retrieval-Augmented Generation (RAG).

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/github-rag-assistant.git
cd github-rag-assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run the Application

```bash
streamlit run streamlit_app.py
```

---

## Example Workflow

- Enter a GitHub repository URL
- Click **Process Repository**
- View the generated repository overview
- Open the chat assistant
- Ask repository-related questions
- Receive AI-generated answers based on retrieved code

---

## Example Questions

- Explain the project architecture.
- What technologies are used?
- How is authentication implemented?
- Explain the folder structure.
- How does the application workflow work?
- Where is the database configured?
- Which APIs are used in this project?

---

