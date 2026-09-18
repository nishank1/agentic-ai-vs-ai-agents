from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


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
    llm = build_llm()
    prompt = "Explain in 3 short bullet points what an LLM is."
    response = llm.invoke(prompt)

    print("Prompt:")
    print(prompt)
    print("\nResponse:")
    print(response.content)


if __name__ == "__main__":
    main()
