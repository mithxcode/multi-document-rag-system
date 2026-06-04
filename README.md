# 🚀 Agentic PDF RAG Chatbot

An advanced Retrieval-Augmented Generation (RAG) application that enables users to interact with PDF documents using natural language. The system leverages semantic search, vector embeddings, and Large Language Models (LLMs) to provide accurate, context-aware answers directly from uploaded PDF content.

Built with **LangChain**, **Pinecone**, **Hugging Face Embeddings**, **Google Gemini**, and **Streamlit**.

---

## 📖 Overview

Traditional chatbots often generate responses based solely on their pre-trained knowledge, which may result in outdated or inaccurate answers. This project implements a **Retrieval-Augmented Generation (RAG)** architecture, allowing the chatbot to retrieve relevant information from PDF documents before generating responses.

The application:

- Extracts content from PDF files
- Splits documents into manageable chunks
- Converts text into vector embeddings
- Stores embeddings in Pinecone Vector Database
- Retrieves relevant chunks using semantic search
- Uses Gemini LLM to generate accurate responses
- Displays source references for transparency

---

## ✨ Features

### Document Processing
- PDF ingestion pipeline
- Automatic text extraction
- Intelligent text chunking
- Metadata preservation

### Retrieval System
- Semantic search using embeddings
- Pinecone vector database integration
- Similarity-based document retrieval
- Context-aware information extraction

### AI-Powered Question Answering
- Google Gemini 2.5 Flash integration
- Context-grounded response generation
- Follow-up conversation support
- Source-aware answering

### User Experience
- Interactive Streamlit interface
- Chat history tracking
- Source page references
- Real-time response generation

---

## 🏗️ System Architecture

```text
PDF Documents
      │
      ▼
Document Loader
(PyPDFLoader)
      │
      ▼
Text Chunking
(RecursiveCharacterTextSplitter)
      │
      ▼
Embedding Generation
(HuggingFace MiniLM)
      │
      ▼
Pinecone Vector Database
      │
      ▼
Semantic Retrieval
      │
      ▼
Gemini LLM
      │
      ▼
Final Response
      │
      ▼
Streamlit UI
```

---

## 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Framework | LangChain |
| Vector Database | Pinecone |
| Embeddings | HuggingFace MiniLM |
| Large Language Model | Gemini 2.5 Flash |
| User Interface | Streamlit |
| PDF Processing | PyPDF |
| Environment Management | python-dotenv |

---

## 📂 Project Structure

```text
agentic-pdf-rag-chatbot/
│
├── pdfs/
│   └── dsa.pdf
│
├── ingest.py
├── chatbot.py
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/mithxcode/agentic-pdf-rag-chatbot.git

cd agentic-pdf-rag-chatbot
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

PINECONE_API_KEY=YOUR_PINECONE_API_KEY
```

---

## 📄 Adding PDF Documents

Create a folder named:

```text
pdfs
```

Place all PDF files inside the folder:

```text
pdfs/
├── dsa.pdf
├── dbms.pdf
├── os.pdf
└── cn.pdf
```

---

## 📥 Indexing Documents

Before using the chatbot, upload document embeddings to Pinecone.

Run:

```bash
python ingest.py
```

Expected Output:

```text
Loading dsa.pdf

Total Pages: 120

Chunks: 231

Upload Complete
```

This process:

1. Loads PDFs
2. Extracts text
3. Creates chunks
4. Generates embeddings
5. Stores vectors in Pinecone

---

## 🤖 Running the Terminal Chatbot

Launch the command-line version:

```bash
python chatbot.py
```

Example:

```text
Ask Question:

What is Quick Sort?
```

Output:

```text
Clear Answer

Important Points

Simple Explanation

Sources:
Page 30
Page 34
Page 35
```

---

## 🌐 Running the Streamlit Web Application

Start the web interface:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 💬 Example Questions

```text
What is Quick Sort?

Explain Binary Search Tree.

What are the advantages of AVL Trees?

Difference between Stack and Queue.

Explain Heap Sort with example.

What is Dynamic Programming?
```

---

## 🔍 Retrieval-Augmented Generation Workflow

```text
User Query
     │
     ▼
Generate Query Embedding
     │
     ▼
Pinecone Similarity Search
     │
     ▼
Retrieve Relevant Chunks
     │
     ▼
Build Context
     │
     ▼
Gemini LLM
     │
     ▼
Generate Answer
     │
     ▼
Display Sources
```

---

## 📚 Source Attribution

The chatbot provides document transparency by displaying:

- Source PDF file
- Referenced page numbers
- Retrieved document chunks

Example:

```text
Files:
• dsa.pdf

Pages:
• Page 30
• Page 34
• Page 35
```

---

## 🚀 Future Enhancements

### Advanced Retrieval

- Query Rewriting
- MMR Retrieval
- Context Compression
- Hybrid Search (BM25 + Vector Search)
- Cross Encoder Reranking

### Agentic AI Features

- Tool Calling
- Query Planning
- Multi-Step Reasoning
- Reflection Agents
- Autonomous Retrieval

### User Experience

- ChatGPT-style Chat Interface
- Streaming Responses
- PDF Upload Feature
- Dark Mode Support
- Multi-PDF Selection

### Production Features

- User Authentication
- Persistent Chat History
- Analytics Dashboard
- Docker Deployment
- Cloud Hosting

---

## 📊 Current Capabilities

| Feature | Status |
|----------|---------|
| PDF Processing | ✅ |
| Semantic Search | ✅ |
| Pinecone Integration | ✅ |
| Gemini Integration | ✅ |
| Source Citations | ✅ |
| Streamlit UI | ✅ |
| Chat Memory | ✅ |
| Multi-PDF Support | ✅ |
| Query Rewriting | 🚧 |
| Agentic Workflow | 🚧 |
| Reranking | 🚧 |

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Embedding Models
- Large Language Models
- LangChain Framework
- Streamlit Applications
- AI-Powered Knowledge Systems

---

## 👨‍💻 Author

### Mithilesh Kumar

AI Enthusiast | Full Stack Developer | Generative AI Learner

**GitHub:**  
https://github.com/mithxcode

**LinkedIn:**  
https://www.linkedin.com/in/mithileshkumar001

---

## 🌟 Support

If you found this project useful, consider giving it a star ⭐ on GitHub.

Contributions, feature suggestions, and feedback are always welcome.

---

