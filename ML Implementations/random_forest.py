import numpy as np
import pandas as pd
from collections import Counter

class DecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def _entropy(self, y):
        counts = np.bincount(y)  # Efficiently count class occurrences
        probabilities = counts[np.nonzero(counts)] / len(y) # Avoid division by zero if a class is absent
        return -np.sum(probabilities * np.log2(probabilities)) if len(probabilities) > 0 else 0 # Handle empty y case

    def _information_gain(self, X, y, split_feature):
        parent_entropy = self._entropy(y)
        unique_values = np.unique(X[:, split_feature])
        weighted_child_entropy = 0

        for value in unique_values:
            indices = X[:, split_feature] == value
            y_subset = y[indices]
            weight = len(y_subset) / len(y)
            weighted_child_entropy += weight * self._entropy(y_subset)

        return parent_entropy - weighted_child_entropy

    def _best_split(self, X, y):
        best_gain = -1
        best_feature = None

        for feature in range(X.shape):
            gain = self._information_gain(X, y, feature)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature

        return best_feature

    def _build_tree(self, X, y, depth):
        if depth == self.max_depth or len(y) < self.min_samples_split or len(np.unique(y)) == 1: #Added early stopping
            return Counter(y).most_common(1)  # Leaf node: most common class

        best_feature = self._best_split(X, y)
        if best_feature is None: # Handle cases where no split improves information gain
            return Counter(y).most_common(1)

        tree = {}
        unique_values = np.unique(X[:, best_feature])
        for value in unique_values:
            indices = X[:, best_feature] == value
            X_subset = X[indices]
            y_subset = y[indices]
            tree[value] = self._build_tree(X_subset, y_subset, depth + 1)
        return tree


    def fit(self, X, y):
        self.tree = self._build_tree(X, y, 0)

    def _predict_one(self, x, tree):
        for feature_value, subtree in tree.items():
            if x == feature_value: # Only works for categorical features in this version
                if isinstance(subtree, dict):
                    return self._predict_one(x[1:], subtree) # Navigate deeper into the tree
                else:
                    return subtree # Leaf node: return prediction
        return list(tree.values()) if len(tree) > 0 else None # Handle missing branch case (return majority class of the parent or None)

    def predict(self, X):
        predictions = []
        for x in X:
          predictions.append(self._predict_one(x, self.tree))
        return np.array(predictions)



class RandomForest:
    def __init__(self, n_estimators=100, max_depth=None, min_samples_split=2, max_features = None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.trees = []

    def fit(self, X, y):
        n_samples = X.shape
        n_features = X.shape

        for _ in range(self.n_estimators):
            # Bootstrap sampling (randomly sample with replacement)
            sample_indices = np.random.choice(n_samples, n_samples, replace=True)
            X_sample = X[sample_indices]
            y_sample = y[sample_indices]

            # Feature bagging (randomly select a subset of features)
            if self.max_features is None:
                n_features_to_use = n_features
            elif isinstance(self.max_features, int):
                 n_features_to_use = min(self.max_features, n_features) # Handle cases where max_features > n_features
            elif isinstance(self.max_features, float):
                n_features_to_use = int(self.max_features * n_features)
            else:
                raise ValueError("max_features must be None, int or float")

            feature_indices = np.random.choice(n_features, n_features_to_use, replace=False)
            X_sample = X_sample[:, feature_indices]

            tree = DecisionTree(max_depth=self.max_depth, min_samples_split=self.min_samples_split)
            tree.fit(X_sample, y_sample)
            self.trees.append((tree, feature_indices)) # Store the tree and the used features

    def predict(self, X):
        predictions = []
        for x in X:
            tree_predictions = []
            for tree, feature_indices in self.trees:
                x_subset = x[feature_indices] # Apply the same feature selection as for training
                tree_predictions.append(tree._predict_one(x_subset.reshape(1,-1), tree)) # Reshape to (1, -1) to make it work with the _predict_one method
            # Handle potential None predictions (if a tree couldn't make a decision)
            valid_predictions = [p for p in tree_predictions if p is not None]
            if valid_predictions:
                predictions.append(Counter(valid_predictions).most_common(1))
            else:
                predictions.append(None) # Or handle in another way, like returning the most frequent class from training data
        return np.array(predictions)