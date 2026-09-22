from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

from langgraph.graph import END, START, StateGraph

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_ai_lab.core import configure_logging, get_default_chat_model  # noqa: E402
from state import WorkflowState


@lru_cache(maxsize=1)
def get_llm():
    return get_default_chat_model()


def create_outline(state: WorkflowState) -> WorkflowState:
    response = get_llm().invoke(
        f"Create a simple 3-step outline that explains: {state['topic']}"
    )
    return {"outline": response.content}


def write_draft(state: WorkflowState) -> WorkflowState:
    response = get_llm().invoke(
        "Use this outline to write a beginner-friendly explanation.\n\n"
        f"Topic: {state['topic']}\n\nOutline:\n{state['outline']}"
    )
    return {"draft": response.content}


def review_draft(state: WorkflowState) -> WorkflowState:
    response = get_llm().invoke(
        "Improve the clarity of this explanation and keep it concise.\n\n"
        f"Draft:\n{state['draft']}"
    )
    return {"final_answer": response.content}


def build_workflow():
    graph = StateGraph(WorkflowState)
    graph.add_node("create_outline", create_outline)
    graph.add_node("write_draft", write_draft)
    graph.add_node("review_draft", review_draft)
    graph.add_edge(START, "create_outline")
    graph.add_edge("create_outline", "write_draft")
    graph.add_edge("write_draft", "review_draft")
    graph.add_edge("review_draft", END)
    return graph.compile()


def main() -> None:
    configure_logging()
    app = build_workflow()
    result = app.invoke(
        {"topic": "the difference between AI agents and agentic workflows"}
    )
    print(result["final_answer"])


if __name__ == "__main__":
    main()
