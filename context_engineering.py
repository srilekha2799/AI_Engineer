import os
from google import genai
import time

# 1. Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

# 2. Create Gemini client
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.8-flash"


# 3. Define system instruction
system_instruction = """
You are a friendly AI study assistant.

Answer questions using the provided study context.

Rules:
- Use simple English.
- Give beginner-friendly explanations.
- Do not invent information.
- If the answer is not present in the context,
  clearly say that the provided context does not contain it.
"""


# 4. Define background context
study_context = """
Topic: Machine Learning

Machine Learning is a branch of Artificial Intelligence.

Supervised Learning:
- Learns using labeled training data.
- Classification predicts categories.
- Regression predicts numerical values.

Unsupervised Learning:
- Learns patterns from unlabeled data.
- Clustering groups similar data points.

Examples:
- Email spam detection is classification.
- House price prediction is regression.
- Customer segmentation is clustering.
"""


# 5. Collect user question
print("=== CONTEXT-AWARE AI STUDY ASSISTANT ===")

question = input("\nAsk a Machine Learning question: ").strip()

if not question:
    raise ValueError("Question cannot be empty.")


# 6. Construct the context-aware prompt
prompt = f"""
Use the following study material to answer the question.

<study_context>
{study_context}
</study_context>

<user_question>
{question}
</user_question>

If the study material does not contain the answer,
say so clearly. Do not make up information.
"""


# 7. Send request to Gemini
# 7. Send request to Gemini with retry handling

max_retries = 3

for attempt in range(1, max_retries + 1):

    try:
        print(f"\nSending request... Attempt {attempt}")

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config={
                "system_instruction": system_instruction
            }
        )

        print("\n=== AI ANSWER ===")

        if response.text:
            print(response.text)
        else:
            print("No response received.")

        break

    except Exception as error:

        print("Error:", error)

        if attempt < max_retries:
            wait_time = 2 ** attempt

            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

        else:
            print("Maximum retries reached.")
            print("Please try again later.")