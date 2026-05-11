"""
================================================================================
KRISHI BONDO — CORE AI ENGINE (RAG + Voice + Vision + Multilingual)
================================================================================
"""

import os
import base64
import logging
from typing import Optional
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.knowledge_base import get_all_documents, get_supported_crops

# ============================================================
# CONFIGURATION
# ============================================================
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger("krishi-bondo")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
GROQ_VISION_MODEL = os.getenv("GROQ_VISION_MODEL", "meta-llama/llama-4-scout-17b-16e-instruct")
GROQ_WHISPER_MODEL = os.getenv("GROQ_WHISPER_MODEL", "whisper-large-v3")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "krishi_knowledge")
TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", "3"))
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.5"))

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file.")


# ============================================================
# PROMPT TEMPLATES — ENGLISH
# ============================================================

RAG_PROMPT_EN = """You are Krishi Bondo, a professional agricultural AI assistant 
helping farmers with crop cultivation, pest management, and yield optimization.

Use the following knowledge base context to answer the farmer's question.
Be specific, practical, and actionable. Use simple language a farmer can understand.

Structure your answer with clear sections if appropriate (e.g., Causes, Solutions, Prevention).

YOU MUST RESPOND ENTIRELY IN CLEAR, SIMPLE ENGLISH.

KNOWLEDGE BASE CONTEXT:
{context}

FARMER'S QUESTION:
{question}

PROFESSIONAL ANSWER (in English):"""


FALLBACK_PROMPT_EN = """You are Krishi Bondo, a professional agricultural AI assistant 
with deep expertise across all aspects of farming, agronomy, horticulture, and crop science.

Provide expert agricultural advice based on your general knowledge.

Guidelines:
- Be specific, practical, and actionable
- Mention scientific names, recommended practices, and typical dosages where relevant
- Use simple language a farmer can understand
- If the question is not agricultural, politely redirect to farming topics

YOU MUST RESPOND ENTIRELY IN CLEAR, SIMPLE ENGLISH.

FARMER'S QUESTION:
{question}

PROFESSIONAL EXPERT ANSWER (in English):"""


# ============================================================
# PROMPT TEMPLATES — BANGLA
# ============================================================

RAG_PROMPT_BN = """তুমি "কৃষি বন্ধু" — একজন পেশাদার কৃষি AI সহকারী, যিনি কৃষকদের ফসল চাষ, পোকামাকড় ব্যবস্থাপনা এবং ফলন বৃদ্ধিতে সাহায্য করেন।

নিচের জ্ঞান ভাণ্ডারের তথ্য ব্যবহার করে কৃষকের প্রশ্নের উত্তর দাও।
উত্তরটি সুনির্দিষ্ট, ব্যবহারিক এবং প্রয়োগযোগ্য হতে হবে। সহজ ভাষা ব্যবহার করো যাতে গ্রামের কৃষকও বুঝতে পারে।

প্রয়োজন অনুসারে উত্তরে স্পষ্ট বিভাগ ব্যবহার করো — যেমন: **কারণ**, **সমাধান**, **প্রতিরোধ**।

🔴 অত্যন্ত গুরুত্বপূর্ণ নিয়ম (কখনো লঙ্ঘন করো না):
1. তোমার সম্পূর্ণ উত্তর অবশ্যই বাংলা ভাষায় (বাংলা লিপিতে) দিতে হবে।
2. প্রশ্ন যে ভাষাতেই করা হোক — ইংরেজি, বাংলিশ (Banglish), Avro, বা বাংলা — উত্তর সবসময় বিশুদ্ধ বাংলায় দিতে হবে।
3. শুধুমাত্র বৈজ্ঞানিক নাম (যেমন Oryza sativa) এবং রাসায়নিক/কীটনাশকের নাম (যেমন Mancozeb, Imidacloprid, NPK) ইংরেজিতে রাখো।
4. কখনোই ইংরেজি বাক্য বা অনুচ্ছেদ লিখবে না — শুধু বৈজ্ঞানিক নাম ছাড়া।

জ্ঞান ভাণ্ডারের তথ্য:
{context}

কৃষকের প্রশ্ন:
{question}

পেশাদার উত্তর (অবশ্যই বাংলায়):"""


