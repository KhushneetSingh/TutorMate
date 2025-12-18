import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# ---- API KEY ----
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError(
        "GOOGLE_API_KEY not set. Please export it or add it to .env"
    )

# ---- Client ----
client = genai.Client(api_key=GOOGLE_API_KEY)

MODEL_NAME = "gemini-2.5-flash-lite"


def generate_study_plan(prompt: str) -> str:
    """
    Generate a study plan using Google Gemini (official SDK).
    """
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text # type: ignore