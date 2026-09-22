from __future__ import annotations

import os

from dotenv import load_dotenv
from pydantic import BaseModel


class RuntimeConfig(BaseModel):
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"
    openai_base_url: str | None = None
    langchain_api_key: str | None = None
    langchain_tracing_v2: bool = False
    langchain_project: str = "agentic-ai-vs-ai-agents"
    log_level: str = "INFO"


def load_runtime_config(*, require_api_key: bool = True) -> RuntimeConfig:
    load_dotenv()

    config = RuntimeConfig(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        openai_base_url=os.getenv("OPENAI_BASE_URL") or None,
        langchain_api_key=os.getenv("LANGCHAIN_API_KEY") or None,
        langchain_tracing_v2=os.getenv("LANGCHAIN_TRACING_V2", "false").lower()
        == "true",
        langchain_project=os.getenv("LANGCHAIN_PROJECT", "agentic-ai-vs-ai-agents"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )

    if require_api_key and (
        not config.openai_api_key or config.openai_api_key == "your_api_key_here"
    ):
        raise SystemExit(
            "Please set OPENAI_API_KEY in your .env file before running this example."
        )

    return config

