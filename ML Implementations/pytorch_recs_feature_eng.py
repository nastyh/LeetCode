import torch
import torch.nn as nn
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# RECS SYSTEM
"""
The RecSysModel returns the predicted interaction score (e.g., rating) between a user and an item.

Breakdown:
Input:

User IDs: Encoded embeddings for users.
Item IDs: Encoded embeddings for items.
User Features: Additional user-specific features (e.g., age, activity).
Item Features: Additional item-specific features (e.g., price, ratings).
Process:

Combines user embeddings with their features (user_embeds + user_feature_embeds).
Combines item embeddings with their features (item_embeds + item_feature_embeds).
Concatenates user and item combined representations.
Feeds the concatenated vector into a dense layer (output_layer) to predict the interaction score.
Output:

A single score (e.g., predicted rating or interaction likelihood) for each user-item pair.

If you input a user and an item with their respective features, the model will output a predicted rating,
which can be compared with the ground truth to compute loss during training or evaluation.
"""
# Sample Data
user_data = pd.DataFrame({
    'user_id': [1, 2, 3, 4],
    'age': [25, 30, 22, 40],
    'location': ['NY', 'CA', 'TX', 'NY'],
    'signup_days': [365, 200, 50, 100],
    'purchase_count': [10, 5, 2, 7]
})

item_data = pd.DataFrame({
    'item_id': [101, 102, 103, 104],
    'category': ['electronics', 'books', 'electronics', 'fashion'],
    'price': [100, 50, 150, 200],
    'discount': [10, 5, 20, 15],
    'rating': [4.5, 4.0, 3.8, 4.7]
})

interactions = pd.DataFrame({
    'user_id': [1, 1, 2, 3, 4],
    'item_id': [101, 102, 103, 101, 104],
    'rating': [5, 4, 3, 5, 2]
})

# Data Exploration Function
def explore_data(user_data, item_data, interactions):
    print("User Data Overview:\n", user_data.describe())
    print("\nItem Data Overview:\n", item_data.describe())
    print("\nInteractions Overview:\n", interactions.describe())
    print("\nUnique Users:", user_data['user_id'].nunique())
    print("Unique Items:", item_data['item_id'].nunique())

explore_data(user_data, item_data, interactions)

# Step 1: Encoding Categorical Features
user_location_encoder = LabelEncoder()
user_data['location_encoded'] = user_location_encoder.fit_transform(user_data['location'])

item_category_encoder = LabelEncoder()
item_data['category_encoded'] = item_category_encoder.fit_transform(item_data['category'])

# Step 2: Scaling Numerical Features
scaler = MinMaxScaler()
user_data[['age_scaled', 'signup_days_scaled', 'purchase_count_scaled']] = scaler.fit_transform(user_data[['age', 'signup_days', 'purchase_count']])
item_data[['price_scaled', 'discount_scaled', 'rating_scaled']] = scaler.fit_transform(item_data[['price', 'discount', 'rating']])

# Step 3: PyTorch Dataset for Recommendation System
class RecSysDataset(torch.utils.data.Dataset):
    def __init__(self, interactions, user_data, item_data):
        self.interactions = interactions
        self.user_data = user_data.set_index('user_id')
        self.item_data = item_data.set_index('item_id')

    def __len__(self):
        return len(self.interactions)

    def __getitem__(self, idx):
        interaction = self.interactions.iloc[idx]
        user_id = interaction['user_id']
        item_id = interaction['item_id']

        user_features = self.user_data.loc[user_id, ['location_encoded', 'age_scaled', 'signup_days_scaled', 'purchase_count_scaled']].values
        item_features = self.item_data.loc[item_id, ['category_encoded', 'price_scaled', 'discount_scaled', 'rating_scaled']].values

        rating = interaction['rating']

        return (
            torch.tensor(user_id, dtype=torch.long),
            torch.tensor(item_id, dtype=torch.long),
            torch.tensor(user_features, dtype=torch.float32),
            torch.tensor(item_features, dtype=torch.float32),
            torch.tensor(rating, dtype=torch.float32)
        )

# Create Dataset
recsys_dataset = RecSysDataset(interactions, user_data, item_data)
data_loader = torch.utils.data.DataLoader(recsys_dataset, batch_size=2, shuffle=True)

# Step 4: Define the Model
class RecSysModel(nn.Module):
    def __init__(self, num_users, num_items, embed_dim, user_feature_dim, item_feature_dim):
        super(RecSysModel, self).__init__()
        self.user_embedding = nn.Embedding(num_users, embed_dim)
        self.item_embedding = nn.Embedding(num_items, embed_dim)

        self.user_feature_layer = nn.Linear(user_feature_dim, embed_dim)
        self.item_feature_layer = nn.Linear(item_feature_dim, embed_dim)

        self.output_layer = nn.Linear(embed_dim * 2, 1)

    def forward(self, user_ids, item_ids, user_features, item_features):
        user_embeds = self.user_embedding(user_ids)
        item_embeds = self.item_embedding(item_ids)

        user_feature_embeds = self.user_feature_layer(user_features)
        item_feature_embeds = self.item_feature_layer(item_features)

        user_combined = user_embeds + user_feature_embeds
        item_combined = item_embeds + item_feature_embeds

        interaction = torch.cat([user_combined, item_combined], dim=1)
        output = self.output_layer(interaction)

        return output

# Step 5: Initialize Model
num_users = user_data['user_id'].nunique()
num_items = item_data['item_id'].nunique()
user_feature_dim = 4  # location_encoded + age_scaled + signup_days_scaled + purchase_count_scaled
item_feature_dim = 4  # category_encoded + price_scaled + discount_scaled + rating_scaled
embed_dim = 8

model = RecSysModel(num_users + 1, num_items + 1, embed_dim, user_feature_dim, item_feature_dim)

# Step 6: Training Loop
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(5):
    for batch in data_loader:
        user_ids, item_ids, user_features, item_features, ratings = batch

        # Forward Pass
        predictions = model(user_ids, item_ids, user_features, item_features).squeeze()
        loss = criterion(predictions, ratings)

        # Backward Pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# Evaluation Step
def evaluate_model(model, data_loader):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for batch in data_loader:
            user_ids, item_ids, user_features, item_features, ratings = batch
            predictions = model(user_ids, item_ids, user_features, item_features).squeeze()
            loss = criterion(predictions, ratings)
            total_loss += loss.item()
    print(f"Evaluation Loss: {total_loss / len(data_loader):.4f}")

evaluate_model(model, data_loader)
