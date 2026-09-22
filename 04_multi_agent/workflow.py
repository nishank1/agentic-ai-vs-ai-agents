from __future__ import annotations

import sys
from pathlib import Path

from langgraph.graph import END, START, StateGraph

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_ai_lab.core import configure_logging  # noqa: E402
from agents import researcher, reviewer, writer
from state import MultiAgentState


def build_workflow():
    graph = StateGraph(MultiAgentState)
    graph.add_node("researcher", researcher)
    graph.add_node("writer", writer)
    graph.add_node("reviewer", reviewer)
    graph.add_edge(START, "researcher")
    graph.add_edge("researcher", "writer")
    graph.add_edge("writer", "reviewer")
    graph.add_edge("reviewer", END)
    return graph.compile()



def main() -> None:
    configure_logging()
    app = build_workflow()
    result = app.invoke({"topic": "how an LLM becomes part of a multi-agent system"})
    print(result["final_answer"])


if __name__ == "__main__":
    main()
