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

