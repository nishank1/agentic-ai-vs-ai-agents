from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from tools import count_words, get_current_utc_time


def build_llm() -> ChatOpenAI:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        raise SystemExit(
            "Please set OPENAI_API_KEY in your .env file before running this example."
        )

    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        api_key=api_key,
        base_url=os.getenv("OPENAI_BASE_URL") or None,
    )


def main() -> None:
    agent = create_react_agent(
        model=build_llm(),
        tools=[get_current_utc_time, count_words],
        prompt=(
            "You are a beginner-friendly AI agent. "
            "Use tools whenever they help you answer accurately."
        ),
    )

    user_message = (
        "Tell me the current UTC time and count the words in this sentence: "
        "agentic workflows make systems more reliable"
    )

    result = agent.invoke({"messages": [("user", user_message)]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
