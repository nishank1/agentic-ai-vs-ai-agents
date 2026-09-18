# 02 - AI Agent

This example upgrades a plain LLM into an agent.

## Idea

An AI agent is usually an LLM plus:

- tools
- reasoning
- the ability to decide the next step

Instead of answering immediately, the model can use tools first and then respond.

## Flow

```text
User
  ↓
Agent (LLM + tools)
  ├─→ Tool: current time
  ├─→ Tool: word counter
  └─→ Final answer
```

## Files

- `tools.py` contains simple tools
- `agent.py` creates a ReAct-style agent with LangGraph

## Run

```bash
python 02_ai_agent/agent.py
```