FALLBACK_PROMPT_BN = """তুমি "কৃষি বন্ধু" — একজন পেশাদার কৃষি AI সহকারী, যিনি চাষাবাদ, কৃষিবিজ্ঞান, উদ্যানপালন এবং ফসল বিজ্ঞানের সব বিষয়ে গভীর জ্ঞান রাখেন।

কৃষকের প্রশ্নের উত্তর তোমার সাধারণ জ্ঞান ব্যবহার করে পেশাদারভাবে দাও।

নির্দেশনা:
- সুনির্দিষ্ট, ব্যবহারিক এবং প্রয়োগযোগ্য উত্তর দাও
- প্রয়োজনে বৈজ্ঞানিক নাম, প্রস্তাবিত পদ্ধতি এবং সাধারণ মাত্রা উল্লেখ করো
- সহজ ভাষায় বলো যাতে কৃষক বুঝতে পারে
- প্রশ্ন কৃষি-সম্পর্কিত না হলে বিনয়ের সাথে কৃষি বিষয়ে ফিরিয়ে আনো

🔴 অত্যন্ত গুরুত্বপূর্ণ নিয়ম (কখনো লঙ্ঘন করো না):
1. তোমার সম্পূর্ণ উত্তর অবশ্যই বাংলা ভাষায় (বাংলা লিপিতে) দিতে হবে।
2. প্রশ্ন যে ভাষাতেই করা হোক — ইংরেজি, বাংলিশ (Banglish), Avro, বা বাংলা — উত্তর সবসময় বিশুদ্ধ বাংলায় দিতে হবে।
3. শুধুমাত্র বৈজ্ঞানিক নাম এবং রাসায়নিক/কীটনাশকের নাম ইংরেজিতে রাখো।
4. কখনোই ইংরেজি বাক্য বা অনুচ্ছেদ লিখবে না।

কৃষকের প্রশ্ন:
{question}

পেশাদার বিশেষজ্ঞ উত্তর (অবশ্যই বাংলায়):"""


# ============================================================
# VISION PROMPTS
# ============================================================

VISION_PROMPT_EN = """You are Krishi Bondo, an expert agricultural AI assistant analyzing a crop image.

Examine the image carefully and provide a professional, actionable analysis.

Your response should include (use markdown headings):
1. **What I See** — Brief description of the crop and visible condition
2. **Diagnosis** — Identify any visible diseases, pests, deficiencies, or issues
3. **Severity** — Mild / Moderate / Severe
4. **Immediate Actions** — Step-by-step treatment recommendations
5. **Prevention** — How to prevent this in future

If the image is unclear or not crop-related, politely say so and ask for a clearer photo.

YOU MUST RESPOND ENTIRELY IN CLEAR, SIMPLE ENGLISH.

FARMER'S QUESTION: {question}"""


VISION_PROMPT_BN = """তুমি "কৃষি বন্ধু" — একজন বিশেষজ্ঞ কৃষি AI সহকারী, যিনি একটি ফসলের ছবি বিশ্লেষণ করছেন।

ছবিটি যত্ন সহকারে পরীক্ষা করো এবং একটি পেশাদার, প্রয়োগযোগ্য বিশ্লেষণ দাও।

তোমার উত্তরে নিম্নলিখিত বিভাগগুলি থাকবে (markdown শিরোনাম ব্যবহার করো):
1. **আমি যা দেখছি** — ফসল এবং দৃশ্যমান অবস্থার সংক্ষিপ্ত বিবরণ
2. **রোগ নির্ণয়** — কোনো রোগ, পোকা, পুষ্টির অভাব বা সমস্যা শনাক্ত করো
3. **তীব্রতা** — হালকা / মাঝারি / গুরুতর
4. **তাৎক্ষণিক করণীয়** — ধাপে ধাপে চিকিৎসার পরামর্শ
5. **প্রতিরোধ** — ভবিষ্যতে এটি প্রতিরোধ করার উপায়

ছবি অস্পষ্ট বা ফসল-সম্পর্কিত না হলে বিনয়ের সাথে বলো এবং স্পষ্ট ছবি চাও।

🔴 অত্যন্ত গুরুত্বপূর্ণ নিয়ম:
1. তোমার সম্পূর্ণ উত্তর অবশ্যই বাংলা ভাষায় (বাংলা লিপিতে) দিতে হবে।
2. শুধুমাত্র বৈজ্ঞানিক নাম এবং রাসায়নিক/কীটনাশকের নাম ইংরেজিতে রাখো।
3. কখনোই ইংরেজি বাক্য বা অনুচ্ছেদ লিখবে না।

কৃষকের প্রশ্ন: {question}"""


# ============================================================
# CORE AI ENGINE
# ============================================================

