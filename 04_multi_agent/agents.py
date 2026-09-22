from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_ai_lab.core import get_default_chat_model  # noqa: E402
from state import MultiAgentState


def researcher(state: MultiAgentState) -> MultiAgentState:
    response = get_default_chat_model().invoke(
        "You are a researcher. Create concise notes that explain the topic.\n\n"
        f"Topic: {state['topic']}"
    )
    return {"research_notes": response.content}



def writer(state: MultiAgentState) -> MultiAgentState:
    response = get_default_chat_model().invoke(
        "You are a writer. Use the research notes to write a clear explanation.\n\n"
        f"Topic: {state['topic']}\n\nResearch notes:\n{state['research_notes']}"
    )
    return {"draft": response.content}



def reviewer(state: MultiAgentState) -> MultiAgentState:
    response = get_default_chat_model().invoke(
        "You are a reviewer. Improve the draft for accuracy and beginner clarity.\n\n"
        f"Draft:\n{state['draft']}"
    )
    return {
        "review": response.content,
        "final_answer": response.content,
    }
