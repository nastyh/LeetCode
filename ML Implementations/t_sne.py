import numpy as np
import matplotlib.pyplot as plt

def euclidean_distance(x1, x2):
    """Calculates the Euclidean distance between two vectors."""
    return np.sqrt(np.sum((x1 - x2)**2))

def pairwise_distances(X):
    """Calculates pairwise Euclidean distances between all samples in X."""
    n_samples = X.shape # Corrected: Access the number of rows (samples)
    distances = np.zeros((n_samples, n_samples))
    for i in range(n_samples):
        for j in range(i + 1, n_samples):  # Avoid redundant calculations
            dist = euclidean_distance(X[i], X[j])
            distances[i, j] = dist
            distances[j, i] = dist  # Distance is symmetric
    return distances


def tsne(X, n_components=2, perplexity=30.0, n_iter=300, learning_rate=200.0):
    """
    Performs t-SNE dimensionality reduction (with custom distance function).

    Args:
        X: The input data (NumPy array). Rows are samples, columns are features.
        n_components: The number of dimensions to reduce to.
        perplexity: The perplexity parameter (typically between 5 and 50).
        n_iter: The number of iterations for optimization.
        learning_rate: The learning rate for optimization.

    Returns:
        The low-dimensional embedding of the data (NumPy array).
    """

    n_samples = X.shape

    # 1. Calculate pairwise affinities (p_ij) - using our custom function
    distances = pairwise_distances(X)  # Now uses the custom pairwise_distances
    P = np.zeros((n_samples, n_samples))

    for i in range(n_samples):
        betamin = -np.inf
        betamax = np.inf
        Di = distances[i]
        Hdi = 0

        desired_entropy = np.log(perplexity)

        Hdiff = 1
        tries = 0

        while np.abs(Hdiff) > 1e-5 and tries < 50:
            beta = (betamin + betamax) / 2.0

            numerator = np.exp(-Di * beta)
            Pi = numerator / np.sum(numerator)
            Hi = -np.sum(Pi * np.log(Pi))

            Hdiff = Hi - desired_entropy

            if Hdiff > 0:
                betamin = beta
            else:
                betamax = beta

            tries += 1
        P[i] = Pi

    P = (P + P.T) / np.sum(P)  # Symmetrize
    P = P * 4  # Amplify probabilities

    # 2. Initialize low-dimensional embedding (Y)
    Y = np.random.randn(n_samples, n_components) * 0.0001

    # 3. Optimization (gradient descent)
    momentum = 0.5
    Y_old = np.zeros_like(Y)

    for t in range(n_iter):
        # Calculate low-dimensional affinities (q_ij)
        sum_Y = np.sum(np.square(Y), axis=1)
        num = -2. * np.dot(Y, Y.T)
        num = np.add(np.add(sum_Y, num).T, sum_Y)
        num = np.exp(num / 2)
        np.fill_diagonal(num, 0.)
        Q = num / np.sum(num)

        # Compute gradient
        pq_diff = P - Q

        sum_Y = np.sum(np.square(Y), axis=1)
        num = -2. * np.dot(Y, Y.T)
        num = np.add(np.add(sum_Y, num).T, sum_Y)
        num = 1 / (1 + np.exp(num / 2))
        np.fill_diagonal(num, 0.)

        grad = np.sum(pq_diff[:, np.newaxis,:] * (Y[np.newaxis,:,:] - Y[:, np.newaxis,:]) * num[:,:, np.newaxis], axis=1)

        # Update Y
        Y_new = Y + learning_rate * grad + momentum * Y_old
        Y_old = Y_new - Y
        Y = Y_new

        # Early exaggeration
        if t < 20:
            P = P * 4
        else:
            P = P / 4


        if t % 10 == 0:
            cost = np.sum(P * np.log(P / Q))
            print(f"Iteration {t}: Cost = {cost}")
            if np.isnan(cost):
                print("Cost is NaN. Stopping optimization.")
                return Y

    return Y


def test_tsne():
    # Create some sample data (e.g., from scikit-learn datasets)
    from sklearn.datasets import load_digits
    digits = load_digits()
    X = digits.data

    # Run t-SNE
    n_components = 2
    perplexity = 30
    n_iter = 500  # Increase iterations for better convergence
    Y = tsne(X, n_components=n_components, perplexity=perplexity, n_iter=n_iter)

    # Visualize the results
    plt.figure(figsize=(10, 8))
    plt.scatter(Y[:, 0], Y[:, 1], c=digits.target, cmap='viridis', s=10) # Color by digit
    plt.title("t-SNE Visualization of Digits")
    plt.colorbar(label="Digit")
    plt.show()


if __name__ == "__main__":
    test_tsne()