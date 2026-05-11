"""
================================================================================
KRISHI BONDO — FASTAPI SERVER (Voice + Image + Multilingual)
================================================================================
"""

import logging
import tempfile
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.core_ai import get_engine

# ============================================================
# CONFIGURATION
# ============================================================

logger = logging.getLogger("krishi-bondo.server")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
INDEX_HTML = FRONTEND_DIR / "index.html"


# ============================================================
# MODELS
# ============================================================

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)
    language: str = Field(default="en")


class SourceInfo(BaseModel):
    crop: Optional[str] = None
    section: Optional[str] = None
    scientific_name: Optional[str] = None


class ChatResponse(BaseModel):
    answer: str
    source: str
    confidence: float
    sources: list[SourceInfo] = []


class HealthResponse(BaseModel):
    status: str
    model: str
    embedding_model: str
    knowledge_base_chunks: int
    supported_crops: list[str]
    similarity_threshold: float


class TranscribeResponse(BaseModel):
    text: str
    language: Optional[str] = None


# ============================================================
# LIFESPAN
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Starting Krishi Bondo server...")
    engine = get_engine()
    stats = engine.get_stats()
    logger.info(f"✅ Engine pre-loaded: {stats['knowledge_base_chunks']} chunks ready")
    yield
    logger.info("👋 Krishi Bondo server shutting down")


# ============================================================
# APP
# ============================================================

app = FastAPI(
    title="Krishi Bondo API",
    description="Hybrid RAG Agricultural AI Assistant with Voice & Vision",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


# ============================================================
# ROUTES
# ============================================================

@app.get("/", include_in_schema=False)
async def serve_frontend():
    if INDEX_HTML.exists():
        return FileResponse(INDEX_HTML)
    return JSONResponse(
        status_code=404,
        content={"error": "Frontend not found", "expected_path": str(INDEX_HTML)},
    )


@app.get("/health", response_model=HealthResponse, tags=["Monitoring"])
async def health_check():
    try:
        engine = get_engine()
        return HealthResponse(**engine.get_stats())
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail=f"Engine unhealthy: {e}")


@app.post("/chat", response_model=ChatResponse, tags=["AI"])
async def chat(request: ChatRequest):
    """Text-based Q&A with Hybrid RAG."""
    try:
        engine = get_engine()
        result = engine.answer(request.question, language=request.language)
        sources = [SourceInfo(**src) for src in result.get("sources", [])]
        return ChatResponse(
            answer=result["answer"],
            source=result["source"],
            confidence=result["confidence"],
            sources=sources,
        )
    except Exception as e:
        logger.error(f"Chat endpoint failed: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process question: {e}")


@app.post("/transcribe", response_model=TranscribeResponse, tags=["Voice"])
async def transcribe(audio: UploadFile = File(...)):
    """Speech-to-Text using Groq Whisper. Auto-detects language."""
    try:
        engine = get_engine()

        suffix = Path(audio.filename or "audio.webm").suffix or ".webm"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            content = await audio.read()
            tmp.write(content)
            tmp_path = tmp.name

        try:
            text = engine.transcribe_audio(tmp_path)
            return TranscribeResponse(text=text)
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    except Exception as e:
        logger.error(f"Transcription failed: {e}")
        raise HTTPException(status_code=500, detail=f"Transcription failed: {e}")


@app.post("/analyze-image", response_model=ChatResponse, tags=["Vision"])
async def analyze_image(
    image: UploadFile = File(...),
    question: str = Form(default="What do you see in this crop image? Identify any issues, pests, or diseases."),
    language: str = Form(default="en"),
):
    """Vision-based crop/pest/disease analysis using Llama-4 Scout."""
    try:
        engine = get_engine()

        suffix = Path(image.filename or "img.jpg").suffix or ".jpg"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            content = await image.read()
            tmp.write(content)
            tmp_path = tmp.name

        try:
            result = engine.analyze_image(tmp_path, question=question, language=language)
            sources = [SourceInfo(**src) for src in result.get("sources", [])]
            return ChatResponse(
                answer=result["answer"],
                source=result["source"],
                confidence=result["confidence"],
                sources=sources,
            )
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    except Exception as e:
        logger.error(f"Image analysis failed: {e}")
        raise HTTPException(status_code=500, detail=f"Image analysis failed: {e}")


@app.get("/api/info", tags=["Info"])
async def api_info():
    return {
        "name": "Krishi Bondo",
        "description": "Agricultural AI Assistant — Hybrid RAG + Voice + Vision",
        "version": "2.0.0",
        "endpoints": {
            "frontend": "GET  /",
            "chat": "POST /chat",
            "transcribe": "POST /transcribe",
            "analyze_image": "POST /analyze-image",
            "health": "GET  /health",
            "docs": "GET  /docs",
        },
    }


if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


# ============================================================
# DEV ENTRY POINT
# ============================================================

if __name__ == "__main__":
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))

    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info",
    )