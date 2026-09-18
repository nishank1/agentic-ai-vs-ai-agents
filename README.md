# agentic-ai-vs-ai-agents

A beginner-friendly, hands-on repository that shows how to move from a single LLM call to a practical multi-agent application.

## What you will learn

This repository explains the difference and relationship between:

- **LLM** - a model that generates text from a prompt
- **AI Agent** - an LLM that can use tools and decide what to do next
- **Agentic Workflow** - a structured sequence of LLM-powered steps
- **Multi-Agent System** - multiple specialized agents collaborating on one task

## Learning progression

```text
LLM
 ↓
LLM + Tools
 ↓
AI Agent
 ↓
Agentic Workflow
 ↓
Multi-Agent System
 ↓
Real-World Agentic Application
```

## Tech stack

- Python 3.11+
- LangChain
- LangGraph
- OpenAI-compatible LLM API
- python-dotenv
- Optional LangSmith tracing support

## Project structure

```text
agentic-ai-vs-ai-agents/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── 01_llm/
├── 02_ai_agent/
├── 03_agentic_workflow/
├── 04_multi_agent/
├── 05_real_world_demo/
└── diagrams/
```

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env`.

Optional variables you can also define if you use a compatible provider:

- `OPENAI_MODEL` (default: `gpt-4o-mini`)
- `OPENAI_BASE_URL`

### 4. Run the examples

```bash
python 01_llm/simple_llm.py
python 02_ai_agent/agent.py
python 03_agentic_workflow/workflow.py
python 04_multi_agent/workflow.py
python 05_real_world_demo/research_agent.py
```

## Learning map

### 01 - LLM
Make one direct model call and print the answer.

### 02 - AI Agent
Add tools so the model can choose actions before answering.

### 03 - Agentic Workflow
Create a fixed graph with clearly defined steps and shared state.

### 04 - Multi-Agent
Split the work between specialist agents that collaborate.

### 05 - Real-World Demo
Use a small team of agents to turn a topic into a practical content brief.

## When to use what

- Use a **plain LLM** for direct question answering or drafting.
- Use an **AI agent** when the model needs tools and autonomy.
- Use an **agentic workflow** when the process should be predictable.
- Use a **multi-agent system** when specialization improves results.

## Diagrams

See the `diagrams/` folder for simple architecture summaries you can reuse in notes, demos, or a LinkedIn post.
