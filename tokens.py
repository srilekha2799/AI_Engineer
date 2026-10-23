
import tiktoken

# Load a tokenizer used by OpenAI models
encoding = tiktoken.get_encoding("o200k_base")

text = input("Enter some text: ")

tokens = encoding.encode(text)

print("\nOriginal text:", text)
print("Tokens:", encoding.decode_single_token_bytes(tokens[0]) if tokens else "No tokens")
print("Token IDs:", tokens)
print("Total tokens:", len(tokens))
print("Character count:", len(text))
print("Token pieces:", [
    encoding.decode_single_token_bytes(token).decode("utf-8", errors="replace")
    for token in tokens
])