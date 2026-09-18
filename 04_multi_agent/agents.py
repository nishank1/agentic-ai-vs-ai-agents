from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from state import MultiAgentState


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


def researcher(state: MultiAgentState) -> MultiAgentState:
    response = get_llm().invoke(
        "You are a researcher. Create concise notes that explain the topic.\n\n"
        f"Topic: {state['topic']}"
    )
    return {"research_notes": response.content}



def writer(state: MultiAgentState) -> MultiAgentState:
    response = get_llm().invoke(
        "You are a writer. Use the research notes to write a clear explanation.\n\n"
        f"Topic: {state['topic']}\n\nResearch notes:\n{state['research_notes']}"
    )
    return {"draft": response.content}



def reviewer(state: MultiAgentState) -> MultiAgentState:
    response = get_llm().invoke(
        "You are a reviewer. Improve the draft for accuracy and beginner clarity.\n\n"
        f"Draft:\n{state['draft']}"
    )
    return {
        "review": response.content,
        "final_answer": response.content,
    }
