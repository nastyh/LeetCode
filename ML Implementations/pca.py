import numpy as np
import matplotlib.pyplot as plt

def pca(X, n_components):
    """
    Performs Principal Component Analysis (PCA) on the given data.

    Args:
        X: The input data (NumPy array).  Rows are samples, columns are features.
        n_components: The number of principal components to keep.

    Returns:
        A tuple containing:
            - principal_components: The top n_components eigenvectors (NumPy array).
            - explained_variance_ratio: The explained variance ratio for each component.
            - X_transformed: The transformed data (NumPy array).
    """

    # 1. Center the data
    X_mean = np.mean(X, axis=0)  # Calculate the mean of each feature (column)
    X_centered = X - X_mean       # Subtract the mean from each data point

    # 2. Calculate the covariance matrix
    covariance_matrix = np.cov(X_centered, rowvar=False)  # rowvar=False is crucial: features are in columns

    # 3. Calculate the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    # 4. Sort eigenvalues and eigenvectors in descending order of eigenvalues
    sorted_indices = np.argsort(eigenvalues)[::-1]  # Get indices for descending sort
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # 5. Calculate the explained variance ratio
    total_variance = np.sum(eigenvalues)
    explained_variance_ratio = eigenvalues / total_variance

    # 6. Select the top n_components eigenvectors (principal components)
    principal_components = eigenvectors[:, :n_components]

    # 7. Project the data onto the principal components
    X_transformed = np.dot(X_centered, principal_components)

    return principal_components, explained_variance_ratio, X_transformed

def test_pca():
    # Create some sample data (2D for easy visualization)
    np.random.seed(0)
    X = np.dot(np.random.rand(100, 2), [[1, 2], [2, 1]]) + np.array([5, 5])  # Creates correlated data

    # Run PCA with 1 component and visualize
    n_components = 1
    principal_components, explained_variance_ratio, X_transformed = pca(X, n_components)

    print("Principal Components (1 component):\n", principal_components)
    print("Explained Variance Ratio (1 component):\n", explained_variance_ratio)

    assert explained_variance_ratio[0] > 0.9, "Explained variance (1 component) is too low. PCA might be incorrect."
    print("Test passed: Explained variance (1 component) is high enough.")

    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], label="Original Data")
    plt.scatter(X_transformed, np.zeros_like(X_transformed), label="Transformed Data (1 Component)", color='red')
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.title("PCA Transformation (1 Component)")
    plt.legend()
    plt.grid(True)
    plt.show()


    # Run PCA with 2 components, reconstruct, and visualize
    n_components = 2
    _, explained_variance_ratio, X_transformed = pca(X, n_components)

    print("Explained Variance Ratio (2 components):", explained_variance_ratio)
    assert sum(explained_variance_ratio) > 0.99, "Explained variance (2 components) is too low."
    print("Test passed: Explained variance (2 components) is high enough.")


    assert np.allclose(X, X_transformed + np.mean(X, axis=0)), "Reconstruction failed with 2 components"
    print("Test passed: Reconstruction successful with 2 components.")

    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], label="Original Data")
    plt.scatter(X_transformed[:, 0], X_transformed[:, 1], label="Transformed Data (2 Components)", color='green')
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("PCA Transformation (2 Components)")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("All PCA tests passed!")


if __name__ == "__main__":
    test_pca()
