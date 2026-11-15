
import os
from google import genai
from google.genai import types

# 1. Get the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

# 2. Create Gemini client
client = genai.Client(api_key=api_key)

# 3. Select embedding model
MODEL = "gemini-embedding-001"

# 4. Text we want to convert into an embedding
text = "I love learning Artificial Intelligence."

# 5. Generate embedding
response = client.models.embed_content(
    model=MODEL,
    contents=text,
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY"
    )
)

# 6. Extract the numerical vector
embedding = response.embeddings[0].values

# 7. Display results
print("Original Text:")
print(text)

print("\nGenerated Embedding:")
print(embedding)

print("\nNumber of Dimensions:")
print(len(embedding))

print("\nFirst 5 Values:")
print(embedding[:5])

# 8. Multiple Sentences
sentences = [
    "I love learning Artificial Intelligence.",
    "Machine learning helps computers learn from data.",
    "I enjoy playing cricket with my friends."
]

response = client.models.embed_content(
    model=MODEL,
    contents=sentences,
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY"
    )
)

for index, item in enumerate(response.embeddings):
    vector = item.values

    print(f"\nSentence {index + 1}:")
    print(sentences[index])

    print("Dimensions:", len(vector))
    print("First 5 values:", vector[:5])