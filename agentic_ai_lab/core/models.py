from __future__ import annotations

from langchain_openai import ChatOpenAI

from .config import RuntimeConfig, load_runtime_config


def build_chat_model(
    config: RuntimeConfig | None = None, **kwargs: object
) -> ChatOpenAI:
    runtime_config = config or load_runtime_config()
    if (
        not runtime_config.openai_api_key
        or runtime_config.openai_api_key == "your_api_key_here"
    ):
        raise SystemExit(
            "Please set OPENAI_API_KEY in your .env file before running this example."
        )

    return ChatOpenAI(
        model=runtime_config.openai_model,
        api_key=runtime_config.openai_api_key,
        base_url=runtime_config.openai_base_url,
        **kwargs,
    )


def get_default_chat_model() -> ChatOpenAI:
    return build_chat_model()
