# Day 23 - Understanding Vector Database Records

documents = [
    {
        "id": "doc_001",
        "text": "Students can apply for leave through the portal.",
        "embedding": [0.21, 0.42, 0.81],
        "metadata": {
            "category": "Leave",
            "department": "Administration"
        }
    },
    {
        "id": "doc_002",
        "text": "Examination results are published online.",
        "embedding": [0.61, 0.12, 0.32],
        "metadata": {
            "category": "Examination",
            "department": "Academics"
        }
    }
]

# Display all records
for document in documents:
    print("\nDocument ID:", document["id"])
    print("Text:", document["text"])
    print("Embedding:", document["embedding"])
    print("Metadata:", document["metadata"])

# Filter documents by category
print("\nLeave-related documents:")

for document in documents:
    if document["metadata"]["category"] == "Leave":
        print(document["text"])