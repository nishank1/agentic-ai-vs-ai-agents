# 02 - AI Agent

This example upgrades a plain LLM into a tool-using agent.

## Architecture

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
- `agent.py` creates a modern LangChain agent using tools and a system prompt

## Entry point

- `agent.py`

## Configuration

- Requires `OPENAI_API_KEY`
- Supports `OPENAI_MODEL` and `OPENAI_BASE_URL`

## Run

```bash
python 02_ai_agent/agent.py
```

## Example input/output

- Input: ask for the current UTC time and a word count
- Output: the agent decides when to call tools and returns a final answer

## Failure considerations

- Tool-enabled autonomy increases flexibility and failure surface area.
- The example does not yet enforce tool allowlists, loop limits, or argument validation; later sections will add those controls.
