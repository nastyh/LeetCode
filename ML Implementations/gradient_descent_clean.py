import numpy as np
import matplotlib.pyplot as plt  # Import for plotting

class GradientDescent:
    def __init__(self, learning_rate=0.01, n_iters=1000, gradient_type='linear'):
        """
        Initializes the GradientDescent object.

        Args:
            learning_rate (float): Learning rate for the gradient descent algorithm.
            n_iters (int): Number of iterations to perform.
            gradient_type (str): Type of gradient to use. Either 'linear' or 'logistic'.
        """
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.gradient_type = gradient_type
        self.weights = None  # Weights (including bias)
        self.costs = None  # Cost values at each iteration

    def fit(self, X, y):
        """
        Fits the model using gradient descent.

        Args:
            X (NumPy array): Input data of shape (n_samples, n_features). Should *not* include a bias column.
            y (NumPy array): Target values of shape (n_samples,).

        Returns:
            self: Returns the fitted GradientDescent object.
        """
        n_samples, n_features = X.shape
        X_with_bias = np.c_[np.ones((n_samples, 1)), X]  # Add bias term
        self.weights = np.zeros(n_features + 1)  # Initialize weights
        self.costs = None

        for i in range(self.n_iters):
            if self.gradient_type == 'linear':
                y_pred = np.dot(X_with_bias, self.weights)
                error = y_pred - y
                gradient = (2/n_samples) * np.dot(X_with_bias.T, error)
                cost = (1/n_samples) * np.sum(error**2)
            elif self.gradient_type == 'logistic':
                z = np.dot(X_with_bias, self.weights)
                y_pred = self._sigmoid(z)  # Use the internal sigmoid function
                error = y_pred - y
                gradient = (1/n_samples) * np.dot(X_with_bias.T, error)
                cost = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
            else:
                raise ValueError("Invalid gradient_type. Choose 'linear' or 'logistic'.")

            self.weights = self.weights - self.learning_rate * gradient
            self.costs.append(cost)
        return self  # Allow chaining

    def predict(self, X):
        """
        Predicts the target values for the given input data.

        Args:
            X (NumPy array): Input data of shape (n_samples, n_features).

        Returns:
            NumPy array: Predicted target values.
        """
        X_with_bias = np.c_[np.ones((X.shape, 1)), X]  # Add bias term to input data
        if self.gradient_type == 'linear':
            return np.dot(X_with_bias, self.weights)
        elif self.gradient_type == 'logistic':
            z = np.dot(X_with_bias, self.weights)
            return self._sigmoid(z)
        else:
            raise ValueError("Invalid gradient_type. Choose 'linear' or 'logistic'.")

    def _sigmoid(self, z):  # Internal sigmoid function (private)
        """
        Sigmoid activation function.
        """
        return 1 / (1 + np.exp(-z))

    def plot_cost(self):
        """Plots the cost function over iterations."""
        if self.costs is None:
            raise RuntimeError("Model not fitted yet. Call fit() first.")
        plt.plot(self.costs)
        plt.xlabel("Iteration")
        plt.ylabel("Cost")
        plt.title("Cost Function vs. Iteration")
        plt.show()



# Example Usage (Linear Regression):
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])  # Sample data (no bias term)
y = np.array([2, 3, 4, 5])  # Sample target values

gd_linear = GradientDescent(learning_rate=0.01, n_iters=1000, gradient_type='linear')
gd_linear.fit(X, y) # fit the model
predictions = gd_linear.predict(X) # make predictions
print("Linear Regression Weights:", gd_linear.weights)
print("Linear Regression Final Cost:", gd_linear.costs[-1])
gd_linear.plot_cost() # plot the cost

# Example Usage (Logistic Regression):
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # Binary classification labels (0 or 1)

gd_logistic = GradientDescent(learning_rate=0.1, n_iters=5000, gradient_type='logistic')
gd_logistic.fit(X, y)
predictions = gd_logistic.predict(X)
print("Logistic Regression Weights:", gd_logistic.weights)
print("Logistic Regression Final Cost:", gd_logistic.costs[-1])
gd_logistic.plot_cost()