from surprise import Dataset
from surprise import KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load the movielens-100k dataset (or any other dataset of your choice)
data = Dataset.load_builtin('ml-100k')

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.25)

# Use the user-based collaborative filtering algorithm (KNNBasic)
sim_options = {
    'name': 'cosine',  # Use cosine similarity
    'user_based': True  # Use user-based approach
}
knn_model = KNNBasic(sim_options=sim_options)

# Train the model on the training set
knn_model.fit(trainset)

# Make predictions on the test set
predictions = knn_model.test(testset)

# Evaluate the model
accuracy.rmse(predictions)

# Get recommendations for a specific user (replace 'user_id' with an actual user ID)
user_id = str(196)
user_items = set(data.df[data.df['user'] == user_id]['item'])
user_unrated_items = set(data.df['item']) - user_items

user_recommendations = []
for item_id in user_unrated_items:
    prediction = knn_model.predict(user_id, item_id)
    user_recommendations.append((item_id, prediction.est))

# Sort recommendations by predicted rating
user_recommendations = sorted(user_recommendations, key=lambda x: x[1], reverse=True)

# Print the top N recommendations
top_n = 5
print(f"Top {top_n} Recommendations for User {user_id}:")
for item_id, rating in user_recommendations[:top_n]:
    print(f"Item {item_id}: Predicted Rating = {rating}")



# ITEM-based

data = Dataset.load_builtin('ml-100k')

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.25)

# Use the item-based collaborative filtering algorithm (KNNBasic)
sim_options = {
    'name': 'cosine',  # Use cosine similarity
    'user_based': False  # Use item-based approach
}
knn_model = KNNBasic(sim_options=sim_options)

# Train the model on the training set
knn_model.fit(trainset)

# Make predictions on the test set
predictions = knn_model.test(testset)

# Evaluate the model
accuracy.rmse(predictions)

# Get recommendations for a specific user (replace 'user_id' with an actual user ID)
user_id = str(196)
user_items = set(data.df[data.df['user'] == user_id]['item'])
user_unrated_items = set(data.df['item']) - user_items

user_recommendations = []
for item_id in user_unrated_items:
    prediction = knn_model.predict(user_id, item_id)
    user_recommendations.append((item_id, prediction.est))

# Sort recommendations by predicted rating
user_recommendations = sorted(user_recommendations, key=lambda x: x[1], reverse=True)

# Print the top N recommendations
top_n = 5
print(f"Top {top_n} Recommendations for User {user_id}:")
for item_id, rating in user_recommendations[:top_n]:
    print(f"Item {item_id}: Predicted Rating = {rating}")