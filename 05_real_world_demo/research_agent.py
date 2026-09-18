from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from typing import TypedDict

from prompts import EDITOR_PROMPT, PLANNER_PROMPT, RESEARCH_PROMPT


class DemoState(TypedDict, total=False):
    topic: str
    plan: str
    research: str
    brief: str



def build_llm() -> ChatOpenAI:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        raise SystemExit(
            "Please set OPENAI_API_KEY in your .env file before running this example."
        )

    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        api_key=api_key,
        base_url=os.getenv("OPENAI_BASE_URL") or None,
    )

_llm: ChatOpenAI | None = None


def get_llm() -> ChatOpenAI:
    global _llm
    if _llm is None:
        _llm = build_llm()
    return _llm


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
        f"{EDITOR_PROMPT}\n\nTopic: {state['topic']}\n\nPlan:\n{state['plan']}\n\nResearch:\n{state['research']}"
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
