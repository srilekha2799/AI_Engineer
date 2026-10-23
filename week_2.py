
import os
from google import genai
from google.genai import types
from pydantic import BaseModel
from google.genai import errors
import time

# 1. Check the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

# 2. Define the expected response structure
class StudyGuide(BaseModel):
    summary: str
    key_points: list[str]
    practice_questions: list[str]

# 3. Create the Gemini client
client = genai.Client(api_key=api_key)

# 4. Get text from the user
print("=== GEMINI AI TEXT SUMMARIZER ===")
text = input("Enter text to summarize:\n").strip()

if not text:
    raise ValueError("Please enter some text.")

# 5. Send the text to Gemini
response = None

for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=(
                "Summarize the following text for a CSE student. "
                "Use simple English. Provide exactly three key points "
                "and two practice questions. Preserve the original meaning "
                "and do not invent facts.\n\n"
                f"TEXT:\n{text}"
            ),
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are a friendly AI tutor. "
                    "Create accurate, beginner-friendly study notes."
                ),
                response_mime_type="application/json",
                response_schema=StudyGuide,
            ),
        )
        break

    except errors.ServerError as error:
        if attempt == 2:
            print("Gemini is temporarily unavailable. Please try again later.")
            raise SystemExit(1)

        wait_seconds = 2 ** (attempt + 1)
        print(f"Temporary server error. Retrying in {wait_seconds} seconds...")
        time.sleep(wait_seconds)

if response is None:
    raise SystemExit("Could not get a response from Gemini.")

# 6. Parse the structured JSON response
result = StudyGuide.model_validate_json(response.text)

# 7. Display the results
print("\n=== SUMMARY ===")
print(result.summary)

print("\n=== KEY POINTS ===")
for point in result.key_points:
    print("-", point)

print("\n=== PRACTICE QUESTIONS ===")
for number, question in enumerate(
    result.practice_questions, start=1
):
    print(f"{number}. {question}")
