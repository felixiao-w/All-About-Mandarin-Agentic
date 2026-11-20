"""Logika utama Hanzi Stroke & Character Agent."""

from backend.core.llm_client import generate_structured_response
from backend.core.schemas import AgentRequest, AgentResponse

from .prompts import SYSTEM_PROMPT
from .tools import format_hanzi_context, search_hanzi_characters

AGENT_NAME = "hanzi_stroke"


def run(request: AgentRequest) -> AgentResponse:
    """Menjalankan Hanzi Stroke & Character Agent dengan konteks dataset radikal & goresan."""
    records = search_hanzi_characters(query=request.user_input, filters=request.filters, limit=5)
    dataset_context = format_hanzi_context(records)

    user_prompt = (
        f"Permintaan analisis karakter Hanzi:\n{request.user_input}\n\n"
        f"Filter tambahan:\n{request.filters or {}}\n\n"
        f"Referensi dataset radikal & goresan:\n{dataset_context}\n\n"
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
