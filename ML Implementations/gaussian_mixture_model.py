import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

def gaussian_mixture_model(X, n_components, max_iter=100, tol=1e-4):
    """
    Performs Gaussian Mixture Model (GMM) clustering using the EM algorithm.

    Args:
        X: The input data (NumPy array). Rows are samples, columns are features.
        n_components: The number of Gaussian components.
        max_iter: The maximum number of iterations for the EM algorithm.
        tol: The tolerance for convergence.

    Returns:
        A tuple containing:
            - weights: The weights of each component (NumPy array).
            - means: The means of each component (NumPy array).
            - covariances: The covariance matrices of each component (NumPy array).
            - responsibilities: The responsibilities of each data point to each component.
    """

    n_samples, n_features = X.shape

    # 1. Initialization
    weights = np.ones(n_components) / n_components  # Equal weights
    means = X[np.random.choice(n_samples, n_components, replace=False)]  # Randomly select initial means
    covariances = np.array([np.eye(n_features)] * n_components)  # Initialize with identity covariance matrices

    log_likelihood_old = -np.inf

    for _ in range(max_iter):
        # 2. E-step (calculate responsibilities)
        responsibilities = np.zeros((n_samples, n_components))
        for i in range(n_components):
            responsibilities[:, i] = weights[i] * multivariate_normal.pdf(X, means[i], covariances[i])
        responsibilities /= np.sum(responsibilities, axis=1, keepdims=True)  # Normalize

        # 3. M-step (update parameters)
        Nk = np.sum(responsibilities, axis=0)  # Number of points assigned to each component
        weights = Nk / n_samples
        means = np.array([np.average(X, axis=0, weights=responsibilities[:, i]) for i in range(n_components)])
        for i in range(n_components):
            X_centered = X - means[i]
            covariances[i] = np.dot(responsibilities[:, i] * X_centered.T, X_centered) / Nk[i] + np.eye(n_features) * 1e-6 # Add small value for numerical stability

        # 4. Check for convergence
        log_likelihood = np.sum(np.log(np.sum(responsibilities * multivariate_normal.pdf(X[:, np.newaxis], means, covariances), axis=1)))
        if np.abs(log_likelihood - log_likelihood_old) < tol:
            break
        log_likelihood_old = log_likelihood

    return weights, means, covariances, responsibilities



def test_gmm():
    # Create some sample data (mixture of two Gaussians)
    np.random.seed(0)
    X = np.concatenate([
        np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100),
        np.random.multivariate_normal([5, 5], [[1, -0.2], [-0.2, 1]], 150)
    ])

    # Run GMM
    n_components = 2
    weights, means, covariances, responsibilities = gaussian_mixture_model(X, n_components)

    print("Weights:", weights)
    print("Means:", means)
    print("Covariances:", covariances)

    # Evaluate (qualitative - visualize the clusters)
    cluster_assignments = np.argmax(responsibilities, axis=1)

    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=cluster_assignments, cmap='viridis')
    plt.title("GMM Clustering")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()


    # Test with 3 components (should overfit a little)
    n_components = 3
    weights, means, covariances, responsibilities = gaussian_mixture_model(X, n_components)

    cluster_assignments = np.argmax(responsibilities, axis=1)

    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=cluster_assignments, cmap='viridis')
    plt.title("GMM Clustering (3 components)")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

    print("GMM tests completed (visual evaluation recommended).")


if __name__ == "__main__":
    test_gmm()