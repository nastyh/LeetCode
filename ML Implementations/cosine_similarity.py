import math
import numpy as np

def cosine_similarity(vec1, vec2):
    """
    Calculates the cosine similarity between two non-zero vectors.
    Args:
        vec1 (numpy.ndarray): The first vector.
        vec2 (numpy.ndarray): The second vector.

    Returns:
        float: The cosine similarity between the two vectors. Returns -2 if vectors are not the same length, or -1 if either vector has a magnitude of 0.

        1 means the vectors are perfectly aligned (same direction).
        0 means the vectors are orthogonal (no similarity).
        -1 means the vectors are perfectly opposite.

        Handles sparse data (ignores zero entities: users didn't interact with)
        Users may have different rating scales 
        Cosine similarity normalizes the vectors
        Because cosine similarity is magnitude invariant,
        it is very useful when the magnitude of the values being compared are not as important as the direction

    """
    if vec1.shape != vec2.shape:
        return -2  # Indicate vectors are not the same length

    magnitude_vec1 = np.linalg.norm(vec1) #  norm of the vector -- length or magnitude 
    # Euclidean norm for [x1..xn] is sqrt(x1**2 + ... + xn**2)
    # square root of the sum of the squared vector components
    magnitude_vec2 = np.linalg.norm(vec2)

    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return -1 #Indicate a vector has a magnitude of 0.

    dot_product = np.dot(vec1, vec2)
    return dot_product / (magnitude_vec1 * magnitude_vec2)


# can do the dot product manually
def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        return None 
    result = 0
    for i in range(len(vec1)):
        result += vec1[i] * vec2[i]
    return result

# we can do magnitude manually
def linalg_norm(vector, ord=None):
    if ord is None or ord == 2:  # Euclidean norm (L2 norm)
        squared_sum = sum(x**2 for x in vector)
        return math.sqrt(squared_sum)

    elif ord == 1:  # L1 norm (Manhattan norm)
        return sum(abs(x) for x in vector)

    elif ord == float('inf'):  # L-infinity norm (max norm)
        return max(abs(x) for x in vector)

    elif ord == float('-inf'): # negative infinity norm (min abs norm)
        return min(abs(x) for x in vector)

    else:
        raise ValueError("Unsupported norm order.")


# Example usage:
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
vec3 = np.array([1, 2, 3, 4])
vec4 = np.array([0, 0, 0])

similarity = cosine_similarity(vec1, vec2)
print(f"Cosine similarity between vec1 and vec2: {similarity}")

similarity_different_length = cosine_similarity(vec1, vec3)
print(f"Cosine similarity between vec1 and vec3 (different length): {similarity_different_length}")

similarity_zero_magnitude = cosine_similarity(vec1, vec4)
print(f"Cosine similarity between vec1 and vec4 (zero magnitude): {similarity_zero_magnitude}")