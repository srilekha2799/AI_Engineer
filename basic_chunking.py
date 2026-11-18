def chunk_text(text, chunk_size):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


text = """
Python is a high-level programming language.
It is widely used in artificial intelligence.
Python supports object-oriented programming.
It is also popular in data science.
"""

chunks = chunk_text(text, 50)

for index, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {index}:")
    print(chunk)


# overlap

def chunk_text1(text, chunk_size, overlap):

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "Overlap must be non-negative and smaller than chunk size."
        )

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(text), step):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


text = """
Retrieval Augmented Generation is an AI technique.
It combines information retrieval with text generation.
Documents are divided into smaller chunks.
These chunks are converted into embeddings.
Relevant information is retrieved for user questions.
"""

chunks = chunk_text1(
    text,
    chunk_size=100,
    overlap=20
)

for index, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {index}:")
    print(chunk)
