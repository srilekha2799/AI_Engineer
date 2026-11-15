
import os
import chromadb

from google import genai
from google.genai import types

# ----------------------------------
# 1. Check Gemini API key
# ----------------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY first.")

client = genai.Client(api_key=api_key)


# ----------------------------------
# 2. Connect to ChromaDB
# ----------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="college_semantic_search",
    metadata={"hnsw:space": "cosine"}
)


# ----------------------------------
# 3. Sample college documents
# ----------------------------------

documents = [
    "Students must submit leave applications through the student portal. Approval from the class advisor is required.",

    "The semester examination timetable is published on the college website. Students should check the examination section regularly.",

    "Students can pay their semester fees through the online student portal using available digital payment methods.",

    "Students interested in campus placements must register with the placement cell and upload their updated resumes.",

    "The college library is open from 9 AM to 5 PM on working days. Students must carry their college ID cards."
]

ids = [
    "doc1",
    "doc2",
    "doc3",
    "doc4",
    "doc5"
]

metadatas = [
    {"category": "Leave"},
    {"category": "Examination"},
    {"category": "Fees"},
    {"category": "Placement"},
    {"category": "Library"}
]


# ----------------------------------
# 4. Generate document embeddings
# ----------------------------------

def generate_embedding(text):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        )
    )

    return response.embeddings[0].values


# ----------------------------------
# 5. Convert all documents to vectors
# ----------------------------------

embeddings = []

for document in documents:

    vector = generate_embedding(document)

    embeddings.append(vector)


# ----------------------------------
# 6. Store documents in ChromaDB
# ----------------------------------

collection.upsert(
    ids=ids,
    embeddings=embeddings,
    documents=documents,
    metadatas=metadatas
)


print("Documents successfully stored!")
print("Total documents:", collection.count())
