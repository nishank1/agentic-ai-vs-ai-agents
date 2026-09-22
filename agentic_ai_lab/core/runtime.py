from __future__ import annotations

from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class ExecutionLimits(BaseModel):
    max_iterations: int = 8
    max_tool_calls: int = 8
    timeout_seconds: float = 60.0
    max_tokens: int | None = None
    max_cost_usd: float | None = None


class RunContext(BaseModel):
    component: str
    model: str | None = None
    run_id: str = Field(default_factory=lambda: uuid4().hex)


def should_stop(*, iterations: int, tool_calls: int, limits: ExecutionLimits) -> bool:
    return iterations >= limits.max_iterations or tool_calls >= limits.max_tool_calls


def extract_text_content(message: Any) -> str:
    content = getattr(message, "content", message)

    if isinstance(content, dict) and "content" in content:
        content = content["content"]

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_chunks = [
            chunk.get("text", "")
            for chunk in content
            if isinstance(chunk, dict) and chunk.get("type") == "text"
        ]
        return "\n".join(chunk for chunk in text_chunks if chunk)

    return str(content)
