from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_ai_lab.core import configure_logging, get_default_chat_model  # noqa: E402
from prompts import EDITOR_PROMPT, PLANNER_PROMPT, RESEARCH_PROMPT


class DemoState(TypedDict, total=False):
    topic: str
    plan: str
    research: str
    brief: str


@lru_cache(maxsize=1)
def get_llm():
    return get_default_chat_model()


def planner(state: DemoState) -> DemoState:
    response = get_llm().invoke(f"{PLANNER_PROMPT}\n\nTopic: {state['topic']}")
    return {"plan": response.content}


def researcher(state: DemoState) -> DemoState:
    response = get_llm().invoke(
        f"{RESEARCH_PROMPT}\n\nTopic: {state['topic']}\n\nPlan:\n{state['plan']}"
    )
    return {"research": response.content}


def editor(state: DemoState) -> DemoState:
    response = get_llm().invoke(
        f"{EDITOR_PROMPT}\n\nTopic: {state['topic']}\n\nPlan:\n{state['plan']}"
        f"\n\nResearch:\n{state['research']}"
    )
    return {"brief": response.content}


def build_workflow():
    graph = StateGraph(DemoState)
    graph.add_node("planner", planner)
    graph.add_node("researcher", researcher)
    graph.add_node("editor", editor)
    graph.add_edge(START, "planner")
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "editor")
    graph.add_edge("editor", END)
    return graph.compile()


def main() -> None:
    configure_logging()
    app = build_workflow()
    result = app.invoke(
        {
            "topic": (
                "the difference and relationship between LLMs, AI agents, agentic "
                "workflows, and multi-agent systems"
            )
        }
    )
    print(result["brief"])


if __name__ == "__main__":
    main()
