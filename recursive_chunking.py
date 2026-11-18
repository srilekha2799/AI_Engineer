
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Transmission Control Protocol (TCP) is a
connection-oriented transport protocol.

TCP provides reliable data transmission
using acknowledgements and retransmissions.

User Datagram Protocol (UDP) is a
connectionless transport protocol.

UDP does not guarantee reliable delivery
or packet ordering.
"""

# Create the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30
)

# Split the text
chunks = splitter.split_text(text)

# Display the results
print("Total chunks:", len(chunks))

for index, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {index}:")
    print(chunk)
