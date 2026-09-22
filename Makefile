.PHONY: install install-dev lint format format-check test

install:
	pip install -r requirements.txt

install-dev:
	pip install -e ".[dev]"

lint:
	ruff check .

format:
	ruff format .

format-check:
	ruff format --check .

test:
	pytest -m "not integration and not llm"

