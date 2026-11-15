
# Day 24 - Semantic Search using Gemini + ChromaDB

import os
import chromadb
from google import genai
from google.genai import types

# --------------------------------
# 1. Initialize Gemini
# --------------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

gemini_client = genai.Client(api_key=api_key)

MODEL = "gemini-embedding-001"


# --------------------------------
# 2. Initialize ChromaDB
# --------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="college_documents",
    metadata={"hnsw:space": "cosine"}
)


# --------------------------------
# 3. Prepare documents
# --------------------------------

documents = [
    "Students can apply for leave through the student portal.",
    "Examination results are published on the college website.",
    "Semester fees must be paid before the deadline.",
    "Students can access placement opportunities through the placement cell.",
    "Library books can be borrowed using a valid student ID."
]

ids = [
    "doc_001",
    "doc_002",
    "doc_003",
    "doc_004",
    "doc_005"
]

metadatas = [
    {"category": "Leave"},
    {"category": "Examination"},
    {"category": "Fees"},
    {"category": "Placements"},
    {"category": "Library"}
]


# --------------------------------
# 4. Generate embeddings
# --------------------------------

def generate_embedding(text, task_type):

    response = gemini_client.models.embed_content(
        model=MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            task_type=task_type
        )
    )

    return response.embeddings[0].values


# --------------------------------
# 5. Store documents in Chroma
# --------------------------------

document_embeddings = []

for document in documents:

    embedding = generate_embedding(
        document,
        "RETRIEVAL_DOCUMENT"
    )

    document_embeddings.append(embedding)


collection.upsert(
    ids=ids,
    embeddings=document_embeddings,
    documents=documents,
    metadatas=metadatas
)

print("Documents stored successfully!")
print("Total records:", collection.count())


# --------------------------------
# 6. Search documents
# --------------------------------

user_query = input("\nAsk a college-related question: ")

query_embedding = generate_embedding(
    user_query,
    "RETRIEVAL_QUERY"
)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3,
    include=["documents", "metadatas", "distances"]
)


# --------------------------------
# 7. Display search results
# --------------------------------

print("\n========== SEARCH RESULTS ==========")

for i in range(len(results["ids"][0])):

    print(f"\nResult {i + 1}")

    print("Document:", results["documents"][0][i])

    print("Category:", results["metadatas"][0][i]["category"])

    print("Cosine Distance:", round(
        results["distances"][0][i], 4
    ))

print("\n====================================")
