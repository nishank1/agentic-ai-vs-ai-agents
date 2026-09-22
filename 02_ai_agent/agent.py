from __future__ import annotations

import sys
from pathlib import Path

from langchain.agents import create_agent

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agentic_ai_lab.core import (  # noqa: E402
    configure_logging,
    extract_text_content,
    get_default_chat_model,
)
from tools import count_words, get_current_utc_time


def main() -> None:
    configure_logging()
    agent = create_agent(
        model=get_default_chat_model(),
        tools=[get_current_utc_time, count_words],
        system_prompt=(
            "You are a beginner-friendly AI agent. "
            "Use tools whenever they help you answer accurately."
        ),
    )

    user_message = (
        "Tell me the current UTC time and count the words in this sentence: "
        "agentic workflows make systems more reliable"
    )

    result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    print(extract_text_content(result["messages"][-1]))


if __name__ == "__main__":
    main()