class KrishiBondoEngine:
    """The brain of Krishi Bondo — RAG + Voice + Vision."""

    def __init__(self):
        logger.info("🌾 Initializing Krishi Bondo Engine...")
        self.embeddings = None
        self.vector_store = None
        self.llm = None
        self.groq_client = None
        self.rag_chain_en = None
        self.rag_chain_bn = None
        self.fallback_chain_en = None
        self.fallback_chain_bn = None
        self._initialize()

    def _initialize(self):
        try:
            logger.info(f"📦 Loading embedding model: {EMBEDDING_MODEL}")
            self.embeddings = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={"device": "cpu"},
                encode_kwargs={"normalize_embeddings": True},
            )
            logger.info("✅ Embedding model loaded successfully")

            logger.info(f"🗄️  Initializing ChromaDB at: {CHROMA_DB_PATH}")
            self.vector_store = Chroma(
                collection_name=COLLECTION_NAME,
                embedding_function=self.embeddings,
                persist_directory=CHROMA_DB_PATH,
            )

            self._populate_knowledge_base_if_empty()

            logger.info(f"🤖 Connecting to Groq with model: {GROQ_MODEL}")
            self.llm = ChatGroq(
                model=GROQ_MODEL,
                api_key=GROQ_API_KEY,
                temperature=0.4,
                max_tokens=1500,
            )

            # Direct Groq client for Whisper + Vision
            logger.info("🎙️  Setting up Groq client for Whisper & Vision...")
            self.groq_client = Groq(api_key=GROQ_API_KEY)

            self._build_chains()
            logger.info("🎉 Krishi Bondo Engine ready!")

        except Exception as e:
            logger.error(f"❌ Initialization failed: {e}")
            raise

    def _populate_knowledge_base_if_empty(self):
        try:
            existing_count = self.vector_store._collection.count()
        except Exception:
            existing_count = 0

        if existing_count == 0:
            logger.info("📚 Knowledge base empty — populating with crop data...")
            docs_data = get_all_documents()

            documents = [
                Document(page_content=item["text"], metadata=item["metadata"])
                for item in docs_data
            ]

            self.vector_store.add_documents(documents)
            logger.info(f"✅ Loaded {len(documents)} document chunks into ChromaDB")
        else:
            logger.info(f"📚 Knowledge base already populated ({existing_count} chunks)")

    def _build_chains(self):
        output_parser = StrOutputParser()

        self.rag_chain_en = ChatPromptTemplate.from_template(RAG_PROMPT_EN) | self.llm | output_parser
        self.rag_chain_bn = ChatPromptTemplate.from_template(RAG_PROMPT_BN) | self.llm | output_parser
        self.fallback_chain_en = ChatPromptTemplate.from_template(FALLBACK_PROMPT_EN) | self.llm | output_parser
        self.fallback_chain_bn = ChatPromptTemplate.from_template(FALLBACK_PROMPT_BN) | self.llm | output_parser

    def _retrieve_context(self, question: str):
        results = self.vector_store.similarity_search_with_score(question, k=TOP_K_RESULTS)

        if not results:
            return None, 0.0, []

        best_distance = results[0][1]
        best_similarity = max(0.0, 1.0 - (best_distance / 2.0))

        logger.info(f"🔍 Best match similarity: {best_similarity:.3f}")

        if best_similarity < SIMILARITY_THRESHOLD:
            return None, best_similarity, []

        context_parts = [doc.page_content for doc, _ in results]
        context_text = "\n\n---\n\n".join(context_parts)
        sources = [doc.metadata for doc, _ in results]

        return context_text, best_similarity, sources

    # ============================================================
    # TEXT Q&A (Hybrid RAG)
    # ============================================================

    def answer(self, question: str, language: str = "en") -> dict:
        if not question or not question.strip():
            msg = (
                "অনুগ্রহ করে কৃষি বা চাষাবাদ সম্পর্কিত একটি প্রশ্ন করুন।"
                if language == "bn"
                else "Please ask a question about agriculture or farming."
            )
            return {"answer": msg, "source": "system", "confidence": 0.0, "sources": []}

        question = question.strip()
        logger.info(f"❓ Q ({language}): {question[:80]}...")

        try:
            context, similarity, sources = self._retrieve_context(question)

            if context:
                logger.info(f"✅ KB mode ({language})")
                chain = self.rag_chain_bn if language == "bn" else self.rag_chain_en
                answer = chain.invoke({"context": context, "question": question})
                return {
                    "answer": answer,
                    "source": "knowledge_base",
                    "confidence": round(similarity, 3),
                    "sources": sources,
                }
            else:
                logger.info(f"🌐 Fallback mode ({language})")
                chain = self.fallback_chain_bn if language == "bn" else self.fallback_chain_en
                answer = chain.invoke({"question": question})
                return {
                    "answer": answer,
                    "source": "general_ai",
                    "confidence": round(similarity, 3),
                    "sources": [],
                }

        except Exception as e:
            logger.error(f"❌ Answer generation failed: {e}")
            err = (
                "প্রশ্নটি প্রক্রিয়া করতে গিয়ে একটি সমস্যা হয়েছে। আবার চেষ্টা করুন।"
                if language == "bn"
                else "I encountered an error. Please try again."
            )
            return {"answer": err, "source": "error", "confidence": 0.0, "sources": [], "error": str(e)}

    # ============================================================
    # VOICE — Speech-to-Text (Whisper)
    # ============================================================

    def transcribe_audio(self, audio_path: str) -> str:
        """Transcribe audio file using Groq Whisper. Auto-detects language."""
        logger.info(f"🎙️  Transcribing audio: {audio_path}")
        try:
            with open(audio_path, "rb") as audio_file:
                transcription = self.groq_client.audio.transcriptions.create(
                    file=(Path(audio_path).name, audio_file.read()),
                    model=GROQ_WHISPER_MODEL,
                    response_format="text",
                )
            text = transcription.strip() if isinstance(transcription, str) else str(transcription).strip()
            logger.info(f"✅ Transcribed: {text[:80]}...")
            return text
        except Exception as e:
            logger.error(f"❌ Transcription error: {e}")
            raise

    # ============================================================
    # VISION — Image Analysis
    # ============================================================

    def analyze_image(self, image_path: str, question: str = "", language: str = "en") -> dict:
        """Analyze a crop/pest image using Groq vision model."""
        logger.info(f"🖼️  Analyzing image: {image_path} (lang={language})")
        try:
            # Encode image to base64
            with open(image_path, "rb") as img_file:
                base64_image = base64.b64encode(img_file.read()).decode("utf-8")

            # Detect mime type from extension
            ext = Path(image_path).suffix.lower().lstrip(".")
            mime_map = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp", "gif": "gif"}
            mime = mime_map.get(ext, "jpeg")

            # Select prompt
            prompt_template = VISION_PROMPT_BN if language == "bn" else VISION_PROMPT_EN
            full_prompt = prompt_template.format(
                question=question or ("ছবিটি বিশ্লেষণ করো" if language == "bn" else "Analyze this image")
            )

            # Call vision model
            response = self.groq_client.chat.completions.create(
                model=GROQ_VISION_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": full_prompt},
                            {
                                "type": "image_url",
                                "image_url": {"url": f"data:image/{mime};base64,{base64_image}"},
                            },
                        ],
                    }
                ],
                temperature=0.4,
                max_tokens=1500,
            )

            answer = response.choices[0].message.content
            logger.info("✅ Image analysis complete")

            return {
                "answer": answer,
                "source": "vision_ai",
                "confidence": 1.0,
                "sources": [],
            }

        except Exception as e:
            logger.error(f"❌ Image analysis error: {e}")
            err = (
                "ছবি বিশ্লেষণে সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।"
                if language == "bn"
                else "Image analysis failed. Please try again."
            )
            return {"answer": err, "source": "error", "confidence": 0.0, "sources": [], "error": str(e)}

    # ============================================================
    # STATS
    # ============================================================

    def get_stats(self) -> dict:
        try:
            doc_count = self.vector_store._collection.count()
        except Exception:
            doc_count = 0

        return {
            "status": "ready",
            "model": GROQ_MODEL,
            "embedding_model": EMBEDDING_MODEL,
            "knowledge_base_chunks": doc_count,
            "supported_crops": get_supported_crops(),
            "similarity_threshold": SIMILARITY_THRESHOLD,
        }


