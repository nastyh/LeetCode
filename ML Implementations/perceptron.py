import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=100):
        """Initializes the perceptron."""
        self.learning_rate = learning_rate
        self.epochs = epochs

    def fit(self, X, y):
        """Trains the perceptron."""
        self.weights = np.zeros(X.shape[1] + 1)  # +1 for bias

        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update

    def predict(self, X):
        """Makes predictions."""
        activation = np.dot(X, self.weights[1:]) + self.weights[0]
        return 1 if activation > 0 else 0

# Example usage
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # AND gate

perceptron = Perceptron()
perceptron.fit(X, y)

print("Predictions:", [perceptron.predict(x) for x in X])