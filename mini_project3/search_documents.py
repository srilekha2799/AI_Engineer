
import os
import chromadb

from google import genai
from google.genai import types


# ----------------------------------
# 1. Check API key
# ----------------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

client = genai.Client(api_key=api_key)


# ----------------------------------
# 2. Connect to existing database
# ----------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="college_semantic_search",
    metadata={"hnsw:space": "cosine"}
)


# ----------------------------------
# 3. Generate query embedding
# ----------------------------------

def generate_query_embedding(question):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )

    return response.embeddings[0].values


# ----------------------------------
# 4. Search the database
# ----------------------------------

def search_documents(question):

    query_vector = generate_query_embedding(question)

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=3,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return results


# ----------------------------------
# 5. Display search results
# ----------------------------------

def display_results(results):

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]
    ids = results["ids"][0]

    print("\n===== SEARCH RESULTS =====")

    for i in range(len(documents)):

        distance = distances[i]

        similarity = 1 - distance

        print(f"\nResult {i + 1}")
        print("------------------------")

        print("ID:", ids[i])
        print("Category:", metadatas[i]["category"])
        print("Document:", documents[i])

        print("Cosine similarity:",
              round(similarity, 4))


# ----------------------------------
# 6. Main application
# ----------------------------------

print("===== COLLEGE SEMANTIC SEARCH =====")

if collection.count() == 0:
    raise ValueError(
        "No documents found. Run ingest_documents.py first."
    )

while True:

    question = input(
        "\nEnter your question (or type exit): "
    )

    if question.lower() == "exit":
        print("Thank you for using Semantic Search!")
        break

    if not question.strip():
        print("Please enter a valid question.")
        continue

    results = search_documents(question)

    display_results(results)
