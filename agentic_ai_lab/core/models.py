from __future__ import annotations

from functools import lru_cache

from langchain_openai import ChatOpenAI

from .config import RuntimeConfig, load_runtime_config


def build_chat_model(
    config: RuntimeConfig | None = None, **kwargs: object
) -> ChatOpenAI:
    runtime_config = config or load_runtime_config()

    return ChatOpenAI(
        model=runtime_config.openai_model,
        api_key=runtime_config.openai_api_key,
        base_url=runtime_config.openai_base_url,
        **kwargs,
    )


@lru_cache(maxsize=1)
def get_default_chat_model() -> ChatOpenAI:
    return build_chat_model()
