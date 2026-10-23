
import os
from google import genai
from google.genai import types

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("Please set GEMINI_API_KEY first.")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a friendly AI tutor for CSE students. "
            "Explain concepts in simple English and give one example."
        )
    ),
    contents="Explain the difference between AI and machine learning."
)

print("Assistant response:")
print(response.text)
