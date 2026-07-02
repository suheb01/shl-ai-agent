# SHL AI Assessment Recommendation Agent

## Overview

The SHL AI Assessment Recommendation Agent is an AI-powered recruitment assistant that recommends the most relevant SHL assessments based on recruiter requirements.

The application uses Retrieval-Augmented Generation (RAG) by combining semantic search with Google's Gemini model. Recruiter requirements are extracted from the conversation, matched against the SHL assessment catalog using vector embeddings stored in ChromaDB, and then Gemini generates professional recommendations based only on the retrieved assessments.

---

## Features

- AI-powered SHL assessment recommendations
- Requirement extraction from recruiter conversations
- Semantic search using Sentence Transformers
- ChromaDB vector database
- Google Gemini integration
- FastAPI REST API
- Modular and scalable architecture
- Multi-turn conversation support

---

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- ChromaDB
- Sentence Transformers
- Google Gemini API
- HuggingFace Transformers
- Uvicorn

---

## Project Structure

```
shl-ai-agent/
│
├── app/
│   ├── agent/
│   ├── api/
│   ├── data/
│   ├── models/
│   ├── retriever/
│   ├── scraper/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Architecture

```
Recruiter Query
        │
        ▼
FastAPI
        │
        ▼
Conversation Service
        │
        ▼
Requirement Extraction
        │
        ▼
Semantic Search
(Sentence Transformers + ChromaDB)
        │
        ▼
Top Matching SHL Assessments
        │
        ▼
Gemini 2.5 Flash
        │
        ▼
Professional Recommendation
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/suheb01/shl-ai-agent.git

cd shl-ai-agent
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```
GET /health
```

### Chat Endpoint

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Looking for a Senior Java Developer with 5 years of experience."
    }
  ]
}
```

---

## How It Works

1. Recruiter enters hiring requirements.
2. Requirements are extracted from the conversation.
3. A semantic query is generated.
4. ChromaDB retrieves the most relevant SHL assessments.
5. Gemini ranks and explains the recommendations.
6. The API returns structured recommendations.

---

## Future Improvements

- Better multi-turn conversation handling
- Metadata-aware ranking
- Advanced prompt engineering
- Logging and monitoring
- Docker support
- Cloud deployment

---

## Author

**Suheb Alam**

---

## License

This project was developed as part of the SHL Research AI Intern Assignment.