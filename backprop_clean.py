import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        """
        Initializes the neural network parameters with random weights and zero biases.
        
        Args:
            input_size (int): Number of input neurons.
            hidden_size (int): Number of neurons in the hidden layer.
            output_size (int): Number of output neurons.
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Xavier/Glorot initialization for weights (helps with better convergence)
        limit_hidden = np.sqrt(6.0 / (input_size + hidden_size))
        self.weights1 = np.random.uniform(-limit_hidden, limit_hidden, (hidden_size, input_size))
        self.bias1 = np.zeros((hidden_size, 1))

        limit_output = np.sqrt(6.0 / (hidden_size + output_size))
        self.weights2 = np.random.uniform(-limit_output, limit_output, (output_size, hidden_size))
        self.bias2 = np.zeros((output_size, 1))

    def _sigmoid(self, z):
        """
        Sigmoid activation function.

        Args:
            z (NumPy array): Input values.

        Returns:
            NumPy array: Sigmoid activations.
        """
        return 1 / (1 + np.exp(-z))

    def _sigmoid_derivative(self, a):
        """
        Derivative of the sigmoid function.

        Args:
            a (NumPy array): Sigmoid activations.

        Returns:
            NumPy array: Derivative of sigmoid at each point.
        """
        return a * (1 - a)

    def forward(self, X):
        """
        Performs forward propagation through the network.

        Args:
            X (NumPy array): Input data of shape (n_samples, input_size).

        Returns:
            tuple: (z1, a1, z2, a2) values from the hidden and output layers.
        """
        # Calculate hidden layer activations
        z1 = np.dot(self.weights1, X.T) + self.bias1  # Weighted sum at hidden layer
        a1 = self._sigmoid(z1)  # Activation at hidden layer

        # Calculate output layer activations
        z2 = np.dot(self.weights2, a1) + self.bias2  # Weighted sum at output layer
        a2 = self._sigmoid(z2)  # Activation at output layer (predictions)

        return z1, a1, z2, a2

    def backward(self, X, y, z1, a1, z2, a2, learning_rate):
        """
        Performs backpropagation to update weights and biases.

        Args:
            X (NumPy array): Input data of shape (n_samples, input_size).
            y (NumPy array): True target values.
            z1, a1, z2, a2: Forward pass values.
            learning_rate (float): Learning rate for parameter updates.
        """
        m = X.shape[0]  # Number of samples

        # Calculate the error at the output layer
        dz2 = a2 - y.T  # Error in output layer
        dw2 = (1 / m) * np.dot(dz2, a1.T)  # Gradient of weights between hidden and output layers
        db2 = (1 / m) * np.sum(dz2, axis=1, keepdims=True)  # Gradient of output biases

        # Calculate the error at the hidden layer
        dz1 = np.dot(self.weights2.T, dz2) * self._sigmoid_derivative(a1)  # Error in hidden layer
       
