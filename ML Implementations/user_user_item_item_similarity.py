from sklearn.metrics.pairwise import cosine_similarity

# Assume `user_rated_matrix` is a matrix with users as rows and items as columns, denoting user ratings.
# Selecting two users, num_users denotes the total number of users.
user1_ratings = user_rated_matrix[0]
user2_ratings = user_rated_matrix[1]

# Computing cosine similarity
similarity = cosine_similarity([user1_ratings, user2_ratings])

print(f"Cosine similarity between user 1 and 2: {similarity[0, 1]}")