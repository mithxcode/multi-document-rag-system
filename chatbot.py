from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# =========================
# Embeddings
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# Pinecone
# =========================

vector_store = PineconeVectorStore(
    index_name="mithilesh-kumar",
    embedding=embeddings
)

# =========================
# Gemini
# =========================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

# =========================
# Memory
# =========================

chat_history = []
last_answer = ""

print("\n🚀 Advanced PDF RAG Chatbot Ready")
print("Type 'exit' to quit.\n")

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    # =========================
    # NO QUERY REWRITING
    # =========================

    history_text = "\n".join(chat_history[-6:])

    rewritten_question = question

    print(f"\n🔄 Query: {rewritten_question}")

    # =========================
    # Retrieval
    # =========================

    results = vector_store.similarity_search_with_score(
        rewritten_question,
        k=5
    )

    docs = [doc for doc, score in results]

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # =========================
    # Retrieval Scores
    # =========================

    print("\n🔍 Retrieval Scores")

    for i, (_, score) in enumerate(results):
        print(f"Chunk {i+1}: {score:.4f}")

    # =========================
    # Prompt
    # =========================

    prompt = f"""
You are an intelligent PDF assistant.

Use the PDF context as the primary source.

Conversation History:
{history_text}

Previous Answer:
{last_answer}

PDF Context:
{context}

Question:
{rewritten_question}

Rules:

1. Answer using PDF context.
2. If user asks follow-up questions like:
   - explain it
   - explain shortly
   - give example
   - what are its advantages
   then use conversation history and previous answer.
3. If answer is unavailable, say:
   "I could not find this information in the PDF."

Provide:

1. Clear Answer
2. Important Points
3. Simple Explanation
"""

    try:

        response = llm.invoke(prompt)

        print("\n" + "=" * 60)
        print("📌 ANSWER")
        print("=" * 60)

        print(response.content)

        # =========================
        # Sources
        # =========================

        print("\n📚 SOURCES")

        pages = set()
        files = set()

        for doc, score in results:

            page = doc.metadata.get("page")
            source = doc.metadata.get("source")

            if page is not None:
                pages.add(page + 1)

            if source:
                files.add(source)

        print("\nFiles:")

        for file in sorted(files):
            print(f"• {file}")

        print("\nPages:")

        for page in sorted(pages):
            print(f"• Page {page}")

        # =========================
        # Update Memory
        # =========================

        last_answer = response.content

        chat_history.append(
            f"User: {question}"
        )

        chat_history.append(
            f"Assistant: {response.content}"
        )

    except Exception as e:

        print("\n❌ ERROR:")
        print(e)

    print("\n" + "-" * 60)