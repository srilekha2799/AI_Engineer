
import os
from google import genai

# Check whether the Gemini API key exists
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

# Create the Gemini client
client = genai.Client(api_key=api_key)

try:
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input="Give me three uses of LLMs."
    )

    print("AI Response:")
    print(response.output_text)

except Exception as error:
    print(f"Gemini API error: {error}")
