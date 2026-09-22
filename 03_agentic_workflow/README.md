# 03 - Agentic Workflow

This example introduces structure.

## Architecture

An agentic workflow is not just "let the model decide everything." It is a designed process with steps.

Here the flow is:

1. Create an outline
2. Draft an explanation
3. Review and improve the draft

## Why it matters

Workflows are useful when you want:

- repeatability
- easier debugging
- shared state between steps
- more control than a free-form agent

## Entry point

- `workflow.py`

## Configuration

- Requires `OPENAI_API_KEY`
- Uses LangGraph state transitions

## Run

```bash
python 03_agentic_workflow/workflow.py
```

## Example input/output

- Input: one topic string
- Output: outline, draft, and reviewed explanation stored across workflow state

## Failure considerations

- A fixed workflow is easier to inspect than an unconstrained agent loop.
- Each node can still fail independently, so later phases will add retries, metrics, and observability.
