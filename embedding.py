# Day 20 - Understanding Embeddings

# These are illustrative vectors, NOT actual model embeddings.

sentence_1 = [0.2, 0.8, 0.4, 0.6]
sentence_2 = [0.3, 0.7, 0.5, 0.6]
sentence_3 = [0.9, 0.1, 0.2, 0.3]

# 1. Print the vectors
print("Sentence 1:", sentence_1)
print("Sentence 2:", sentence_2)
print("Sentence 3:", sentence_3)

# 2. Find vector dimensions
print("\nVector dimensions:")

print("Sentence 1:", len(sentence_1))
print("Sentence 2:", len(sentence_2))
print("Sentence 3:", len(sentence_3))

# 3. Access individual vector values
print("\nFirst dimension of Sentence 1:")
print(sentence_1[0])

# 4. Check vector length
print("\nNumber of values in Sentence 1:")
print(len(sentence_1))