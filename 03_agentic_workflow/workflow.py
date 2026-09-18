from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph

from state import WorkflowState


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
    app = build_workflow()
    result = app.invoke({"topic": "the difference between AI agents and agentic workflows"})
    print(result["final_answer"])


if __name__ == "__main__":
    main()
