from __future__ import annotations

from typing import TypedDict


class WorkflowState(TypedDict, total=False):
    topic: str
    outline: str
    draft: str
    final_answer: str
