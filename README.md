Your project is good and **very suitable for a GitHub portfolio**, especially for AI/ML or AI Engineer roles. It shows:

* LangGraph agent workflow
* RAG with FAISS
* Tool usage
* Streamlit frontend
* Multi-stage hospital workflow (admission → preparation → discharge → follow-up)

This is exactly the kind of **AI system project recruiters like to see**.

Below are suggestions for **repository name, description, and a full README.md**.

---

# 1️⃣ Suggested GitHub Repository Names

Choose a **clear and professional name**.

### Best Options

1. **hospital-ai-assistant**
2. **patient-hospitalisation-ai-agent**
3. **hospital-support-ai-assistant**
4. **rag-hospital-assistant**
5. **patient-care-ai-agent**

✅ **Recommended:**
`hospital-ai-assistant`

Reason:
Simple, clear, and searchable.

---

# 2️⃣ GitHub Repository Description

Use a **short description (1–2 lines)**.

**Option 1 (Best)**

> AI-powered Hospital Assistant built with LangGraph, RAG, and Streamlit that helps patients prepare for hospitalisation, surgery, discharge, and follow-up care.

**Option 2**

> A LangGraph-based AI assistant that guides patients through hospital admission, surgery preparation, discharge process, and post-hospital follow-up using a RAG knowledge base.

---

# 3️⃣ Complete README.md

You can copy this directly into your repo.

---

# 🏥 Hospital AI Assistant

An **AI-powered assistant that helps patients prepare for hospitalisation** by answering questions about admission, surgery preparation, discharge, and follow-up care.

This project demonstrates how to build a **tool-using AI agent with LangGraph, RAG, and Streamlit**.

The assistant retrieves hospital knowledge from a **PDF knowledge base** and provides structured responses to patients.

---

# 🚀 Features

### 🧠 AI Agent (LangGraph)

* Uses **LangGraph workflow**
* Supports **tool calling**
* Maintains **conversation memory with SQLite**

### 📚 RAG Knowledge Base

* Uses **FAISS vector database**
* Embeddings from **HuggingFace sentence-transformers**
* Retrieves hospital documents dynamically

### 🏥 Hospital Guidance

The assistant helps patients understand:

* Admission requirements
* Documents required for hospitalisation
* Pre-surgery preparation
* Hospital discharge process
* Post-hospital follow-up care

### 🛠 Tools Used by Agent

| Tool                        | Purpose                                 |
| --------------------------- | --------------------------------------- |
| hospital_knowledge_tool     | Retrieves hospital information from RAG |
| surgery_details_tool        | Returns patient surgery schedule        |
| contact_representative_tool | Provides hospital support contact       |

### 💬 Interactive Chat Interface

* Built with **Streamlit**
* Chat-style UI
* Session-based conversations
* Multi-thread conversation history

---

# 🏗 System Architecture

The AI assistant follows a **tool-augmented agent workflow**.

```
User Query
   ↓
Streamlit UI
   ↓
LangGraph Agent
   ↓
Tool Selection
   ↓
RAG Retrieval / Hospital System
   ↓
Final Response
```

---

# 📂 Project Structure

```
Project/
│
├── app.py                # Streamlit UI
├── main.py               # LangGraph agent workflow
├── tools.py              # Agent tools
├── prompt.py             # System prompt
├── requirements.txt
│
├── assets/
│   ├── langsmith_trace.png
│   └── workflow.png
│
└── rag/
    ├── retriever.py
    ├── vectorstores/
    └── docs/
        ├── ADMISSION_DOCS
        │   └── admission_requirements.pdf
        │
        ├── PREPARATION_DOCS
        │   └── pre_surgery_preparation.pdf
        │
        ├── DISCHARGE_DOCS
        │   └── hospital_discharge_process.pdf
        │
        └── FOLLOWUP_DOCS
            └── post_hospital_followup.pdf
```

---

# ⚙️ Tech Stack

| Technology                 | Usage                        |
| -------------------------- | ---------------------------- |
| **LangChain**              | LLM framework                |
| **LangGraph**              | Agent workflow orchestration |
| **Streamlit**              | Frontend interface           |
| **FAISS**                  | Vector database              |
| **HuggingFace Embeddings** | Text embeddings              |
| **Ollama (Qwen model)**    | Local LLM                    |
| **SQLite**                 | Chat memory storage          |

---

# 📚 Knowledge Base

The assistant uses **RAG (Retrieval Augmented Generation)** to retrieve hospital documents.

Categories:

* Admission Documents
* Surgery Preparation
* Hospital Discharge
* Post-Hospital Follow-up

Each category has its own **FAISS vector index**.

---

# 🧠 AI Agent Workflow

The LangGraph workflow contains two main nodes:

```
START
  ↓
Agent Node (LLM)
  ↓
Tool Router
  ↓
Tool Node
  ↓
Agent Node
  ↓
END
```

The agent decides which tool to use based on the user query.

---

# ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/hospital-ai-assistant.git
cd hospital-ai-assistant
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Start Ollama Model

Make sure **Ollama** is running.

```bash
ollama run qwen3:4b
```

---

### 4️⃣ Build Vector Database

Run the retriever script once to build FAISS indexes.

```bash
python rag/retriever.py
```

---

### 5️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 💬 Example Questions

You can ask:

* What documents are required for hospital admission?
* What should I bring before surgery?
* What happens during hospital discharge?
* What follow-up care is needed after hospitalisation?
* What is the surgery schedule for patient P1001?


---

# 🎯 Learning Outcomes

This project demonstrates:

* Building **AI agents using LangGraph**
* Implementing **RAG pipelines**
* Designing **tool-calling LLM systems**
* Creating **LLM-powered applications with Streamlit**
* Managing **conversation memory**

---

# 🔮 Future Improvements

* Add **real hospital API integration**
* Improve **multi-patient support**
* Add **authentication**
* Add **medical appointment scheduling**
* Use **LangSmith monitoring**
---

# 👨‍💻 Author

**Aakash Gayke**

Aspiring **AI Engineer / ML Engineer**
