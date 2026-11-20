"""Helper Pandas untuk membaca dan mencari dataset kosakata HSK."""

import json
from typing import Any, Dict, List, Optional

import pandas as pd

from backend.core.config import get_data_path

DATASET_FILENAME = "01_hsk_vocabulary.csv"


def load_hsk_dataset() -> pd.DataFrame:
    """Membaca dataset 01_hsk_vocabulary.csv secara aman menggunakan Pandas."""
    csv_path = get_data_path(DATASET_FILENAME)
    try:
        return pd.read_csv(csv_path)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return pd.DataFrame()


def search_hsk_vocabulary(
    query: str,
    filters: Optional[Dict[str, Any]] = None,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    """Mencari kosakata HSK yang relevan dari dataset berdasarkan query dan filter opsional."""
    df = load_hsk_dataset()
    if df.empty:
        return []

    filtered_df = df.copy()

    if filters:
        for key, value in filters.items():
            if value is not None and key in filtered_df.columns:
                filtered_df = filtered_df[
                    filtered_df[key].astype(str).str.lower() == str(value).strip().lower()
                ]

    keyword = query.strip()
    if keyword and not filtered_df.empty:
        mask = filtered_df.astype(str).apply(
            lambda col: col.str.contains(keyword, case=False, na=False, regex=False)
        ).any(axis=1)
        matched_df = filtered_df[mask]
        if not matched_df.empty:
            filtered_df = matched_df

    return filtered_df.head(limit).fillna("").to_dict(orient="records")


def format_hsk_context(records: List[Dict[str, Any]]) -> str:
    """Memformat hasil pencarian dataset menjadi konteks teks untuk prompt LLM."""
    if not records:
        return (
            f"Dataset `{DATASET_FILENAME}` belum tersedia di folder data/ atau tidak ada entri "
            "yang cocok. Gunakan pengetahuan kosakata HSK standar."
        )
    return json.dumps(records, ensure_ascii=False, indent=2)
