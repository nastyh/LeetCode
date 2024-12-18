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