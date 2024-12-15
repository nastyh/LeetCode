# Import necessary libraries
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import svds

# User-Item interaction matrix (R)
R = np.array([[4, 0, 2], [0, 5, 0], [3, 0, 0]])

# Convert to sparse matrix
R_sparse = lil_matrix(R)

# Apply Matrix Factorization (SVD)
num_factors = 2
U, sigma, Vt = svds(R_sparse, k=num_factors)

# Reconstruct matrix with reduced dimensions
R_reconstructed = np.dot(np.dot(U, np.diag(sigma)), Vt)

# Predictions for all items
all_user_predicted_ratings = np.dot(np.dot(U, np.diag(sigma)), Vt)

# Top-N recommendations for a user
user_id = 0
user_ratings = all_user_predicted_ratings[user_id]

# Sort the ratings in descending order and get item indices
sorted_indices = np.argsort(-user_ratings)

# Recommend top 2 items that the user has not rated
top_recommended_indices = sorted_indices[~R[user_id].astype(bool)][:2]