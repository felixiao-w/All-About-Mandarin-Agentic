"""Logika utama Mandarin Shopping Assistant Agent."""

from backend.core.llm_client import generate_structured_response
from backend.core.schemas import AgentRequest, AgentResponse

from .prompts import SYSTEM_PROMPT
from .tools import format_products_context, search_ecommerce_products

AGENT_NAME = "shopping_assistant"


def run(request: AgentRequest) -> AgentResponse:
    """Menjalankan Mandarin Shopping Assistant Agent dengan konteks dataset produk e-commerce."""
    records = search_ecommerce_products(query=request.user_input, filters=request.filters, limit=5)
    dataset_context = format_products_context(records)

    user_prompt = (
        f"Permintaan belanja pengguna:\n{request.user_input}\n\n"
        f"Filter tambahan:\n{request.filters or {}}\n\n"
        f"Konteks dataset produk e-commerce:\n{dataset_context}\n\n"
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
