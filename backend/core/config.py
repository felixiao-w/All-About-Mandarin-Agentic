"""Konfigurasi terpusat aplikasi dari environment variables (.env)."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip() or "gemini-2.5-flash"

_raw_data_dir = os.getenv("DATA_DIR", "data").strip() or "data"
_data_dir_path = Path(_raw_data_dir)
DATA_DIR: Path = _data_dir_path if _data_dir_path.is_absolute() else (BASE_DIR / _data_dir_path)


def get_data_path(filename: str) -> Path:
    """Mengembalikan path absolut ke file dataset di dalam DATA_DIR."""
    return DATA_DIR / filename
