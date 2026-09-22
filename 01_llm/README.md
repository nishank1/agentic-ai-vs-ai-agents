# 01 - LLM

This is the simplest possible starting point and the baseline for every later comparison.

## Architecture

```text
User → Prompt → LLM → Response
```

## What this example teaches

- How shared runtime configuration is loaded
- How to initialize a provider-backed chat model
- How to send one prompt
- How to treat this pattern as a baseline for later evaluation

## Entry point

- `simple_llm.py`

## Configuration

- Requires `OPENAI_API_KEY`
- Supports `OPENAI_MODEL` and `OPENAI_BASE_URL`

## Run

```bash
python 01_llm/simple_llm.py
```

## Example input/output

- Input: a single instructional prompt
- Output: a direct model answer with no tools, memory, or workflow state

## Failure considerations

- Missing credentials should fail immediately.
- This pattern is simple, but offers almost no control or recovery once the prompt is sent.
