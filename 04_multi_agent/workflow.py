from __future__ import annotations

from langgraph.graph import END, START, StateGraph

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
    app = build_workflow()
    result = app.invoke({"topic": "how an LLM becomes part of a multi-agent system"})
    print(result["final_answer"])


if __name__ == "__main__":
    main()
