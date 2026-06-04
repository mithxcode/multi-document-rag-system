import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Title
st.title("📚 PDF RAG Chatbot")
st.write("Ask questions from your PDF")

# Load Models
@st.cache_resource
def load_components():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = PineconeVectorStore(
        index_name="mithilesh-kumar",
        embedding=embeddings
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )

    return vector_store, llm

vector_store, llm = load_components()

# Session Memory
if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Ask a Question")

if st.button("Submit") and question:

    with st.spinner("Searching PDF..."):

        docs = vector_store.similarity_search(
            question,
            k=5
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
You are an expert PDF assistant.

Use ONLY the provided context.

Context:
{context}

Question:
{question}

Answer clearly.
"""

        response = llm.invoke(prompt)

        answer = response.content

        st.session_state.history.append(
            (question, answer)
        )

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        pages = set()

        for doc in docs:
            page = doc.metadata.get("page")

            if page is not None:
                pages.add(page + 1)

        st.write(
            f"Pages: {sorted(list(pages))}"
        )

# Chat History
if st.session_state.history:

    st.subheader("Chat History")

    for q, a in reversed(
        st.session_state.history
    ):

        st.markdown(
            f"**Q:** {q}"
        )

        st.markdown(
            f"**A:** {a}"
        )

        st.divider()