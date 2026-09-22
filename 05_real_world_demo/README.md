# 05 - Real-World Demo

This final example turns the ideas into a small practical application.

## Architecture

```text
Topic → Planner → Researcher → Editor → Content brief
```

## Scenario

You want to prepare a short content brief for a LinkedIn post comparing:

- LLMs
- AI agents
- agentic workflows
- multi-agent systems

## What happens

1. A planner creates a structure
2. A researcher expands the ideas
3. An editor turns it into a concise post brief

## Entry point

- `research_agent.py`

## Configuration

- Requires `OPENAI_API_KEY`
- Supports OpenAI-compatible endpoints

## Run

```bash
python 05_real_world_demo/research_agent.py
```

## Example input/output

- Input: a broad topic about LLMs, agents, workflows, and multi-agent systems
- Output: a compact content brief with structure and key takeaways

## Failure considerations

- This example is intentionally small and local.
- It demonstrates orchestration, but not yet evaluation, approval, guardrails, or external side effects.
