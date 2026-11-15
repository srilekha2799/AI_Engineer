
import os
from google import genai
from google.genai import types
import numpy as np

# 1. Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

# 2. Create Gemini client
client = genai.Client(api_key=api_key)

MODEL = "gemini-embedding-001"

# 3. Sentences to compare
sentences = [
    "I love learning Artificial Intelligence.",
    "I enjoy studying AI and machine learning.",
    "I like playing cricket with my friends."
]

# 4. Generate embeddings
response = client.models.embed_content(
    model=MODEL,
    contents=sentences,
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY"
    )
)

# 5. Extract vectors
embeddings = [
    np.array(item.values)
    for item in response.embeddings
]

# 6. Calculate cosine similarity
def cosine_similarity(A, B):
    return np.dot(A, B) / (
        np.linalg.norm(A) * np.linalg.norm(B)
    )

# 7. Compare sentence pairs
for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):

        score = cosine_similarity(
            embeddings[i],
            embeddings[j]
        )

        print("\nSentence 1:", sentences[i])
        print("Sentence 2:", sentences[j])
        print("Similarity Score:", round(float(score), 4))