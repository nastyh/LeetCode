"""
“Implement a basic version of matrix factorization (e.g., SVD) for dimensionality reduction on a user-item matrix.
Explain how reducing dimensionality can help in computing similarities.”
Follow-up: “How do you choose the number of latent features, and what impact does this choice have on recommendations?”
"""
import numpy as np


"""
Reduced Sparsity:
User-item rating matrices are often very sparse. SVD or other matrix factorization techniques
can fill in the missing values by approximating the original matrix with a lower-rank matrix.
This reduces sparsity, making it easier to compute meaningful similarities.

Latent Features:
Matrix factorization decomposes the original high-dimensional user-item matrix into two lower-dimensional matrices: a user latent feature matrix and an item latent feature matrix.
These latent features capture underlying patterns and relationships that may not be apparent in the original data.
By computing similarities in this lower-dimensional latent space, we can often obtain more accurate and robust results.

Noise Reduction:
Dimensionality reduction can help filter out noise and irrelevant information from the original data, leading to more reliable similarity measures.

Computational Efficiency:
Computing similarities in a lower-dimensional space is computationally less expensive than in the original high-dimensional space, especially for large datasets.
Choosing the Number of Latent Features (k) and Its Impact:

Methods for Choosing k:

Explained Variance:
Examine the singular values (S) from SVD. The singular values represent the amount of variance captured by each latent feature.
Choose k such that the first k singular values explain a significant portion (e.g., 80-90%) of the total variance.
Cross-Validation:
Split the data into training and validation sets.
Train the matrix factorization model with different values of k and evaluate its performance on the validation set (e.g., using RMSE or MAE).
Choose the value of k that yields the best performance.
Trial and Error:
Experiment with different values of k and observe the impact on recommendation quality.
This approach can be time-consuming but can provide valuable insights.
Domain Knowledge:
If there is prior knowledge about the data, that knowledge can be used to inform the choice of k.
Impact of k on Recommendations:

Small k:
Underfitting: The model may not capture enough of the underlying patterns in the data, leading to poor recommendations.
Oversimplification: The latent features may be too general, resulting in recommendations that are not personalized enough.
Reduced noise: smaller k values can filter out noise.
Large k:
Overfitting: The model may overfit the training data, capturing noise and irrelevant details, leading to poor generalization.
Increased computational cost: larger k values increase the amount of computation required.
Increased complexity: the model may become overly complex, making it difficult to interpret the latent features.
Optimal k:
A well-chosen value of k balances the trade-off between underfitting and overfitting, leading to accurate and personalized recommendations.
The optimal k, will allow the model to capture the meaningful patterns in the data, while filtering out noise.
"""

def matrix_factorization_svd(ratings, k):
    """
    Performs matrix factorization using Singular Value Decomposition (SVD).

    Args:
        ratings (numpy.ndarray): User-item ratings matrix.
        k (int): Number of latent features.

    Returns:
        numpy.ndarray: User latent feature matrix.
        numpy.ndarray: Item latent feature matrix.
    """
    U, S, Vt = np.linalg.svd(ratings)
    Sk = np.diag(S[:k])
    Uk = U[:, :k]
    Vk = Vt[:k, :].T

    return Uk, Vk

def compute_reduced_similarity(user_latent_matrix, item_latent_matrix, user_index, item_index):
    """
    Computes the cosine similarity between a user and item in the reduced latent space.

    Args:
        user_latent_matrix (numpy.ndarray): User latent feature matrix.
        item_latent_matrix (numpy.ndarray): Item latent feature matrix.
        user_index (int): Index of the user.
        item_index (int): Index of the item.

    Returns:
        float: Cosine similarity between the user and item.
    """
    user_vector = user_latent_matrix[user_index, :]
    item_vector = item_latent_matrix[item_index, :]
    return cosine_similarity(user_vector, item_vector)

def cosine_similarity(vec1, vec2):
    """Calculates the cosine similarity between two vectors."""
    magnitude_vec1 = np.linalg.norm(vec1)
    magnitude_vec2 = np.linalg.norm(vec2)

    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0

    dot_product = np.dot(vec1, vec2)
    return dot_product / (magnitude_vec1 * magnitude_vec2)

# Example usage:
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
])

k = 2  # Number of latent features
user_latent, item_latent = matrix_factorization_svd(ratings, k)

user_index = 0
item_index = 2
similarity = compute_reduced_similarity(user_latent, item_latent, user_index, item_index)
print(f"Similarity between user {user_index} and item {item_index} in reduced space: {similarity}")