# ============================================================
# SINGLETON
# ============================================================

_engine_instance: Optional[KrishiBondoEngine] = None


def get_engine() -> KrishiBondoEngine:
    global _engine_instance
    if _engine_instance is None:
        _engine_instance = KrishiBondoEngine()
    return _engine_instance


# ============================================================
# QUICK TEST
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🌾 KRISHI BONDO — ENGINE TEST (RAG + Voice + Vision)")
    print("=" * 70 + "\n")

    engine = get_engine()
    stats = engine.get_stats()
    print(f"\n📊 STATS: {stats}\n")

    print("-" * 70)
    print("TEST: KB Question - English")
    print("-" * 70)
    r = engine.answer("How do I control brown planthopper in rice?", language="en")
    print(f"Source: {r['source']} | Confidence: {r['confidence']}")
    print(f"Answer: {r['answer'][:300]}...\n")

    print("-" * 70)
    print("TEST: KB Question - Bangla (forced)")
    print("-" * 70)
    r = engine.answer("How do I control brown planthopper in rice?", language="bn")
    print(f"Source: {r['source']} | Confidence: {r['confidence']}")
    print(f"Answer: {r['answer'][:300]}...\n")

    print("=" * 70)
    print("✅ Engine tests complete! Voice & Vision require API endpoints.")
    print("=" * 70 + "\n")