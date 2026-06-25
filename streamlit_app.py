import streamlit as st

from repo_loader import clone_repo
from file_reader import read_repository
from document_processor import create_chunks
from index_manager import get_or_create_index

from retriever import retrieve_chunks
from rag import generate_answer

from summary_generator import generate_repo_summary

st.set_page_config(
    page_title="GitHub Repository RAG Assistant",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>

div[data-testid="stButton"] > button{

    border-radius:50px;
    height:60px;
    font-size:20px;

}

</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "page" not in st.session_state:
    st.session_state["page"] = "summary"

if "repo_name" not in st.session_state:
    st.session_state["repo_name"] = ""

if "repo_summary" not in st.session_state:
    st.session_state["repo_summary"] = ""

if st.session_state["page"] == "summary":

    st.title("GitHub Repository RAG Assistant")

    st.write(
        "Analyze any public GitHub repository and chat with its codebase using Retrieval-Augmented Generation (RAG)."
    )

    st.divider()

    repo_url = st.text_input(
        "GitHub Repository URL",
        placeholder="https://github.com/owner/repository"
    )

    if st.button(
        "Process Repository",
        use_container_width=True
    ):

        if repo_url == "":

            st.warning(
                "Please enter a GitHub repository URL."
            )

        else:

            with st.spinner(
                "Analyzing repository..."
            ):

                repo_name = (
                    repo_url
                    .rstrip("/")
                    .split("/")[-1]
                )

                st.session_state["repo_name"] = repo_name

                repo_path = clone_repo(
                    repo_url
                )

                documents = read_repository(
                    repo_path
                )

                if len(documents) == 0:

                    st.error(
                        """
                No supported source code files were found.

                Currently supported:
                • Python (.py)
                • JavaScript (.js)
                • JSX (.jsx)
                • TypeScript (.ts/.tsx)
                • Java (.java)
                • C++ (.cpp)
                """
                    )

                    st.stop()

                

                try:

                    summary = generate_repo_summary(
                        documents
                    )

                    st.session_state[
                        "repo_summary"
                    ] = summary

                except Exception as e:

                    st.session_state[
                        "repo_summary"
                    ] = f"Summary unavailable.\n\n{e}"

                chunks = create_chunks(
                    documents
                )

                

                get_or_create_index(
                    chunks,
                    repo_name
                )

                st.session_state[
                    "messages"
                ] = []

            st.success(
                "Repository processed successfully!"
            )

    if st.session_state["repo_summary"] != "":

        st.divider()

        st.subheader("Repository Overview")


        st.markdown(
            f"### {st.session_state['repo_name']}"
        )

        st.divider()

        st.subheader("Repository Summary")

        st.markdown(
            st.session_state["repo_summary"]
        )

        st.divider()

        st.divider()

        st.subheader("Start exploring the repository")

        if st.button(
            "Open Chat Assistant",
            use_container_width=True
        ):
            st.session_state["page"] = "chat"
            st.rerun()

        st.divider()

        if st.button(
            "Analyze Another Repository",
            use_container_width=True
        ):

            st.session_state["repo_summary"] = ""
            st.session_state["repo_name"] = ""
            st.session_state["messages"] = []
            st.session_state["page"] = "summary"

            st.rerun()

elif st.session_state["page"] == "chat":

    st.title("Repository Chat Assistant")

    st.caption(
        f"Currently chatting with **{st.session_state['repo_name']}**"
    )

    col1, col2 = st.columns([1, 5])

    with col1:

        if st.button(
            "Back",
            use_container_width=True
        ):

            st.session_state["page"] = "summary"
            st.rerun()

    with col2:

        if st.button(
            "Clear Chat",
            use_container_width=True
        ):

            st.session_state["messages"] = []
            st.rerun()

    st.divider()

    if len(st.session_state["messages"]) == 0:

        st.info(
            """
    **Welcome!**

    Ask anything about this repository.

    Example questions:

    - Explain the project architecture.
    - How is authentication implemented?
    - What are the main modules?
    - Explain the API flow.
    - How is the database connected?
    """
        )

    # Show previous chat messages
    for msg in st.session_state["messages"]:

        with st.chat_message(msg["role"]):

            st.markdown(msg["content"])


    # Make sure a repository has been processed
    if st.session_state["repo_name"] == "":

        st.warning("Please process a repository first.")

        st.stop()


    # Chat input
    user_question = st.chat_input(
        "Ask anything about the repository..."
    )


    if user_question:

        # Save user message
        st.session_state["messages"].append({

            "role": "user",

            "content": user_question

        })

        with st.chat_message("user"):

            st.markdown(user_question)

        with st.chat_message("assistant"):

            with st.spinner(
                "Retrieving relevant code and generating response..."
            ):

                results = retrieve_chunks(
                    user_question,
                    st.session_state["repo_name"]
                )

                chat_history = ""

                for msg in st.session_state["messages"]:

                    chat_history += (
                        f"{msg['role']}: {msg['content']}\n"
                    )

                answer = generate_answer(
                    user_question,
                    results,
                    chat_history
                )

            st.markdown(answer)

        # Save assistant response
        st.session_state["messages"].append({

            "role": "assistant",

            "content": answer

        })

        st.rerun()