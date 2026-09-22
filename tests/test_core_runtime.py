from __future__ import annotations

from langchain_core.messages import AIMessage

from agentic_ai_lab.core import (
    ExecutionLimits,
    RunContext,
    extract_text_content,
    should_stop,
)


def test_should_stop_when_iteration_limit_reached() -> None:
    limits = ExecutionLimits(max_iterations=2, max_tool_calls=4)

    assert should_stop(iterations=2, tool_calls=1, limits=limits) is True
    assert should_stop(iterations=1, tool_calls=4, limits=limits) is True
    assert should_stop(iterations=1, tool_calls=3, limits=limits) is False


def test_extract_text_content_supports_string_and_blocks() -> None:
    assert extract_text_content("hello") == "hello"
    assert extract_text_content(AIMessage(content="message object")) == "message object"
    assert (
        extract_text_content(
            {
                "content": [
                    {"type": "text", "text": "first"},
                    {"type": "text", "text": "second"},
                ]
            }
        )
        == "first\nsecond"
    )


def test_run_context_generates_run_id() -> None:
    context = RunContext(component="unit-test", model="demo")

    assert context.component == "unit-test"
    assert context.model == "demo"
    assert context.run_id
