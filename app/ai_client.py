import os
import json
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
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        return response.text  # type: ignore
    
    except Exception as e:
        # Log the error if needed
        print(f"Error generating study plan: {e}")
        
        # Return fallback study plan
        return json.dumps({
            "goal": "Prepare for Mobile Forensics exam",
            "duration_days": 14,
            "tasks": [
                {
                    "day": 1,
                    "topic": "Android Security Basics",
                    "objective": "Understand Android architecture and sandboxing",
                    "resources": ["Lecture notes", "Textbook"]
                }
            ]
        })