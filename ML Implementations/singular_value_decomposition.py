import numpy as np

def svd(A):
    """
    Performs Singular Value Decomposition on matrix A.
    find the principal directions of variance in the data.
    The eigenvectors of the covariance matrix correspond to these principal directions.
    By finding the eigenvectors, we can project the data onto a lower-dimensional space\
    while preserving most of the variance.
    Args:
        A: Input matrix.
    Returns:
        U, Sigma, V: SVD decomposition of A.
        U: Orthogonal matrix containing left singular vectors.
        Σ: Diagonal matrix containing singular values.
        V^T: Orthogonal matrix containing right singular vectors.
    """

    # Compute the covariance matrix A^T * A
    A_T_A = np.dot(A.T, A)

    # Compute eigenvalues and eigenvectors of A^T * A
    eigenvalues, eigenvectors = np.linalg.eig(A_T_A)

    # Sort eigenvalues and eigenvectors in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Compute singular values (square root of eigenvalues)
    singular_values = np.sqrt(eigenvalues)

    # Compute right singular vectors (V)
    V = eigenvectors

    # Compute left singular vectors (U)
    # np.newaxis inserts a new dimension along axis 0, effectively transforming the 1D array into a column vector.
    U = np.dot(A, V) / singular_values[:, np.newaxis] # creates a column vector from the singular values array singular_values.

    # Create the diagonal matrix of singular values (Sigma)
    # he context of SVD creates a diagonal matrix with the singular values on its main diagonal.
    # NumPy function takes a 1D array (in this case, the singular values) and creates a diagonal matrix.
    # The input array elements are placed on the main diagonal of the output matrix, and all other elements are set to zero.

    # A = U * Σ * V^T
    """
    The Σ matrix is a diagonal matrix containing the singular values.
    By creating a diagonal matrix from the singular values using
    np.diag(singular_values), we ensure that the multiplication with the orthogonal
    matrices U and V^T correctly reconstructs the original matrix A.   
    """
    Sigma = np.diag(singular_values)

    return U, Sigma, V.T


 # HOW TO RECOMMEND TOP10 UNSEEN ITEMS FOR USER 352 AFTER DOING ALL OF THAT
    import numpy as np

    # Assume U and V are numpy arrays
    # U: m x k matrix (User latent factors)
    # V: k x n matrix (Item latent factors)
    # R: m x n matrix (Original user-item interactions)
    
    def recommend_top_n(user_id, U, V, R, n=10):
        # Step 1: Extract user latent factors
        user_vector = U[user_id]  # Shape: (1, k)
        
        # Step 2: Compute predicted scores for all items
        predicted_scores = np.dot(user_vector, V)  # Shape: (1, n)
        
        # Step 3: Filter out seen items
        seen_items = np.where(R[user_id] > 0)[0]  # Indices of items the user has interacted with
        unseen_scores = np.copy(predicted_scores)
        unseen_scores[seen_items] = -np.inf  # Set scores of seen items to -inf to exclude them
        
        # Step 4: Get top N items
        top_n_indices = np.argsort(unseen_scores)[-n:][::-1]  # Indices of top N items
        return top_n_indices
    
    # Example Usage
    user_id = 352
    top_10_items = recommend_top_n(user_id, U, V, R, n=10)
    print("Top 10 recommended items for User 352:", top_10_items)
