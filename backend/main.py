"""Entry point FastAPI untuk Mandarin Ecosystem AI Hub."""

from typing import Callable

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.agents.culinary_menu import run as run_culinary_menu
from backend.agents.drama_recommender import run as run_drama_recommender
from backend.agents.hanzi_stroke import run as run_hanzi_stroke
from backend.agents.hsk_quiz import run as run_hsk_quiz
from backend.agents.sentence_translator import run as run_sentence_translator
from backend.agents.shopping_assistant import run as run_shopping_assistant
from backend.core.llm_client import MissingAPIKeyError
from backend.core.schemas import AgentRequest, AgentResponse

app = FastAPI(
    title="Mandarin Ecosystem AI Hub",
    description="Backend API modular dengan 6 AI Agent independen berbasis Pandas & Gemini Structured Output.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _execute_agent(agent_fn: Callable[[AgentRequest], AgentResponse], request: AgentRequest) -> AgentResponse:
    """Menjalankan fungsi agent dengan penanganan error terpusat."""
    try:
        return agent_fn(request)
    except MissingAPIKeyError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Terjadi kesalahan saat memproses agent: {exc}") from exc


@app.get("/health", tags=["System"])
def health_check() -> dict:
    """Endpoint pengecekan status layanan API."""
    return {
        "status": "ok",
        "service": "Mandarin Ecosystem AI Hub",
        "agents": [
            "hsk-quiz",
            "sentence-translator",
            "hanzi-stroke",
            "drama-recommender",
            "culinary-menu",
            "shopping-assistant",
        ],
    }


@app.post("/api/agents/hsk-quiz", response_model=AgentResponse, tags=["Agents"])
def hsk_quiz_endpoint(request: AgentRequest) -> AgentResponse:
    """HSK Flashcard & Quiz Agent."""
    return _execute_agent(run_hsk_quiz, request)


@app.post("/api/agents/sentence-translator", response_model=AgentResponse, tags=["Agents"])
def sentence_translator_endpoint(request: AgentRequest) -> AgentResponse:
    """Mandarin Sentence & Translator Agent."""
    return _execute_agent(run_sentence_translator, request)


@app.post("/api/agents/hanzi-stroke", response_model=AgentResponse, tags=["Agents"])
def hanzi_stroke_endpoint(request: AgentRequest) -> AgentResponse:
    """Hanzi Stroke & Character Agent."""
    return _execute_agent(run_hanzi_stroke, request)


@app.post("/api/agents/drama-recommender", response_model=AgentResponse, tags=["Agents"])
def drama_recommender_endpoint(request: AgentRequest) -> AgentResponse:
    """Chinese Drama & Movie Recommender Agent."""
    return _execute_agent(run_drama_recommender, request)


@app.post("/api/agents/culinary-menu", response_model=AgentResponse, tags=["Agents"])
def culinary_menu_endpoint(request: AgentRequest) -> AgentResponse:
    """Chinese Culinary & Menu Agent."""
    return _execute_agent(run_culinary_menu, request)


@app.post("/api/agents/shopping-assistant", response_model=AgentResponse, tags=["Agents"])
def shopping_assistant_endpoint(request: AgentRequest) -> AgentResponse:
    """Mandarin Shopping Assistant Agent."""
    return _execute_agent(run_shopping_assistant, request)
