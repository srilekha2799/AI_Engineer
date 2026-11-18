
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load the PDF
reader = PdfReader("Computer_Networks.pdf")

# 2. Create the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

all_chunks = []

# 3. Extract and split each page
for page_number, page in enumerate(reader.pages, start=1):

    text = page.extract_text()

    if not text or not text.strip():
        continue

    # 4. Split page text
    chunks = splitter.split_text(text)

    # 5. Preserve metadata
    for chunk_index, chunk in enumerate(chunks, start=1):

        document = {
            "content": chunk,
            "metadata": {
                "source": "Computer_Networks.pdf",
                "page": page_number,
                "chunk": chunk_index
            }
        }

        all_chunks.append(document)

# 6. Display results
print("Total chunks:", len(all_chunks))

for document in all_chunks[:5]:

    print("\n--------------------")

    print("Metadata:", document["metadata"])

    print("Content:", document["content"])