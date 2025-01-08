"""
Reading from a table
"""
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from sklearn.preprocessing import LabelEncoder
import torch
import torch.nn as nn

# Reading data from a CSV file
file_path = "data.csv"
data_table = pd.read_csv(file_path)

# Display first few rows
print(data_table.head())

"""
Reading from a json
[
    {"document_id": 1, "metric_1": 0.5, "metric_2": 3.2},
    {"document_id": 2, "metric_1": 0.8, "metric_2": 4.1}
]
"""

file_path = "data.json"
with open(file_path, "r") as file:
    data_json = json.load(file)
# Convert to a DataFrame for easier processing
data_table = pd.DataFrame(data_json)
# Display first few rows
print(data_table.head())

## DATA EXPLORATION

# Check for missing values
print(data_table.isnull().sum())
sns.heatmap(data_table.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()

# z scores for outliers
# Calculate z-scores
z_scores = data_table.select_dtypes(include="number").apply(zscore)
# Flag rows with z-scores > 3 as potential outliers
outliers = (z_scores.abs() > 3).any(axis=1)
print(f"Number of outliers: {outliers.sum()}")
# View outlier rows
print(data_table[outliers])

# Check data types
print(data_table.dtypes)
# Display summary statistics
print(data_table.describe())

# Plot histograms for numeric features
data_table.hist(figsize=(10, 8), bins=30)
plt.suptitle("Feature Distributions")
plt.show()

# Calculate and visualize correlation matrix
correlation_matrix = data_table.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.show()


# ONE-HOT ENCODING

# Example data
data = pd.DataFrame({
    "document_id": [1, 2, 3],
    "category": ["A", "B", "A"]
})

# One-hot encoding using pandas
encoded_data = pd.get_dummies(data, columns=["category"])
print(encoded_data)


# Example data
data = pd.DataFrame({
    "document_id": [1, 2, 3, 4, 5],
    "category": ["A", "B", "A", "C", "B"],
    "target": [0.5, 0.7, 0.8, 0.6, 0.9]
})

# LABEL ENCODING
"""
Label encoding is useful for ordinal categories or when
you want compact integer representations of the categorical data.
"""

# Example data
data = pd.DataFrame({
    "document_id": [1, 2, 3],
    "category": ["A", "B", "A"]
})

label_encoder = LabelEncoder()
data["category_encoded"] = label_encoder.fit_transform(data["category"])
print(data)

# EMBEDDING FOR HIGH CARDINALITY FEATURES
"""
Embeddings are ideal for categorical features with many unique values (e.g., user IDs, item IDs).
"""

# Example categories
categories = ["A", "B", "C", "A", "B", "C"]

# Map categories to indices
category_to_index = {cat: idx for idx, cat in enumerate(set(categories))}
indices = [category_to_index[cat] for cat in categories]

# Define embedding layer
num_categories = len(category_to_index)
embedding_dim = 4
embedding_layer = nn.Embedding(num_categories, embedding_dim)

# Convert indices to tensor
category_indices = torch.tensor(indices)

# Get embeddings
embeddings = embedding_layer(category_indices)
print(embeddings)

# TARGET ENCODING
"""
Target encoding replaces each category with the mean
(or another statistic) of the target variable for that category. It is common in recommendation systems.
"""
# Example data
data = pd.DataFrame({
    "document_id": [1, 2, 3, 4, 5],
    "category": ["A", "B", "A", "C", "B"],
    "target": [0.5, 0.7, 0.8, 0.6, 0.9]
})

# Calculate target mean for each category
target_mean = data.groupby("category")["target"].mean()
data["category_encoded"] = data["category"].map(target_mean)
print(data)

# Interaction feature
data["user_item_interaction"] = data["user_id"].astype(str) + "_" + data["item_id"].astype(str)
print(data)


# NUMERICAL

# Missing to Average


# Example data
data = pd.DataFrame({
    "feature_1": [1.2, 2.5, None, 4.3, 5.1]
})

# Replace missing values with the mean
data["feature_1_filled_mean"] = data["feature_1"].fillna(data["feature_1"].mean())
print(data)

# Normalization

from sklearn.preprocessing import MinMaxScaler

# Example data
data = pd.DataFrame({
    "feature_1": [1.2, 2.5, 3.6, 4.3, 5.1]
})

# Normalize feature to range 0-1
scaler = MinMaxScaler()
data["feature_1_normalized"] = scaler.fit_transform(data[["feature_1"]])
print(data)

# Standardization

from sklearn.preprocessing import StandardScaler

# Standardize feature
scaler = StandardScaler()
data["feature_1_standardized"] = scaler.fit_transform(data[["feature_1"]])
print(data)


# Bucketing

# Equal width bins
data["feature_1_binned"] = pd.cut(data["feature_1"], bins=3, labels=["Low", "Medium", "High"])
print(data)


# Equal frequency bins
data["feature_1_binned_quantiles"] = pd.qcut(data["feature_1"], q=3, labels=["Low", "Medium", "High"])
print(data)


# RECS

# Simulated user-item interaction data
data = pd.DataFrame({
    "user_id": [1, 1, 1, 2, 2, 3, 3, 3],
    "item_id": [101, 102, 103, 101, 104, 102, 103, 105],
    "rating": [4, 5, 3, 4, 2, 5, 1, 3]
})

# Simulated predictions (e.g., from a trained model)
data["predicted_rating"] = [4.2, 4.8, 2.9, 3.8, 2.3, 5.0, 1.5, 2.8]

from sklearn.metrics import mean_squared_error, mean_absolute_error

# Mean Squared Error (MSE)
mse = mean_squared_error(data["rating"], data["predicted_rating"])
print(f"Mean Squared Error (MSE): {mse:.3f}")

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")

# Mean Absolute Error (MAE)
mae = mean_absolute_error(data["rating"], data["predicted_rating"])
print(f"Mean Absolute Error (MAE): {mae:.3f}")

# Simulate top-K recommendations per user
top_k = 3
recommendations = data.sort_values(by=["user_id", "predicted_rating"], ascending=[True, False])
recommendations = recommendations.groupby("user_id").head(top_k)
print(recommendations)


# Precision@K and Recall@K
def precision_at_k(recommendations, k):
    precision_scores = []
    for user_id, group in recommendations.groupby("user_id"):
        relevant_items = group[group["rating"] >= 4]  # Define relevant items as those with true rating >= 4
        precision_scores.append(len(relevant_items) / k)
    return np.mean(precision_scores)

precision = precision_at_k(recommendations, top_k)
print(f"Precision@{top_k}: {precision:.3f}")

# NDCG
def ndcg_at_k(recommendations, k):
    ndcg_scores = []
    for user_id, group in recommendations.groupby("user_id"):
        relevance = group["rating"].values[:k]  # Take top-K true ratings
        gains = 2**relevance - 1
        discounts = np.log2(np.arange(2, len(relevance) + 2))
        dcg = np.sum(gains / discounts)
        ideal_gains = sorted(2**group["rating"], reverse=True)[:k]
        ideal_dcg = np.sum(ideal_gains / discounts)
        ndcg_scores.append(dcg / ideal_dcg if ideal_dcg > 0 else 0.0)
    return np.mean(ndcg_scores)

ndcg = ndcg_at_k(recommendations, top_k)
print(f"NDCG@{top_k}: {ndcg:.3f}")

# PYTORCH DNN for recs
"""
The network uses:

User Features: Information about users (e.g., age, preferences, etc.).
Item Features: Attributes of items (e.g., category, price, etc.).
Embedding Layers: For categorical features like user IDs and item IDs.
Fully Connected Layers: To combine user and item features and predict scores.
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Example data
data = pd.DataFrame({
    "user_id": [1, 1, 2, 2, 3, 3],
    "item_id": [101, 102, 101, 103, 102, 104],
    "user_feature": [0.5, 0.5, 0.8, 0.8, 0.3, 0.3],
    "item_feature": [0.7, 0.2, 0.7, 0.4, 0.2, 0.9],
    "score": [4.5, 3.0, 4.0, 2.5, 3.0, 5.0]
})

# Dataset class
class RecommendationDataset(Dataset):
    def __init__(self, df):
        self.user_ids = torch.tensor(df["user_id"].values, dtype=torch.long)
        self.item_ids = torch.tensor(df["item_id"].values, dtype=torch.long)
        self.user_features = torch.tensor(df["user_feature"].values, dtype=torch.float32)
        self.item_features = torch.tensor(df["item_feature"].values, dtype=torch.float32)
        self.scores = torch.tensor(df["score"].values, dtype=torch.float32)

    def __len__(self):
        return len(self.scores)

    def __getitem__(self, idx):
        return {
            "user_id": self.user_ids[idx],
            "item_id": self.item_ids[idx],
            "user_feature": self.user_features[idx],
            "item_feature": self.item_features[idx],
            "score": self.scores[idx]
        }

# Neural network with dropout and L1 regularization
class RecommendationModel(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim, hidden_dim, dropout_rate):
        super(RecommendationModel, self).__init__()
        # Embedding layers
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
        # Fully connected layers with dropout
        self.fc1 = nn.Linear(embedding_dim * 2 + 2, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, 1)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, user_id, item_id, user_feature, item_feature):
        user_emb = self.user_embedding(user_id)
        item_emb = self.item_embedding(item_id)
        # Concatenate embeddings and features
        x = torch.cat([user_emb, item_emb, user_feature.unsqueeze(1), item_feature.unsqueeze(1)], dim=1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x.squeeze()  # Return a single score per example

# Hyperparameters
num_users = data["user_id"].nunique()
num_items = data["item_id"].nunique()
embedding_dim = 8
hidden_dim = 16
dropout_rate = 0.3
learning_rate = 0.001
l1_lambda = 0.001
num_epochs = 20
batch_size = 2

# Prepare data
dataset = RecommendationDataset(data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Initialize model, loss, and optimizer
model = RecommendationModel(num_users=num_users + 1, num_items=num_items + 1,
                             embedding_dim=embedding_dim, hidden_dim=hidden_dim,
                             dropout_rate=dropout_rate)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop with L1 regularization
for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0.0
    for batch in dataloader:
        user_id = batch["user_id"]
        item_id = batch["item_id"]
        user_feature = batch["user_feature"]
        item_feature = batch["item_feature"]
        score = batch["score"]

        # Forward pass
        predictions = model(user_id, item_id, user_feature, item_feature)
        mse_loss = criterion(predictions, score)

        # L1 regularization
        l1_loss = sum(torch.sum(torch.abs(param)) for param in model.parameters())
        loss = mse_loss + l1_lambda * l1_loss

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {epoch_loss / len(dataloader):.4f}")

# Evaluation
model.eval()
true_scores = []
predicted_scores = []

for batch in dataloader:
    user_id = batch["user_id"]
    item_id = batch["item_id"]
    user_feature = batch["user_feature"]
    item_feature = batch["item_feature"]
    score = batch["score"]

    predictions = model(user_id, item_id, user_feature, item_feature)
    true_scores.extend(score.tolist())
    predicted_scores.extend(predictions.tolist())

# Calculate evaluation metrics
mse = mean_squared_error(true_scores, predicted_scores)
rmse = np.sqrt(mse)
mae = mean_absolute_error(true_scores, predicted_scores)

print(f"\nEvaluation Metrics:")
print(f"Mean Squared Error (MSE): {mse:.3f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")
print(f"Mean Absolute Error (MAE): {mae:.3f}")


# CATEGORICAL

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np

# Example data for classification
data = pd.DataFrame({
    "user_id": [1, 1, 2, 2, 3, 3],
    "item_id": [101, 102, 101, 103, 102, 104],
    "user_feature": [0.5, 0.5, 0.8, 0.8, 0.3, 0.3],
    "item_feature": [0.7, 0.2, 0.7, 0.4, 0.2, 0.9],
    "label": [1, 0, 1, 0, 0, 1]  # 1 = used, 0 = not used
})

# Dataset class
class RecommendationDataset(Dataset):
    def __init__(self, df):
        self.user_ids = torch.tensor(df["user_id"].values, dtype=torch.long)
        self.item_ids = torch.tensor(df["item_id"].values, dtype=torch.long)
        self.user_features = torch.tensor(df["user_feature"].values, dtype=torch.float32)
        self.item_features = torch.tensor(df["item_feature"].values, dtype=torch.float32)
        self.labels = torch.tensor(df["label"].values, dtype=torch.float32)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            "user_id": self.user_ids[idx],
            "item_id": self.item_ids[idx],
            "user_feature": self.user_features[idx],
            "item_feature": self.item_features[idx],
            "label": self.labels[idx]
        }

# Neural network for binary classification
class RecommendationModel(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim, hidden_dim, dropout_rate):
        super(RecommendationModel, self).__init__()
        # Embedding layers
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
        # Fully connected layers with dropout
        self.fc1 = nn.Linear(embedding_dim * 2 + 2, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, 1)  # Binary classification: output 1 logit
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout_rate)
        self.sigmoid = nn.Sigmoid()

    def forward(self, user_id, item_id, user_feature, item_feature):
        user_emb = self.user_embedding(user_id)
        item_emb = self.item_embedding(item_id)
        # Concatenate embeddings and features
        x = torch.cat([user_emb, item_emb, user_feature.unsqueeze(1), item_feature.unsqueeze(1)], dim=1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return self.sigmoid(x).squeeze()  # Return probabilities

# Hyperparameters
num_users = data["user_id"].nunique()
num_items = data["item_id"].nunique()
embedding_dim = 8
hidden_dim = 16
dropout_rate = 0.3
learning_rate = 0.001
l1_lambda = 0.001
num_epochs = 20
batch_size = 2

# Prepare data
dataset = RecommendationDataset(data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Initialize model, loss, and optimizer
model = RecommendationModel(num_users=num_users + 1, num_items=num_items + 1,
                             embedding_dim=embedding_dim, hidden_dim=hidden_dim,
                             dropout_rate=dropout_rate)
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss for classification
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop with L1 regularization
for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0.0
    for batch in dataloader:
        user_id = batch["user_id"]
        item_id = batch["item_id"]
        user_feature = batch["user_feature"]
        item_feature = batch["item_feature"]
        label = batch["label"]

        # Forward pass
        predictions = model(user_id, item_id, user_feature, item_feature)
        bce_loss = criterion(predictions, label)

        # L1 regularization
        l1_loss = sum(torch.sum(torch.abs(param)) for param in model.parameters())
        loss = bce_loss + l1_lambda * l1_loss

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {epoch_loss / len(dataloader):.4f}")

# Evaluation
model.eval()
true_labels = []
predicted_probs = []

for batch in dataloader:
    user_id = batch["user_id"]
    item_id = batch["item_id"]
    user_feature = batch["user_feature"]
    item_feature = batch["item_feature"]
    label = batch["label"]

    predictions = model(user_id, item_id, user_feature, item_feature)
    true_labels.extend(label.tolist())
    predicted_probs.extend(predictions.tolist())

# Convert probabilities to binary predictions
predicted_labels = [1 if prob >= 0.5 else 0 for prob in predicted_probs]

# Calculate evaluation metrics
accuracy = accuracy_score(true_labels, predicted_labels)
precision = precision_score(true_labels, predicted_labels)
recall = recall_score(true_labels, predicted_labels)
f1 = f1_score(true_labels, predicted_labels)

print("\nEvaluation Metrics:")
print(f"Accuracy: {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1-Score: {f1:.3f}")


# COLLABORATIVE FILTERING

"""
Input: The model uses a user ID and item ID as inputs.
Embeddings: Each user ID and item ID is mapped to dense vectors (embeddings).
Concatenation: User and item embeddings are concatenated and passed through a DNN.
Output: Predicts a score representing the interaction between the user and the item.
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import numpy as np
import pandas as pd

# Example user-item interaction data
interaction_data = pd.DataFrame({
    "user_id": [0, 0, 1, 1, 2, 2],
    "item_id": [0, 1, 0, 2, 1, 2],
    "interaction": [5, 3, 4, 2, 1, 5]  # Ratings or interaction scores
})

# Dataset class
class InteractionDataset(Dataset):
    def __init__(self, df):
        self.user_ids = torch.tensor(df["user_id"].values, dtype=torch.long)
        self.item_ids = torch.tensor(df["item_id"].values, dtype=torch.long)
        self.interactions = torch.tensor(df["interaction"].values, dtype=torch.float32)

    def __len__(self):
        return len(self.interactions)

    def __getitem__(self, idx):
        return {
            "user_id": self.user_ids[idx],
            "item_id": self.item_ids[idx],
            "interaction": self.interactions[idx]
        }

# Neural network for collaborative filtering
class CollaborativeFilteringModel(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim, hidden_dim):
        super(CollaborativeFilteringModel, self).__init__()
        # Embedding layers
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
        # Fully connected layers
        self.fc1 = nn.Linear(embedding_dim * 2, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim // 2)
        self.fc3 = nn.Linear(hidden_dim // 2, 1)  # Single score output
        self.relu = nn.ReLU()

    def forward(self, user_id, item_id):
        # Get embeddings
        user_emb = self.user_embedding(user_id)
        item_emb = self.item_embedding(item_id)
        # Concatenate embeddings
        x = torch.cat([user_emb, item_emb], dim=1)
        # Pass through fully connected layers
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x.squeeze()  # Return a single score per example

# Hyperparameters
num_users = interaction_data["user_id"].nunique()
num_items = interaction_data["item_id"].nunique()
embedding_dim = 8
hidden_dim = 16
learning_rate = 0.001
num_epochs = 20
batch_size = 2

# Prepare data
dataset = InteractionDataset(interaction_data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Initialize model, loss, and optimizer
model = CollaborativeFilteringModel(num_users=num_users, num_items=num_items,
                                     embedding_dim=embedding_dim, hidden_dim=hidden_dim)
criterion = nn.MSELoss()  # Loss for predicting interaction scores
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0.0
    for batch in dataloader:
        user_id = batch["user_id"]
        item_id = batch["item_id"]
        interaction = batch["interaction"]

        # Forward pass
        predictions = model(user_id, item_id)
        loss = criterion(predictions, interaction)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {epoch_loss / len(dataloader):.4f}")

# Example prediction for unseen user-item pairs
model.eval()
test_user_id = torch.tensor([0, 1, 2], dtype=torch.long)  # User IDs
test_item_id = torch.tensor([2, 1, 0], dtype=torch.long)  # Item IDs

predicted_scores = model(test_user_id, test_item_id)
print(f"Predicted Interaction Scores: {predicted_scores.detach().numpy()}")
