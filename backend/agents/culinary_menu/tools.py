"""Helper Pandas untuk membaca dan mencari dataset kuliner & menu Tiongkok."""

import json
from typing import Any, Dict, List, Optional

import pandas as pd

from backend.core.config import get_data_path

DATASET_FILENAME = "05_chinese_culinary_menu.csv"


def load_culinary_dataset() -> pd.DataFrame:
    """Membaca dataset 05_chinese_culinary_menu.csv secara aman menggunakan Pandas."""
    csv_path = get_data_path(DATASET_FILENAME)
    try:
        return pd.read_csv(csv_path)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return pd.DataFrame()


def search_culinary_menu(
    query: str,
    filters: Optional[Dict[str, Any]] = None,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    """Mencari hidangan kuliner Tiongkok dari dataset sesuai query dan filter opsional."""
    df = load_culinary_dataset()
    if df.empty:
        return []

    filtered_df = df.copy()

    if filters:
        for key, value in filters.items():
            if value is not None and key in filtered_df.columns:
                filtered_df = filtered_df[
                    filtered_df[key].astype(str).str.contains(str(value).strip(), case=False, na=False, regex=False)
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


def format_culinary_context(records: List[Dict[str, Any]]) -> str:
    """Memformat data menu kuliner menjadi teks konteks untuk prompt LLM."""
    if not records:
        return (
            f"Dataset `{DATASET_FILENAME}` belum tersedia di folder data/ atau tidak ada menu "
            "yang cocok. Berikan rekomendasi dan penjelasan kuliner Tiongkok secara umum."
        )
    return json.dumps(records, ensure_ascii=False, indent=2)
