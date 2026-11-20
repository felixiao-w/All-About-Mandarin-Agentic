"""Wrapper Gemini API menggunakan google-genai SDK dengan Structured Output."""

from typing import Optional, Type, TypeVar

from google import genai
from google.genai import types
from pydantic import BaseModel

from backend.core.config import GEMINI_API_KEY, GEMINI_MODEL

SchemaT = TypeVar("SchemaT", bound=BaseModel)

_PLACEHOLDER_KEYS = {"", "your_api_key_here", "YOUR_API_KEY_HERE"}


class MissingAPIKeyError(ValueError):
    """Muncul ketika GEMINI_API_KEY belum dikonfigurasi di file .env."""


def _get_genai_client(api_key: Optional[str] = None) -> genai.Client:
    """Membuat instance google.genai.Client setelah memvalidasi API key."""
    resolved_key = (api_key if api_key is not None else GEMINI_API_KEY).strip()
    if resolved_key in _PLACEHOLDER_KEYS:
        raise MissingAPIKeyError(
            "GEMINI_API_KEY belum diisi atau masih menggunakan nilai placeholder. "
            "Salin .env.example menjadi .env lalu masukkan API key Gemini Anda."
        )
    return genai.Client(api_key=resolved_key)


def generate_structured_response(
    system_prompt: str,
    user_prompt: str,
    response_schema: Type[SchemaT],
    model: Optional[str] = None,
    temperature: float = 0.3,
) -> SchemaT:
    """Memanggil Gemini API dan mengembalikan output tervalidasi sesuai Pydantic schema.

    Args:
        system_prompt: Instruksi peran sistem untuk agent.
        user_prompt: Prompt pengguna yang sudah diperkaya konteks dataset.
        response_schema: Kelas Pydantic BaseModel target untuk Structured Output.
        model: Nama model Gemini (default mengikuti GEMINI_MODEL di .env).
        temperature: Tingkat kreativitas model.

    Returns:
        Instance dari ``response_schema`` hasil parsing JSON Gemini.
    """
    client = _get_genai_client()
    target_model = model or GEMINI_MODEL

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        response_mime_type="application/json",
        response_schema=response_schema,
        temperature=temperature,
    )

    response = client.models.generate_content(
        model=target_model,
        contents=user_prompt,
        config=config,
    )

    if response.parsed is not None and isinstance(response.parsed, response_schema):
        return response.parsed

    if not response.text:
        raise RuntimeError("Gemini API mengembalikan respons kosong.")

    return response_schema.model_validate_json(response.text)
