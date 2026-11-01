import os
from google import genai

# 1. Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

# 2. Initialize Gemini
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.8-flash"


# 3. Source text
source_text = """
Machine Learning is a branch of Artificial Intelligence
that enables computers to learn patterns from data.

Supervised Learning uses labeled data to train models.
Classification predicts categories, while regression
predicts numerical values.

Unsupervised Learning works with unlabeled data.
Clustering groups similar data points.

Machine Learning is used in healthcare, fraud detection,
recommendation systems, and image recognition.
"""


# 4. Define three prompts
prompts = {

    "PROMPT A - BASIC": f"""
    Summarize this text:

    {source_text}
    """,

    "PROMPT B - IMPROVED": f"""
    Summarize the following text for a first-year CSE student.

    Use simple English.
    Preserve the original meaning.
    Keep the summary under 100 words.
    Do not invent facts.

    Text:
    {source_text}
    """,

    "PROMPT C - STRUCTURED": f"""
    You are an educational AI assistant.

    Task:
    Summarize the following Machine Learning text.

    Audience:
    First-year CSE student.

    Requirements:
    - Explain what Machine Learning is.
    - Explain supervised learning.
    - Explain unsupervised learning.
    - Mention the listed applications.
    - Use simple English.
    - Do not add unsupported facts.

    Output format:
    1. Title
    2. Summary
    3. Three key points

    Text:
    {source_text}
    """
}


# 5. Function to generate response
def generate_response(prompt):

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text or ""


# 6. Basic output evaluation
def evaluate_output(output):

    word_count = len(output.split())

    return {
        "word_count": word_count,
        "has_output": bool(output.strip()),
        "has_title": "title" in output.lower(),
        "has_key_points": "key points" in output.lower()
    }


# 7. Test each prompt
results = {}

for prompt_name, prompt in prompts.items():

    print("\n" + "=" * 60)
    print(prompt_name)
    print("=" * 60)

    try:

        output = generate_response(prompt)

        results[prompt_name] = {
            "output": output,
            "evaluation": evaluate_output(output)
        }

        print("\nGENERATED OUTPUT:")
        print(output)

        print("\nEVALUATION:")
        print(results[prompt_name]["evaluation"])

    except Exception as error:

        print("Error:", error)


# 8. Final comparison
print("\n" + "=" * 60)
print("FINAL PROMPT COMPARISON")
print("=" * 60)

for name, result in results.items():

    evaluation = result["evaluation"]

    print("\n", name)
    print("Word count:", evaluation["word_count"])
    print("Output available:", evaluation["has_output"])
    print("Contains title:", evaluation["has_title"])
    print("Contains key points:", evaluation["has_key_points"])