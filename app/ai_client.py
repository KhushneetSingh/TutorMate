import os
from openai import OpenAI

# Read API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY not set. Add it to .env or environment variables."
    )

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_study_plan(prompt: str) -> str:
    """
    Calls LLM to generate a study plan.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert study planner."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=600,
    )

    return response.choices[0].message.content