import os
import json
from google import genai

# 1. Check the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

# 2. Create the Gemini client
client = genai.Client(api_key=api_key)

# 3. Define the prompt
prompt = """
Explain machine learning for a beginner.

Return a JSON object with these fields:
- topic: a string
- summary: a short string
- key_points: an array of exactly three strings
- example: a string
"""

# 4. Request structured JSON output
response = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "summary": {"type": "string"},
                "key_points": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 3,
                    "maxItems": 3
                },
                "example": {"type": "string"}
            },
            "required": [
                "topic",
                "summary",
                "key_points",
                "example"
            ]
        }
    }
)

# 5. Get the generated text
output = response.output_text

print("Raw model output:")
print(output)

# 6. Parse and display the JSON
try:
    data = json.loads(output)

    print("\nTopic:", data["topic"])
    print("\nSummary:", data["summary"])

    print("\nKey points:")
    for point in data["key_points"]:
        print("-", point)

    print("\nExample:", data["example"])

except (json.JSONDecodeError, KeyError, TypeError) as error:
    print("The response was not in the expected format:", error)
