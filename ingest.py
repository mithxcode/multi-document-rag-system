from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

documents = []

pdf_folder = "pdfs"

for file in os.listdir(pdf_folder):

    if file.endswith(".pdf"):

        print(f"Loading {file}")

        loader = PyPDFLoader(
            os.path.join(pdf_folder, file)
        )

        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = file

        documents.extend(docs)

print(f"\nTotal Pages: {len(documents)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Chunks: {len(chunks)}")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    index_name="mithilesh-kumar"
)

print("✅ Upload Complete")