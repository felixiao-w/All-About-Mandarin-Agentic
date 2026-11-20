"""Logika utama Mandarin Sentence & Translator Agent."""

from backend.core.llm_client import generate_structured_response
from backend.core.schemas import AgentRequest, AgentResponse

from .prompts import SYSTEM_PROMPT
from .tools import format_sentences_context, search_sentences

AGENT_NAME = "sentence_translator"


def run(request: AgentRequest) -> AgentResponse:
    """Menjalankan Mandarin Sentence & Translator Agent dengan konteks korpus kalimat."""
    records = search_sentences(query=request.user_input, filters=request.filters, limit=5)
    dataset_context = format_sentences_context(records)

    user_prompt = (
        f"Permintaan penerjemahan / kalimat pengguna:\n{request.user_input}\n\n"
        f"Filter tambahan:\n{request.filters or {}}\n\n"
        f"Referensi dataset kalimat:\n{dataset_context}\n\n"
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
