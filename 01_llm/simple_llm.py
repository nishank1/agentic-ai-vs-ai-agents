from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_ai_lab.core import (  # noqa: E402
    configure_logging,
    get_default_chat_model,
    get_logger,
    log_event,
)

LOGGER = get_logger(__name__)


def main() -> None:
    configure_logging()
    llm = get_default_chat_model()
    prompt = "Explain in 3 short bullet points what an LLM is."
    log_event(LOGGER, "llm_example_started", example="01_llm")
    response = llm.invoke(prompt)

    print("Prompt:")
    print(prompt)
    print("\nResponse:")
    print(response.content)


if __name__ == "__main__":
    main()
