from __future__ import annotations

from typing import TypedDict


class MultiAgentState(TypedDict, total=False):
    topic: str
    research_notes: str
    draft: str
    review: str
    final_answer: str
