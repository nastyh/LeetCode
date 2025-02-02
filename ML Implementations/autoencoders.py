import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# FROM SCRATCH


import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def autoencoder(X, encoding_dim, epochs=1000, learning_rate=0.1):
    n_samples, input_dim = X.shape

    # Initialize weights (randomly)
    weights1 = np.random.randn(input_dim, encoding_dim) * 0.01  # Weights for encoder
    weights2 = np.random.randn(encoding_dim, input_dim) * 0.01  # Weights for decoder
    biases1 = np.zeros((1, encoding_dim))
    biases2 = np.zeros((1, input_dim))


    for epoch in range(epochs):
        # Forward pass
        encoded = sigmoid(np.dot(X, weights1) + biases1)
        decoded = sigmoid(np.dot(encoded, weights2) + biases2)

        # Backward pass (manual gradient calculation - simplified)
        error = X - decoded
        output_delta = error * sigmoid_derivative(decoded)
        hidden_delta = output_delta.dot(weights2.T) * sigmoid_derivative(encoded)

        # Update weights (gradient descent)
        weights2 += encoded.T.dot(output_delta) * learning_rate
        weights1 += X.T.dot(hidden_delta) * learning_rate
        biases2 += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        biases1 += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

        if epoch % 100 == 0:
            loss = np.mean(np.square(error))
            print(f"Epoch {epoch}, Loss: {loss}")

    return weights1, weights2, biases1, biases2


def test_autoencoder():
    # Sample Data (replace with your data)
    X = np.random.rand(100, 784)  # Example: 100 samples, 784 features (like flattened MNIST images)

    encoding_dim = 128
    weights1, weights2, biases1, biases2 = autoencoder(X, encoding_dim, epochs=2000, learning_rate=.5)

    # Reconstruction (example)
    encoded_data = sigmoid(np.dot(X, weights1) + biases1)
    reconstructed_data = sigmoid(np.dot(encoded_data, weights2) + biases2)

    # Evaluate (visual inspection - compare X and reconstructed_data)
    n = 10  # How many digits we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # Display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(X[i].reshape(28, 28)) # Assuming 784 is a flattened 28x28 image
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(reconstructed_data[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()


if __name__ == "__main__":
    test_autoencoder()


# TENSOR FLOW AND KERAS
def autoencoder(input_dim, encoding_dim):
    """
    Builds a simple autoencoder model using TensorFlow/Keras.

    Args:
        input_dim: The dimensionality of the input data.
        encoding_dim: The dimensionality of the encoded representation.

    Returns:
        A tuple containing the encoder model and the autoencoder model.
    """

    # Encoder
    input_layer = tf.keras.layers.Input(shape=(input_dim,))
    encoded = tf.keras.layers.Dense(encoding_dim, activation='relu')(input_layer)  # You can experiment with different activations

    # Decoder
    decoded = tf.keras.layers.Dense(input_dim, activation='sigmoid')(encoded) # Output should be same size as input, sigmoid for pixel values

    # Autoencoder model
    autoencoder = tf.keras.Model(input_layer, decoded)

    # Compile the autoencoder
    autoencoder.compile(optimizer='adam', loss='mse')  # Mean Squared Error is common for autoencoders

    # Encoder model (to get the encoded representation separately)
    encoder = tf.keras.Model(input_layer, encoded)

    return encoder, autoencoder



def test_autoencoder():
    # Load a dataset (e.g., MNIST)
    (x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()  # We only need the images

    # Preprocess the data
    x_train = x_train.astype('float32') / 255.0  # Normalize pixel values to
    x_test = x_test.astype('float32') / 255.0
    x_train = x_train.reshape(len(x_train), np.prod(x_train.shape[1:])) # Flatten images
    x_test = x_test.reshape(len(x_test), np.prod(x_test.shape[1:]))

    input_dim = x_train.shape
    encoding_dim = 128  # Size of the bottleneck layer

    # Build the autoencoder
    encoder, autoencoder = autoencoder(input_dim, encoding_dim)

    # Train the autoencoder
    autoencoder.fit(x_train, x_train, epochs=10, batch_size=256, shuffle=True, validation_data=(x_test, x_test))

    # Example: Encode and decode some test images
    decoded_imgs = autoencoder.predict(x_test)

    # Visualize some results
    n = 10  # How many digits we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # Display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(x_test[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(decoded_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()


if __name__ == "__main__":
    test_autoencoder()