"""Kontrak skema Pydantic standar untuk seluruh AI Agent."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """Payload standar yang dikirim client ke endpoint agent."""

    user_input: str = Field(..., min_length=1, description="Pertanyaan atau instruksi dari pengguna.")
    filters: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Filter opsional sesuai dataset masing-masing agent (mis. level HSK, genre, kategori).",
    )


class AgentResponse(BaseModel):
    """Output terstruktur standar yang dikembalikan oleh setiap agent."""

    agent_name: str = Field(..., description="Nama modul agent yang memproses permintaan.")
    mandarin_text: str = Field(..., description="Teks utama dalam aksara Mandarin (Hanzi).")
    pinyin: str = Field(..., description="Pelafalan Pinyin dengan nada.")
    translation: str = Field(..., description="Terjemahan dalam Bahasa Indonesia.")
    explanation: str = Field(..., description="Penjelasan kontekstual, tata bahasa, atau insight tambahan.")
    recommended_items: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Daftar item rekomendasi atau referensi yang relevan dari dataset.",
    )
