# Contributing

Thanks for contributing to the Agentic AI Engineering Lab.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
make install-dev
```

## Common commands

```bash
make lint
make format
make test
```

## Contribution guidelines

- Keep examples small, explicit, and runnable locally.
- Prefer incremental additions over large rewrites.
- Add tests for shared utilities and important workflow behavior.
- Document architecture, trade-offs, and failure considerations alongside code changes.
- Do not commit secrets; use `.env.example` for configuration shape only.

## Pull requests

- Explain the engineering problem being solved.
- Summarize architectural trade-offs.
- Note any limitations or follow-up work.
