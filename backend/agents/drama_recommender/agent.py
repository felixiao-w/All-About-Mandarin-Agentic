"""Logika utama Chinese Drama & Movie Recommender Agent."""

from backend.core.llm_client import generate_structured_response
from backend.core.schemas import AgentRequest, AgentResponse

from .prompts import SYSTEM_PROMPT
from .tools import format_dramas_context, search_dramas_movies

AGENT_NAME = "drama_recommender"


def run(request: AgentRequest) -> AgentResponse:
    """Menjalankan Chinese Drama & Movie Recommender Agent."""
    records = search_dramas_movies(query=request.user_input, filters=request.filters, limit=5)
    dataset_context = format_dramas_context(records)

    user_prompt = (
        f"Permintaan rekomendasi drama/film:\n{request.user_input}\n\n"
        f"Filter tambahan:\n{request.filters or {}}\n\n"
        f"Konteks katalog dataset drama & film:\n{dataset_context}\n\n"
        f"Pastikan `agent_name` bernilai `{AGENT_NAME}`."
    )

    response = generate_structured_response(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
        response_schema=AgentResponse,
    )
    response.agent_name = AGENT_NAME
    if not response.recommended_items and records:
        response.recommended_items = records
    return response
