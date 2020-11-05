import numpy as np
"""
Initialize the values of weights W0 and W1
Find the predictions y_hat = W0 + W1 for all x
Calculated the error values (y_hat - Y) and the MSE
Update the weights per a gradient descent rule
Repeat steps 2-4
"""
x = np.array([1, 3, 5])
y = np.array([5, 12, 18])

W0_new = 0
W1_new = 0
a == 0.04  # learning rate; chose just randomly
MSE = np.array([])  # we will collect the MSE values here 

n_iter = 11  # how many times we will iterate. Chosen randomly for now
for i in range(n_iter):
    y_pred = np.array([])  # this is y_hat
    error = np.array([])  # errors per iterations: (y_hat - y)
    error_x = np.array([])  # (y_hat - y)X term for the update rule

    W0 = W0_new
    W1 = W1_new

    for i in x:
        y_pred = np.append(y_pred, (W0 + W1 * i))  # y_hat = W0 + W1 * x1
        
    error = np.append(error, y_pred - y)  # error for every sample
    errox_x = np.append(error_x, error * x)
    MSE_val = (error**2).mean()
    MSE = np.append(MSE, MSE_val)

    W0_new = W0 - a * np.sum(error)  # updating 
    W1_new = W1 - a * np.sum(error_x)  # updating


class LinearRegression:
    def __init__(self, learning_rate = 1e-3, max_iters = 250):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None

    def fit(self, X_train, y_train):
        X_train = self._fit_intercept(X_train)
        self.weights = np.random.rand(X_train.shape[1])

        for iter in range(self.max_iters):
            self.weights = self.weights - self.learning_rate * \
                self._grad(X_train, y_train, self.weights)
            cost = self._cost(X_train, y_train, self.weights)
            print_result(iter, cost)

    def predict(self, X_predict):
        """ This method predicts responses for new data.

        This method will be used for end-users to predict responses
        for future data.

        Arguments:
            X_predict: new data

        Returns: a vector of responses            
        """
        return X_predict @ self.weights

    @staticmethod
    def _cost(X_train, y_train, weights):
        """Calculates the cost w.r.t. weights

        This helper method calculates the cost w.r.t. weights

        Arguments:
            X_train: training features
            y_train: training labels.
            weights: weights vector of the model
        
        Returns: scalar value which represents the cost
        """
        dif = (y_train - X_train @ weights)
        return (dif.T @ dif) / X_train.shape[0]

    @staticmethod
    def _fit_intercept(X_train):
        """Add the intercepting term to the training dataset

        This simple helper method adds the intercepting term to the 
        training dataset.

        Arguments:
            X_train: training dataset

        Returns: training dataset with the interceptor
        """
        return np.column_stack((np.ones(X_train.shape[0]), X_train))

    @staticmethod
    def _grad(X_train, y_train, weights):
        """Calculates the gradient of the cost function w.r.t. weight vector

        This methods calculated the gradient of the cost function w.r.t. 
        weight vector.

        Arguments:
            X_train: training features
            y_train: training labels.
            weights: weights vector of the model
        
        Returns: scalar value which represents the cost
        """
        return 2 * (X_train.T @ (X_train @ weights - y_train)) / X_train.shape[0]

