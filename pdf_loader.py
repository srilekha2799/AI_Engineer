
from pypdf import PdfReader

def load_pdf(file_path):

    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(
        reader.pages, start=1
    ):

        text = page.extract_text()

        if text and text.strip():

            document = {
                "content": text.strip(),
                "metadata": {
                    "source": file_path,
                    "page": page_number
                }
            }

            documents.append(document)

    return documents

# Load the PDF
documents = load_pdf("Computer_Networks.pdf")

# Display extracted information
print("Total extracted pages:", len(documents))

for document in documents:

    print("\nPage:", document["metadata"]["page"])

    print("Source:", document["metadata"]["source"])

    print("Content:")
    print(document["content"][:300])