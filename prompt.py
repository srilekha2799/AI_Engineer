
import os
from google import genai

# Check whether the Gemini API key exists
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError(
        "Please set your GEMINI_API_KEY first."
    )

# Create the Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

text = """
Machine learning allows computers to learn patterns from data.
It is used in recommendation systems, fraud detection,
image recognition, and many other applications.
"""

prompt = f"""
You are a friendly AI tutor teaching a beginner.

Task: Explain the following text in simple English.

Requirements:
- Use no more than 100 words.
- Include three key points.
- Give one real-world example.
- Preserve the original meaning.
- Do not add unsupported facts.

Text:
{text}
"""

try:
    # Send the prompt to Gemini
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    print("AI Response:")
    print(response.text)

except Exception as error:
    print("Something went wrong:", error)
