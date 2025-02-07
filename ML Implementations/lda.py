import numpy as np
import pandas as pd

class LDA:
    """
    Linear Discriminant Analysis (LDA) implementation from scratch.
    """

    def __init__(self, n_components=None):
        """
        Initializes the LDA model.

        Args:
            n_components (int, optional): Number of components to keep after dimensionality reduction. 
                                          Defaults to None (n_classes - 1).
        """
        self.n_components = n_components
        self.weights = None  # Linear discriminant vectors (weights)
        self.classes = None  # Unique class labels

    def fit(self, X, y):
        """
        Fits the LDA model to the data.

        Args:
            X (NumPy array): Input data of shape (n_samples, n_features).
            y (NumPy array): Target labels of shape (n_samples,).
        """

        n_samples = X.shape[0]
        self.classes = np.unique(y)  # Extract unique class labels
        n_classes = len(self.classes)
        n_features = X.shape[1]

        # 1. Calculate class means:
        class_means = {}  # Dictionary to store mean of each class
        for c in self.classes:
            X_c = X[y == c]  # Select data points belonging to class c
            class_means[c] = np.mean(X_c, axis=0)  # Calculate mean along each feature

        # 2. Calculate Within-Class Scatter Matrix (S_W):
        S_W = np.zeros((n_features, n_features))  # Initialize S_W to zeros
        for c in self.classes:
            X_c = X[y == c]  # Select data points belonging to class c
            n_c = X_c.shape[0]  # Number of samples in class c
            S_W += np.cov(X_c, rowvar=False) * (n_c - 1)  # Add class-specific scatter matrix (unbiased)

        # 3. Calculate Between-Class Scatter Matrix (S_B):
        overall_mean = np.mean(X, axis=0)  # Calculate overall mean of all data points
        S_B = np.zeros((n_features, n_features))  # Initialize S_B to zeros
        for c in self.classes:
            n_c = X[y == c].shape[0]  # Number of samples in class c
            diff = (class_means[c] - overall_mean).reshape(-1, 1)  # Difference between class mean and overall mean (reshaped)
            S_B += n_c * np.dot(diff, diff.T)  # Add class-specific between-class scatter

        # 4. Calculate the Eigenvalues and Eigenvectors of inv(S_W) * S_B:
        # Use solve for numerical stability (avoids direct inverse calculation)
        eigenvalues, eigenvectors = np.linalg.eig(np.linalg.solve(S_W, S_B))

        # 5. Sort Eigenvalues in descending order:
        idx = np.argsort(eigenvalues)[::-1]  # Get indices for sorted eigenvalues (descending)
        eigenvalues = eigenvalues[idx]  # Sort eigenvalues
        eigenvectors = eigenvectors[:, idx]  # Sort eigenvectors according to sorted eigenvalues

        # 6. Select the top k Eigenvectors (k = n_components):
        if self.n_components is None:
            self.n_components = n_classes - 1  # Default: n_classes - 1
        self.weights = eigenvectors[:, :self.n_components]  # Select top n_components eigenvectors

    def transform(self, X):
        """
        Applies the learned transformation to the data.

        Args:
            X (NumPy array): Input data of shape (n_samples, n_features).

        Returns:
            NumPy array: Transformed data of shape (n_samples, n_components).
        
        Raises:
            RuntimeError: If the model hasn't been fitted yet.
        """
        if self.weights is None:
            raise RuntimeError("Model not fitted yet. Call fit() first.")
        return np.dot(X, self.weights)  # Project data onto the selected eigenvectors

    def fit_transform(self, X, y):
        """
        Fits the model and transforms the data in one step.

        Args:
            X (NumPy array): Input data.
            y (NumPy array): Target labels.

        Returns:
            NumPy array: Transformed data.
        """
        self.fit(X, y)  # Fit the model
        return self.transform(X)  # Transform the data


# Example Usage (with comments):
np.random.seed(0)  # For reproducibility
X = np.concatenate([np.random.normal(0, 1, (50, 2)), np.random.normal(3, 1.5, (50, 2))])  # Create sample data (2 classes)
y = np.concatenate([np.zeros(50), np.ones(50)])  # Create sample labels

lda = LDA(n_components=1)  # Create LDA object (reduce to 1 dimension)
X_transformed = lda.fit_transform(X, y)  # Fit and transform the data

print("Transformed data shape:", X_transformed.shape)

import matplotlib.pyplot as plt  # Import for plotting
plt.scatter(X_transformed, y)  # Create a scatter plot of transformed data
plt.xlabel("LDA Component 1")  # Label the x-axis
plt.ylabel("Class")  # Label the y-axis
plt.title("LDA Projection")  # Set the plot title
plt.show()  # Display the plot

# Example with Pandas DataFrame (with comments):
df = pd.DataFrame(X, columns=['feature1', 'feature2'])  # Create Pandas DataFrame
df['label'] = y  # Add labels to the DataFrame
X = df[['feature1', 'feature2']].values  # Extract features as NumPy array
y = df['label'].values  # Extract labels as NumPy array

lda = LDA(n_components=1)  # Create LDA object (reduce to 1 dimension)
X_transformed = lda.fit_transform(X, y)  # Fit and transform the data
print("Transformed data shape:", X_transformed.shape)  # Print shape of transformed data