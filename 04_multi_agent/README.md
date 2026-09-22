# 04 - Multi-Agent System

This example shows how several specialized agents can collaborate.

## Architecture

```text
Topic → Researcher → Writer → Reviewer → Final answer
```

## Roles

- **Researcher** gathers the important ideas
- **Writer** turns those ideas into a clear explanation
- **Reviewer** checks whether the explanation is complete and clear

## Idea

A multi-agent system is useful when one general agent is not enough or when specialization improves results.

## Entry point

- `workflow.py`

## Configuration

- Requires `OPENAI_API_KEY`
- Uses shared state across specialized roles

## Run

```bash
python 04_multi_agent/workflow.py
```

## Example input/output

- Input: one topic string
- Output: research notes, draft, review, and final answer

## Failure considerations

- Specialization can improve clarity, but each extra role adds coordination cost.
- Multi-agent designs need observability and evaluation because a good final answer can hide inefficient or incorrect intermediate behavior.
