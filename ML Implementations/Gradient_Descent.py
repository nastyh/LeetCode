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
    
    def __init__(self):
        pass

    def train_gradient_descent(self, X, y, learning_rate=0.01, n_iters=100):
        """
        Trains a linear regression model using gradient descent
        """
        # Step 0: Initialize the parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(shape=(n_features,1))
        self.bias = 0
        costs = []

        for i in range(n_iters):
            # Step 1: Compute a linear combination of the input features and weights
            y_predict = np.dot(X, self.weights) + self.bias

            # Step 2: Compute cost over training set
            cost = (1 / n_samples) * np.sum((y_predict - y)**2)
            costs.append(cost)

            if i % 100 == 0:
                print(f"Cost at iteration {i}: {cost}")

            # Step 3: Compute the gradients
            dJ_dw = (2 / n_samples) * np.dot(X.T, (y_predict - y))  # wrt to coefficients w
            dJ_db = (2 / n_samples) * np.sum((y_predict - y))   # wrt to b, an intercept 
            
            # Step 4: Update the parameters
            self.weights = self.weights - learning_rate * dJ_dw
            self.bias = self.bias - learning_rate * dJ_db

        return self.weights, self.bias, costs

    def train_normal_equation(self, X, y):
        """
        Trains a linear regression model using the normal equation
        """
        self.weights = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
        self.bias = 0
        return self.weights, self.bias

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


regressor = LinearRegression()
w_trained, b_trained, costs = regressor.train_gradient_descent(X_train, y_train, learning_rate=0.005, n_iters=600)
