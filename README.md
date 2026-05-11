cat > README.md << 'README_EOF'
<div align="center">

# 🌾 Krishi Bondo

### Your AI-Powered Agricultural Companion

**Hybrid RAG System · Multilingual · Privacy-First**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=flat)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama--3.1-F55036?style=flat)](https://groq.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Local-FF6B6B?style=flat)](https://www.trychroma.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Features](#-features) · [Demo](#-demo) · [Quick Start](#-quick-start) · [Architecture](#-architecture) · [API](#-api-reference)

</div>

---

## 🌟 What is Krishi Bondo?

**Krishi Bondo** (meaning *"Farmer's Friend"* in Bangla) is a professional-grade AI assistant that helps farmers make informed decisions about their crops. Built as a **Hybrid Retrieval-Augmented Generation (RAG)** system, it combines a curated agricultural knowledge base with the reasoning power of Meta's Llama-3.1 to deliver expert advice in real time — in **both English and Bangla** 🇧🇩.

> *"From soil to harvest — your AI agronomist, always available."*

---

## ✨ Features

### 🧠 **Hybrid Intelligence**
- 📚 **Knowledge Base Mode** — Answers from curated, research-grade data on Rice, Potato, and Tomato (ICAR, IRRI, FAO sourced)
- 🌐 **General AI Mode** — Falls back to Llama-3.1 for any agricultural topic outside the knowledge base
- 🎯 **Smart Routing** — Cosine-similarity-based decision making with confidence scoring

### 🌏 **True Multilingual Support**
- 🇬🇧 **English** — Clean, professional responses
- 🇧🇩 **Bangla (বাংলা)** — Native Bangla replies regardless of input language
- 🔀 **Banglish/Avro tolerant** — Ask in romanized Bangla, get pure Bangla answers
- 🔁 **One-click toggle** — Switch languages anywhere in the UI

### 🎨 **Premium UI/UX**
- ✨ **Gemini-inspired design** — Modern, minimalist, distraction-free
- 🌗 **Light & Dark mode** — System-aware with manual override
- 📱 **Fully responsive** — Phone, tablet, desktop
- 💬 **Chat history** — Persistent across sessions via localStorage
- 🌤️ **Live weather widget** — Real-time local weather (Open-Meteo)
- 💡 **Smart suggestions** — Quick-start prompts for common queries

### ⚡ **Performance & Privacy**
- 🚀 **Sub-second inference** — Groq's blazing-fast LPU infrastructure
- 🔒 **Local embeddings** — HuggingFace MiniLM runs entirely on your machine
- 💾 **Local vector DB** — ChromaDB stores your knowledge base on disk
- 🆓 **Zero embedding costs** — Free, offline, M-series Mac optimized
- 🛡️ **Secrets safe** — API keys protected by `.gitignore`

---

## 🎬 Demo

<div align="center">

### Knowledge Base Mode (Curated Answer)
> 🌾 **Q:** *"How do I control brown planthopper in rice?"*  
> 📚 **A:** Structured answer with causes, solutions, and prevention — **73% match** from KB.

### General AI Mode (Fallback)
> 🍓 **Q:** *"How do I grow strawberries in winter?"*  
> 🌐 **A:** Expert advice from Llama-3.1 — falls back gracefully when KB doesn't cover it.

### Bangla Mode (Forced Bangla Output)
> 🌾 **Q (English):** *"How do I control brown planthopper in rice?"*  
> 🇧🇩 **A (Bangla):** **ধানে বাদামি গাছ ফড়িং দমন** — কারণ, সমাধান, প্রতিরোধ সহ পূর্ণ বাংলা উত্তর।

</div>

---

## 🏗️ Architecture

┌─────────────────────────────────────────────────────────────────┐
│                         USER (Browser)                          │
│              Gemini-Style UI · EN / বাংলা Toggle                 │
└──────────────────────────────┬──────────────────────────────────┘
│ HTTPS / JSON
▼
┌─────────────────────────────────────────────────────────────────┐
│                      FASTAPI SERVER                             │
│       /chat · /health · /docs · CORS · Lifespan                 │
└──────────────────────────────┬──────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│                    KRISHI BONDO ENGINE                          │
│                                                                 │
│   ┌─────────────────┐         ┌──────────────────────────┐      │
│   │  HuggingFace    │────────▶│      ChromaDB            │      │
│   │  Embeddings     │  embed  │  (Local Vector Store)    │      │
│   │  (MiniLM, 22M)  │         │   46 chunks · 3 crops    │      │
│   └─────────────────┘         └────────────┬─────────────┘      │
│                                            │                    │
│                            similarity_search                    │
│                                            │                    │
│                            ┌───────────────▼───────────────┐    │
│                            │   Above threshold?            │    │
│                            └───────┬───────────────┬───────┘    │
│                                    │YES         NO │            │
│                                    ▼               ▼            │
│                          ┌──────────────┐ ┌──────────────┐      │
│                          │  RAG Chain   │ │  Fallback    │      │
│                          │  (KB + LLM)  │ │  Chain (LLM) │      │
│                          └──────┬───────┘ └──────┬───────┘      │
│                                 │                │              │
│                                 └────────┬───────┘              │
│                                          ▼                      │
│                              ┌────────────────────────┐         │
│                              │   GROQ API             │         │
│                              │   Llama-3.1-8b-instant │         │
│                              └────────────────────────┘         │
└─────────────────────────────────────────────────────────────────┘

---

## 🛠️ Tech Stack

| Layer            | Technology                                      | Purpose                          |
|------------------|-------------------------------------------------|----------------------------------|
| **Backend**      | FastAPI · Uvicorn · Pydantic                    | Async API server with validation |
| **AI Framework** | LangChain · LangChain-Groq · LangChain-Chroma   | Orchestration & chains           |
| **LLM**          | Groq Cloud · Llama-3.1-8b-instant               | Generation                       |
| **Embeddings**   | sentence-transformers (MiniLM-L6-v2)            | Local, free vector encoding      |
| **Vector DB**    | ChromaDB                                        | Persistent semantic search       |
| **Frontend**     | HTML5 · Tailwind CSS · Vanilla JS · marked.js   | Zero-build interactive UI        |
| **Fonts**        | Plus Jakarta Sans · Hind Siliguri (Bangla)      | Beautiful typography             |
| **Weather**      | Open-Meteo API                                  | Free, no-auth weather data       |

---

## 🚀 Quick Start

### Prerequisites
- 🐍 **Python 3.12** (3.11+ works; 3.13+ untested)
- 🍎 **macOS / Linux / Windows** (M-series Mac optimized)
- 🔑 **Free Groq API key** → [console.groq.com](https://console.groq.com/keys)

### Installation

#### 1️⃣ Clone & Enter
```bash
git clone https://github.com/yourusername/krishi-bondo.git
cd krishi-bondo
```

#### 2️⃣ Create Virtual Environment
```bash
python3.12 -m venv .venv
source .venv/bin/activate           # macOS / Linux
# .venv\Scripts\activate            # Windows
```

#### 3️⃣ Install Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

#### 4️⃣ Configure API Key
Create `.env` in the project root:
```env
GROQ_API_KEY=gsk_your_actual_key_here
GROQ_MODEL=llama-3.1-8b-instant
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
CHROMA_DB_PATH=./chroma_db
COLLECTION_NAME=krishi_knowledge
TOP_K_RESULTS=3
SIMILARITY_THRESHOLD=0.5
HOST=0.0.0.0
PORT=8000
```

> 💡 **Get a free Groq key** in 30 seconds — no credit card needed.

#### 5️⃣ Launch! 🚀
```bash
./run.sh
```

Open **[http://localhost:8000](http://localhost:8000)** and start asking questions! 🌾

---

## 📂 Project Structure

krishi-bondo/
│
├── app/
│   ├── init.py
│   ├── main.py                  # FastAPI server · routes · CORS
│   ├── core_ai.py               # RAG engine · LangChain · Groq
│   └── knowledge_base.py        # Curated crop data (Rice, Potato, Tomato)
│
├── frontend/
│   └── index.html               # Gemini-style chat UI
│
├── chroma_db/                   # (auto-generated) Persistent vector store
│
├── .env                         # Secrets (gitignored)
├── .gitignore
├── requirements.txt             # Pinned dependencies
├── run.sh                       # One-command launcher
└── README.md

---

## 🔌 API Reference

### `POST /chat`
Ask Krishi Bondo a question.

**Request:**
```json
{
  "question": "How do I control late blight in potatoes?",
  "language": "en"
}
```

**Response:**
```json
{
  "answer": "**Late blight** in potatoes is caused by *Phytophthora infestans*...",
  "source": "knowledge_base",
  "confidence": 0.812,
  "sources": [
    { "crop": "potato", "section": "common_diseases", "scientific_name": "Solanum tuberosum" }
  ]
}
```

**Parameters:**
| Field      | Type     | Required | Description                          |
|------------|----------|----------|--------------------------------------|
| `question` | string   | ✅       | Farmer's question (1–2000 chars)     |
| `language` | string   | ❌       | `"en"` or `"bn"` (default: `"en"`)   |

---

### `GET /health`
Check engine status.

**Response:**
```json
{
  "status": "ready",
  "model": "llama-3.1-8b-instant",
  "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
  "knowledge_base_chunks": 46,
  "supported_crops": ["rice", "potato", "tomato"],
  "similarity_threshold": 0.5
}
```

---

### `GET /docs`
Interactive Swagger UI for API testing.

---

## 🧬 How Hybrid RAG Works

1. **Embed:** User question is converted to a 384-dim vector locally (MiniLM)
2. **Retrieve:** ChromaDB performs cosine similarity search over 46 knowledge chunks
3. **Decide:** If best match similarity ≥ 0.5 → use KB. Otherwise → fall back to general LLM
4. **Generate:** Llama-3.1 produces the answer with strict language enforcement
5. **Respond:** UI displays answer with source badge (KB vs General AI) and confidence

---

## 📊 Knowledge Base Coverage

Each crop covers **13+ sections**:
- 🌱 Scientific classification & overview
- 🪴 Soil & climate requirements
- 📅 Growing seasons & varieties
- 💧 Water management
- 🌿 Fertilizer recommendations
- 🐛 Common pests (with chemical names)
- 🦠 Diseases & treatments
- 🌾 Harvesting & yield benchmarks

**Currently supported:**
- 🌾 **Rice** (*Oryza sativa*)
- 🥔 **Potato** (*Solanum tuberosum*)
- 🍅 **Tomato** (*Solanum lycopersicum*)

> Extending coverage is trivial — just append to `app/knowledge_base.py` and restart.

---

## 🗺️ Roadmap

- [x] Hybrid RAG with KB + Fallback
- [x] English + Bangla support
- [x] Chat history persistence
- [x] Weather widget
- [ ] 📸 Image-based pest detection (vision LLM)
- [ ] 📄 PDF knowledge ingestion
- [ ] 🗣️ Voice input for low-literacy users
- [ ] 🌐 Hindi, Telugu, Tamil support
- [ ] 💬 Multi-turn conversation memory
- [ ] ☁️ Production deployment guide (Railway/Fly.io)

---

## 🤝 Contributing

Contributions are welcome! Whether it's expanding the knowledge base, improving Bangla translations, or adding new features:

```bash
git checkout -b feature/your-feature
# make changes
git commit -m "feat: add amazing feature"
git push origin feature/your-feature
# open a PR
```

---

## 🙏 Acknowledgments

- 🤖 **[Groq](https://groq.com/)** — for the world's fastest LLM inference
- 🤗 **[HuggingFace](https://huggingface.co/)** — for free, open embedding models
- 🦜 **[LangChain](https://www.langchain.com/)** — for elegant RAG orchestration
- 🎨 **[Tailwind CSS](https://tailwindcss.com/)** — for utility-first styling
- 🌾 **[ICAR](https://icar.org.in/) · [IRRI](https://www.irri.org/) · [FAO](https://www.fao.org/)** — for open agricultural research

---

## 📜 License

Released under the **MIT License**. See [LICENSE](LICENSE) for details.

---

<div align="center">

### Built with ❤️ for farmers everywhere

**If Krishi Bondo helps you, please give it a ⭐ on GitHub!**

[Report Bug](https://github.com/yourusername/krishi-bondo/issues) · [Request Feature](https://github.com/yourusername/krishi-bondo/issues) · [Star Project](https://github.com/yourusername/krishi-bondo)

</div>
README_EOF