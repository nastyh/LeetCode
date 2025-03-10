"""
Concept is the same as with a regression tree: need to choose a feature and an optimal threshold for this feature to split on
However, how to calculate losses for left and right regions?
The algo selects the split that produces the purest substets normalized by their size. 
L(D, theta) = n_left / n_total * Gini_left + n_right / n_total * Gini_right
where 
D - remaining training examples
theta - feature and feature threshold
n_left, n_right - number of samples in the left and right subsets
Gini_left, Gini_right -- Gini indices for the left and right subsets
Repeat till a stopping criteria is reached

Gini index = 1 - sum(p_k_m)^2
p_k _m- fraction of training examples with class k among all training examples in node m
"""

class DecisionTree:
    """
    Decision tree for classification
    """

    def __init__(self):
        self.root_dict = None
        self.tree_dict = None

    def split_dataset(self, X, y, feature_idx, threshold):
        """
        Splits dataset X into two subsets, according to a given feature
        and feature threshold.

        Args:
            X: 2D numpy array with data samples
            y: 1D numpy array with labels
            feature_idx: int, index of feature used for splitting the data
            threshold: float, threshold used for splitting the data

        Returns:
            splits: dict containing the left and right subsets
            and their labels
        """

        left_idx = np.where(X[:, feature_idx] < threshold)
        right_idx = np.where(X[:, feature_idx] >= threshold)

        left_subset = X[left_idx]
        y_left = y[left_idx]

        right_subset = X[right_idx]
        y_right = y[right_idx]

        splits = {
        'left': left_subset,
        'y_left': y_left,
        'right': right_subset,
        'y_right': y_right,
        }

        return splits

    def gini_impurity(self, y_left, y_right, n_left, n_right):
        """
        Computes Gini impurity of a split.

        Args:
            y_left, y_right: target values of samples in left/right subset
            n_left, n_right: number of samples in left/right subset

        Returns:
            gini_left: float, Gini impurity of left subset
            gini_right: gloat, Gini impurity of right subset
        """

        n_total = n_left + n_left

        score_left, score_right = 0, 0
        gini_left, gini_right = 0, 0

        if n_left != 0:
            for c in range(self.n_classes):
                # For each class c, compute fraction of samples with class c
                p_left = len(np.where(y_left == c)[0]) / n_left
                score_left += p_left * p_left
            gini_left = 1 - score_left

        if n_right != 0:
            for c in range(self.n_classes):
                p_right = len(np.where(y_right == c)[0]) / n_right
                score_right += p_right * p_right
            gini_right = 1 - score_right

        return gini_left, gini_right

    def entropy(y):
        """Calculates the entropy of a label array."""
        unique, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        entropy = -np.sum(probabilities * np.log2(probabilities))
        return entropy
    
    def information_gain(y, y_left, y_right):
        """Calculates the information gain of a split."""
        n = len(y)
        n_left = len(y_left)
        n_right = len(y_right)
    
        if n_left == 0 or n_right == 0:  # Handle edge case where a split results in empty subset
          return 0
    
        parent_entropy = entropy(y)
        weighted_child_entropy = (n_left / n) * entropy(y_left) + (n_right / n) * entropy(y_right)
        information_gain = parent_entropy - weighted_child_entropy
        return information_gain
    
    
    def gini_index(y):
        """Calculates the Gini impurity of a label array."""
        unique, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        gini = 1 - np.sum(probabilities**2)
        return gini
    
    def gini_gain(y, y_left, y_right):
        """Calculates the Gini gain of a split."""
        n = len(y)
        n_left = len(y_left)
        n_right = len(y_right)
    
        if n_left == 0 or n_right == 0: # Handle edge case where a split results in empty subset
          return 0
        
        parent_gini = gini_index(y)
        weighted_child_gini = (n_left / n) * gini_index(y_left) + (n_right / n) * gini_index(y_right)
        gini_gain = parent_gini - weighted_child_gini
        return gini_gain

    def get_cost(self, splits):
        """
        Computes cost of a split given the Gini impurity of
        the left and right subset and the sizes of the subsets
        
        Args:
            splits: dict, containing params of current split
        """
        y_left = splits['y_left']
        y_right = splits['y_right']

        n_left = len(y_left)
        n_right = len(y_right)
        n_total = n_left + n_right

        gini_left, gini_right = self.gini_impurity(y_left, y_right, n_left, n_right)
        cost = (n_left / n_total) * gini_left + (n_right / n_total) * gini_right

        return cost

    def find_best_split(self, X, y):
        """
        Finds the best feature and feature index to split dataset X into
        two groups. Checks every value of every attribute as a candidate
        split.

        Args:
            X: 2D numpy array with data samples
            y: 1D numpy array with labels

        Returns:
            best_split_params: dict, containing parameters of the best split
        """

        n_samples, n_features = X.shape

        best_feature_idx, best_threshold, best_cost, best_splits = np.inf, np.inf, np.inf, None

        for feature_idx in range(n_features):
            for i in range(n_samples):
                current_sample = X[i]
                threshold = current_sample[feature_idx]
                splits = self.split_dataset(X, y, feature_idx, threshold)
                cost = self.get_cost(splits)

                if cost < best_cost:
                    best_feature_idx = feature_idx
                    best_threshold = threshold
                    best_cost = cost
                    best_splits = splits

        best_split_params = {
            'feature_idx': best_feature_idx,
            'threshold': best_threshold,
            'cost': best_cost,
            'left': best_splits['left'],
            'y_left': best_splits['y_left'],
            'right': best_splits['right'],
            'y_right': best_splits['y_right'],
        }

        return best_split_params


    def build_tree(self, node_dict, depth, max_depth, min_samples):
        """
        Builds the decision tree in a recursive fashion.

        Args:
            node_dict: dict, representing the current node
            depth: int, depth of current node in the tree
            max_depth: int, maximum allowed tree depth
            min_samples: int, minimum number of samples needed to split a node further

        Returns:
            node_dict: dict, representing the full subtree originating from current node
        """
        left_samples = node_dict['left']
        right_samples = node_dict['right']
        y_left_samples = node_dict['y_left']
        y_right_samples = node_dict['y_right']

        if len(y_left_samples) == 0 or len(y_right_samples) == 0:
            node_dict["left_child"] = node_dict["right_child"] = self.create_terminal_node(np.append(y_left_samples, y_right_samples))
            return None

        if depth >= max_depth:
            node_dict["left_child"] = self.create_terminal_node(y_left_samples)
            node_dict["right_child"] = self.create_terminal_node(y_right_samples)
            return None

        if len(right_samples) < min_samples:
            node_dict["right_child"] = self.create_terminal_node(y_right_samples)
        else:
            node_dict["right_child"] = self.find_best_split(right_samples, y_right_samples)
            self.build_tree(node_dict["right_child"], depth+1, max_depth, min_samples)

        if len(left_samples) < min_samples:
            node_dict["left_child"] = self.create_terminal_node(y_left_samples)
        else:
            node_dict["left_child"] = self.find_best_split(left_samples, y_left_samples)
            self.build_tree(node_dict["left_child"], depth+1, max_depth, min_samples)

        return node_dict

    def create_terminal_node(self, y):
        """
        Creates a terminal node.
        Given a set of labels the most common label is computed and
        set as the classification value of the node.

        Args:
            y: 1D numpy array with labels
        Returns:
            classification: int, predicted class
        """
        classification = max(set(y), key=list(y).count)
        return classification

    def train(self, X, y, max_depth, min_samples):
        """
        Fits decision tree on a given dataset.

        Args:
            X: 2D numpy array with data samples
            y: 1D numpy array with labels
            max_depth: int, maximum allowed tree depth
            min_samples: int, minimum number of samples needed to split a node further
        """
        self.n_classes = len(set(y))
        self.root_dict = self.find_best_split(X, y)
        self.tree_dict = self.build_tree(self.root_dict, 1, max_depth, min_samples)

    def predict(self, X, node):
        """
        Predicts the class for a given input example X.

        Args:
            X: 1D numpy array, input example
            node: dict, representing trained decision tree

        Returns:
            prediction: int, predicted class
        """
        feature_idx = node['feature_idx']
        threshold = node['threshold']

        if X[feature_idx] < threshold:
            if isinstance(node['left_child'], (int, np.integer)):
                return node['left_child']
            else:
                prediction = self.predict(X, node['left_child'])
        elif X[feature_idx] >= threshold:
            if isinstance(node['right_child'], (int, np.integer)):
                return node['right_child']
            else:
                prediction = self.predict(X, node['right_child'])

        return prediction
