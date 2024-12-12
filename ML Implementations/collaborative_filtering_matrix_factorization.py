"""
You are given a dataset of user-item interactions (ratings). Each user has rated a subset of items on a scale from 1 to 5. Your task is to:
1. Implement a collaborative filtering-based recommendation system using Matrix Factorization.
2. Predict the missing ratings for the user-item pairs and recommend the top 3 items for each user that they haven't rated yet.
"""

import numpy as np
import pandas as pd

ratings_matrix = pd.DataFrame(
    data=[
        [5, 3, np.nan, 1],
        [4, np.nan, np.nan, 1],
        [1, 1, np.nan, 5],
        [np.nan, np.nan, 4, 4],
        [np.nan, 4, 5, np.nan],
    ],
    index=['User1', 'User2', 'User3', 'User4', 'User5'],
    columns=['Item1', 'Item2', 'Item3', 'Item4']
)

"""
Implementation steps
data (D) --> users vs. items
D = P * Qt
P will be a matrix w/ coefficients for users 
Q  --""--                  for items        
Sizes: 
P = len(data): 5 times k 
Q = len(data[0]) 4 times k
where k is the length of the embaddings matrix for users and items respectively
"""
"""
L = ||D - P * Qt||^2 = (D - P * Qt)t * (D - P * Qt)
diff L / diff P = -Q * (D - P * Qt)
diff L / diff Q = -P * (D - P * Qt)
"""


def matrix_factorization(R, K, steps=100, alpha=0.0002, beta=0.02):
    """
    Performs matrix factorization by alternating least squares.

    Args:
        R: User-item rating matrix
        K: Number of latent features
        steps: Number of iterations
        alpha: Learning rate
        beta: Regularization parameter

    Returns:
        P: User feature matrix
        Q: Item feature matrix

    Stochastic Gradient Descent (SGD): We use SGD to update the latent factors iteratively,
    considering one rating at a time. This can be more efficient for large datasets.
    Regularization: The regularization term (0.01 * P[i,:] and 0.01 * Q[j,:]) helps prevent overfitting.
    Hyperparameter Tuning: Experiment with different values for K, learning_rate, and epochs to optimize performance.
    Cold Start Problem: For new users or items, content-based filtering or popularity-based recommendations can be combined.
    """

    num_users, num_items = R.shape
    P = np.random.rand(num_users, K)
    Q = np.random.rand(num_items, K)

    for step in range(steps):
        for i in range(num_users):
            for j in range(num_items):
                if R[i][j] > 0:
                    eij = R[i][j] - np.dot(P[i,:], Q[j,:].T)
                    P[i,:] += alpha * (eij * Q[j,:] - beta * P[i,:])
                    Q[j,:] += alpha * (eij * P[i,:] - beta * Q[j,:])

    return P, Q

# Convert the DataFrame to a NumPy array
R = ratings_matrix.values

# Perform matrix factorization
K = 2  # Number of latent features
P, Q = matrix_factorization(R, K)

# Predict missing ratings
predicted_ratings = np.dot(P, Q.T)

# Fill in missing values in the original DataFrame
for i in range(len(ratings_matrix)):
    for j in range(len(ratings_matrix.columns)):
        if np.isnan(ratings_matrix.iloc[i, j]):
            ratings_matrix.iloc[i, j] = predicted_ratings[i, j]