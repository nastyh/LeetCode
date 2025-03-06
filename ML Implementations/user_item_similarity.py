"""
Question: “Given a dataset of user-item ratings, implement a collaborative filtering algorithm to predict a user’s
rating for an unseen item using user-to-user cosine similarity.”
Follow-up: “How do you handle users with no common rated items?”
"""
import math
import numpy as np

def user_user_collaborative_filtering(ratings, user_id, item_id, k=3):
    """
    Predicts a user's rating for an unseen item using user-to-user collaborative filtering.

    Args:
        ratings (numpy.ndarray): User-item ratings matrix (users x items).
        user_id (int): The ID of the user for whom to predict the rating.
        item_id (int): The ID of the item for which to predict the rating.
        k (int): The number of nearest neighbors to consider.

    Returns:
        float: The predicted rating.
        Returns None if user or item ID is out of bounds.
    """
    num_users, num_items = ratings.shape

    if user_id < 0 or user_id >= num_users or item_id < 0 or item_id >= num_items:
        return None  # User or item ID out of bounds

    user_ratings = ratings[user_id, :]

    # Find users who have rated the target item
    similar_users = []
    for other_user_id in range(num_users):
        if other_user_id != user_id and ratings[other_user_id, item_id] != 0:
            similar_users.append(other_user_id)
    """
    If, after calculating similarities, there are neighbors,
    but all of their similarities are zero, it means that while
    they've rated the target item, they have no overlapping ratings with the user.

    In this edge case, and in the case where no users have rated the item:
    If the target user has any ratings, the mean of the target users ratings is returned.
    If the target user has no ratings, the mean of all ratings in the ratings matrix is returned.
    If the ratings matrix is empty, 0 is returned.

    Performs well with sparse data, as it only considers co-rated items.
    nsensitive to differences in rating scale or magnitude. It focuses on the angle between vectors.
    Captures the overall preference pattern between users.
    """
    if not similar_users:
        return np.mean(ratings[user_id, ratings[user_id,:]!=0]) if np.any(ratings[user_id, ratings[user_id,:]!=0]) else np.mean(ratings[ratings!=0]) if np.any(ratings[ratings!=0]) else 0 #Handle case where no users have rated the item, or the active user has no ratings.

    # Calculate cosine similarity between the target user and other users
    similarities = []
    for other_user_id in similar_users:
        other_user_ratings = ratings[other_user_id, :]
        mask = (user_ratings != 0) & (other_user_ratings != 0)  # Only consider common rated items

        if np.sum(mask) == 0:  #Handle the case of users with no common ratings.
            similarities.append((other_user_id, 0)) #Assign a similarity of 0 if no common ratings.
            continue

        similarity = cosine_similarity(user_ratings[mask], other_user_ratings[mask])
        similarities.append((other_user_id, similarity))

    # Sort users by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Select the top k nearest neighbors
    nearest_neighbors = similarities[:min(k, len(similarities))]

    # Calculate the weighted average of ratings
    numerator = 0
    denominator = 0
    for neighbor_id, similarity in nearest_neighbors:
        numerator += similarity * ratings[neighbor_id, item_id]
        denominator += similarity

    if denominator == 0: #Handles the case where all neighbors have similarity of 0.
        return np.mean(ratings[user_id, ratings[user_id,:]!=0]) if np.any(ratings[user_id, ratings[user_id,:]!=0]) else np.mean(ratings[ratings!=0]) if np.any(ratings[ratings!=0]) else 0

    return numerator / denominator

def cosine_similarity(vec1, vec2):
    """
    Calculates the cosine similarity between two vectors.
    can implement linalg norm (denominator)
    and dot product manually
    see below 
    Pearson correlation accounts for differences in rating scale by centering the data around the mean rating of each user.
    Users have consistent rating biases
    Measures the linear relationship between two variables.
    Only uses co-rated items, and requires at least 2 co-rated items to function.
    When the dataset is not extremely sparse, and there are many co-rated items.
    """
    magnitude_vec1 = np.linalg.norm(vec1)
    magnitude_vec2 = np.linalg.norm(vec2)

    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0

    dot_product = np.dot(vec1, vec2)
    return dot_product / (magnitude_vec1 * magnitude_vec2)

# can do the dot product manually
def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        return None 
    result = 0
    for i in range(len(vec1)):
        result += vec1[i] * vec2[i]
    return result

# we can do magnitude manually
def linalg_norm(vector, ord=None):
    if ord is None or ord == 2:  # Euclidean norm (L2 norm)
        squared_sum = sum(x**2 for x in vector)
        return math.sqrt(squared_sum)

    elif ord == 1:  # L1 norm (Manhattan norm)
        return sum(abs(x) for x in vector)

    elif ord == float('inf'):  # L-infinity norm (max norm)
        return max(abs(x) for x in vector)

    elif ord == float('-inf'): # negative infinity norm (min abs norm)
        return min(abs(x) for x in vector)

    else:
        raise ValueError("Unsupported norm order.")

# Example usage:
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
])

user_id = 0
item_id = 2
predicted_rating = user_user_collaborative_filtering(ratings, user_id, item_id)
print(f"Predicted rating for user {user_id} and item {item_id}: {predicted_rating}")

user_id = 0
item_id = 0
predicted_rating = user_user_collaborative_filtering(ratings, user_id, item_id)
print(f"Predicted rating for user {user_id} and item {item_id}: {predicted_rating}")