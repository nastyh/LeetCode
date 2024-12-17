class LinearRegression:
    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        # gradient descent
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            # compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))  # error in our current prediction
            # Multiplying this difference with X.T essentially distributes the error across each weight
            # in the model according to how much that weight contributed to the prediction
            # Dividing by n_samples (number of data points) normalizes the gradient
            # for an average update across all samples.
            # dot product b/c calculate the gradient for all weights in a single operation.
            # The dot product ensures that each weight is updated based on its contribution to the error.
            db = (1 / n_samples) * np.sum(y_predicted - y) # calculates the sum of the difference between
            # the predicted values (y_predicted) and the actual target values (y) across all data points.
            # np.sum() sums up the errors for all data points.

            # update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        y_approximated = np.dot(X, self.weights) + self.bias
        return y_approximated
    

    

    