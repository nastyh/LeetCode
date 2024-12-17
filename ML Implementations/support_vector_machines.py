import numpy as np

class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        """
        binary classification

        """
        self.lr = learning_rate
        self.lambda_param = lambda_param  # regularization term to prevent overfitting
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X, y):
        """
        X: samples, features
        Y: -1 or 1
        """
        n_samples, n_features = X.shape

        # Convert labels to -1 and 1 for binary classification
        y_ = np.where(y <= 0, -1, 1)

        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                # Calculate the margin violation condition
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition: # Margin violation, update with full loss term
                    # only update with a regularization term to prevent overfitting.
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    # update with a full loss term that includes both the regularization
                    # and the misclassification penalty.
                    self.w -= self.lr * (
                        2 * self.lambda_param * self.w - np.dot(x_i, y_[idx])
                    )
                    self.b -= self.lr * y_[idx]

    def predict(self, X):
        """
        X is new data in the same shape of samples, features 
        """
        approx = np.dot(X, self.w) - self.b
        return np.sign(approx) # # Predict class based on the sign of the approximation
