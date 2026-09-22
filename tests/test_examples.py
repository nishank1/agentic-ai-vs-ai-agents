from __future__ import annotations

from tests.helpers import load_example_module


def test_agent_tools_behave_as_expected() -> None:
    tools_module = load_example_module("agent_tools", "02_ai_agent/tools.py")

    assert tools_module.count_words.invoke({"text": "agentic systems need controls"}) == 4
    assert tools_module.get_current_utc_time.invoke({endswith("00:00")}) is False


def test_workflow_graphs_compile() -> None:
    workflow_module = load_example_module("workflow_03", "03_agentic_workflow/workflow.py")
    multi_agent_module = load_example_module("workflow_04", "04_multi_agent/workflow.py")
    demo_module = load_example_module("workflow_05", "05_real_world_demo/research_agent.py")

    workflow_nodes = workflow_module.build_workflow().get_graph().nodes
    multi_agent_nodes = multi_agent_module.build_workflow().get_graph().nodes
    demo_nodes = demo_module.build_workflow().get_graph().nodes

    assert {"__start__", "create_outline", "write_draft", "review_draft"}.issubset(
        workflow_nodes
    )
    assert {"__start__", "researcher", "writer", "reviewer"}.issubset(multi_agent_nodes)
    assert {"__start__", "planner", "researcher", "editor"}.issubset(demo_nodes)
