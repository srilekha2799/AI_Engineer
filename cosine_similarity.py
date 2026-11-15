
import math

# Two example vectors
A = [1, 2]
B = [2, 1]

# Step 1: Calculate dot product
def dot_product(A, B):
    total = 0

    for i in range(len(A)):
        total += A[i] * B[i]

    return total

# Step 2: Calculate vector magnitude
def magnitude(vector):
    total = 0

    for value in vector:
        total += value ** 2

    return math.sqrt(total)

# Step 3: Calculate cosine similarity
def cosine_similarity(A, B):

    if len(A) != len(B):
        raise ValueError("Vectors must have the same dimensions.")

    mag_A = magnitude(A)
    mag_B = magnitude(B)

    if mag_A == 0 or mag_B == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector.")

    dot = dot_product(A, B)

    similarity = dot / (mag_A * mag_B)

    return similarity

# Test the function
score = cosine_similarity(A, B)

print("Vector A:", A)
print("Vector B:", B)
print("Cosine Similarity:", score)