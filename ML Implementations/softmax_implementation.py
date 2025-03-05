"""
function that computes the softmax of a vector, ensuring numerical stability
converts a vector of real numbers into a probability distribution
used in multi-class classification problems 
softmax(x)_i = (e^x_i) / sum_j_to_K(e^x_j)
x is the input vector, x_i -- i-th element of the vector
K is the number of elements in this vector

Not numerical stable, since e^x can become very large --> overflow
instead subtract the max val of the input vector from each element before 
exponentiations
largest exponent, thus, will be 0, no overflow 
"""

import numpy as np

def softmax(x):
    """Computes the softmax function in a numerically stable way."""
    e_x = np.exp(x - np.max(x))  # Subtract max for stability
    return e_x / e_x.sum(axis=0)

# Example usage
x = np.array([2.0, 1.0, 0.1])
softmax_result = softmax(x)
print("Softmax:", softmax_result)

# Example with larger values, demonstrating numerical stability
x_large = np.array([1000, 999, 998])
softmax_large_result = softmax(x_large)
print("Softmax (large values):", softmax_large_result)

# Example with negative values.
x_negative = np.array([-1, -2, -3])
softmax_negative_result = softmax(x_negative)
print("Softmax (negative values):", softmax_negative_result)

#Example with zeros.
x_zeros = np.array([0,0,0])
softmax_zeros_result = softmax(x_zeros)
print("Softmax (zeros):", softmax_zeros_result)