import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample item data
item_data = {
    'item_id': [1, 2, 3, 4, 5],
    'item_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Electronics']
}

items = pd.DataFrame(item_data)

# Sample user data with context
user_data = {
    'user_id': [1, 2],
    'state': ['NY', 'CA']
}

users = pd.DataFrame(user_data)

# Sample user interactions
interactions = {
    'user_id': [1, 2, 1],
    'item_id': [4, 1, 2],
    'context': ['Morning', 'Evening', 'Afternoon']
}

interactions_df = pd.DataFrame(interactions)

# Select context for a user (assuming we know the context based on time of the day)
user_id = 1
context = 'Morning'

user_interactions = interactions_df[interactions_df['user_id'] == user_id]
context_specific_interactions = user_interactions[user_interactions['context'] == context]

# Items the user interacted with in the selected context
item_ids_context = context_specific_interactions['item_id'].tolist()

# Match items in the same context
items_in_context = interactions_df[
    (interactions_df['context'] == context) &
    (~interactions_df['item_id'].isin(item_ids_context))
]

recommended_items_context = items_in_context['item_id'].unique()

# Recommend items based on shared context
# but not yet interacted with in the same context
print(recommended_items_context)