# 🧠 AI Twin at Work

## 📌 Overview

**AI Twin at Work** is a personalized, local-first assistant that simulates an intelligent daily work companion. It ingests your emails, calendar events, and notes, and helps you:

- Summarize your daily work activity
- Track open loops and pending tasks
- Query your day in natural language
- View structured calendar and note insights

> This prototype is completely offline and privacy-preserving using open-source models.

---

## 🚀 Problem It Solves

In today’s fast-paced work environments, people struggle to keep track of:

- What they did throughout the day
- Meetings and follow-ups
- Important notes scattered across tools

**AI Twin** addresses this by acting as your daily memory—ingesting raw inputs and turning them into actionable, queryable summaries.

---

## 🛠️ Approach & Architecture

The solution is built using:

- **FastAPI** for the web interface
- **Sentence Transformers** for embeddings
- **ChromaDB** for vector-based search
- **Hugging Face Transformers** for summarization and Q&A
- **HTML/JS UI** with a tabbed layout

### 📂 Workflow

1. **Data Ingestion**: Parses `.json` email/calendar + `.md` notes
2. **Embedding & Indexing**: Semantic vector store with Chroma
3. **Summarization**: Daily overview generated using `distilbart-cnn`
4. **RAG-based QA**: Contextual answers from your own work history
5. **Frontend**: Simple tabbed UI (Summary, Calendar, Notes + Ask)

---

## 💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-twin.git
cd ai-twin
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Data

Create a `data/` folder and include:

- `email.json`: Mock emails
- `calendar.json`: Calendar events
- `notes.md`: Raw notes

Sample data is already included or can be extended.

### 5. Run the App

```bash
uvicorn main:app --reload
```

Then open your browser at: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Example Questions You Can Ask

- "What did I do today?"
- "What meetings involved Alex?"
- "Which tasks are still open?"

---

## ✨ Features Planned

- ⏳ Real-time ingestion from Gmail/Google Calendar
- 📅 Date-wise filter for meetings
- 🗃️ Downloadable daily summaries
- 🔒 Fine-grained PII detection
