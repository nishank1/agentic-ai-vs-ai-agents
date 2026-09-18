from __future__ import annotations

from datetime import datetime, timezone

from langchain_core.tools import tool


@tool
def get_current_utc_time() -> str:
    """Return the current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@tool
def count_words(text: str) -> int:
    """Count how many words appear in the provided text."""
    return len(text.split())
