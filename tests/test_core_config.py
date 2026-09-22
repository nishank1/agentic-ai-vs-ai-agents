from __future__ import annotations

import pytest

from agentic_ai_lab.core import build_chat_model, load_runtime_config


def test_load_runtime_config_reads_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "demo-model")
    monkeypatch.setenv("OPENAI_BASE_URL", "https://example.com/v1")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    config = load_runtime_config()

    assert config.openai_api_key == "test-key"
    assert config.openai_model == "demo-model"
    assert config.openai_base_url == "https://example.com/v1"
    assert config.log_level == "DEBUG"


def test_load_runtime_config_allows_missing_key_for_non_runtime_checks(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    config = load_runtime_config(require_api_key=False)

    assert config.openai_api_key is None


def test_build_chat_model_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(SystemExit):
        build_chat_model()
