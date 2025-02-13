"""
provided customer / Boost usage data so that you can construct customer profile vectors.
To determine customer similarity, you will compare customer profile vectors using the cosine similarity metric
(which is provided for you). Finally, for a given customer,
you will provide a list of Boost recommendations that the customer has never used before with new Boosts from more similar customers coming first.
boost_descriptions = {
    0: "10% Off McDonald's",
    1: '$1 Off Any Pizza Shop',
    2: '$1 Off Any Coffee Shop',
    3: '10% Off Chipotle',
    4: '10% Off Whole Foods'
}

# Customer / Boost pairs of the form [customer_index, boost_index]
customer_boost_pairs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 3],
    [2, 4],
    [3, 1],
    [3, 3],
    [3, 4],
    [4, 1],
    [4, 2],
    [5, 0],
    [5, 1],
    [5, 4],
    [6, 2],
    [6, 3],
    [6, 4],
    [7, 4],
    [8, 3],
    [8, 4],
    [9, 0],
    [9, 1],
    [9, 2],
    [9, 3],
    [9, 4]
]
"""
from scipy.spatial.distance import cosine
from collections import defaultdict

def build_customer_usage(pairs, num_boosts):
    """
    Build a fixed-length vector for each customer based on usage.
    Each customer is represented by a list of length `num_boosts` where a 1 indicates usage of that Boost.
    """
    usage = defaultdict(lambda: [0] * num_boosts)
    for customer, boost in pairs:
        usage[customer][boost] = 1  # Binary indicator for usage
    return dict(usage)

def recommend_boosts(customer_usage, target_customer):
    """
    For the target customer, compute the cosine similarity (via SciPy) with every other customer.
    For every Boost not used by the target, sum the similarity scores of customers who used it.
    Return Boost IDs sorted by this aggregated similarity score in descending order.
    """
    if target_customer not in customer_usage:
        return []
    
    target_vector = customer_usage[target_customer]
    similarities = {}
    
    # Compute similarity between target and every other customer.
    for customer, vector in customer_usage.items():
        if customer == target_customer:
            continue
        # cosine() returns cosine distance, so similarity is 1 - distance.
        sim = 1 - cosine(target_vector, vector)
        similarities[customer] = sim

    # Aggregate similarity scores for Boosts that the target hasn't used.
    recommended_scores = defaultdict(float)
    for customer, sim in similarities.items():
        vector = customer_usage[customer]
        for boost, used in enumerate(vector):
            if target_vector[boost] == 0 and used:
                recommended_scores[boost] += sim

    # Sort Boosts by aggregated similarity score in descending order.
    sorted_boosts = sorted(recommended_scores.items(), key=lambda x: x[1], reverse=True)
    return [boost for boost, score in sorted_boosts]

# Provided data
boost_descriptions = {
    0: "10% Off McDonald's",
    1: '$1 Off Any Pizza Shop',
    2: '$1 Off Any Coffee Shop',
    3: '10% Off Chipotle',
    4: '10% Off Whole Foods'
}

# Customer / Boost pairs of the form [customer_index, boost_index]
customer_boost_pairs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 3],
    [2, 4],
    [3, 1],
    [3, 3],
    [3, 4],
    [4, 1],
    [4, 2],
    [5, 0],
    [5, 1],
    [5, 4],
    [6, 2],
    [6, 3],
    [6, 4],
    [7, 4],
    [8, 3],
    [8, 4],
    [9, 0],
    [9, 1],
    [9, 2],
    [9, 3],
    [9, 4]
]

if __name__ == "__main__":
    num_boosts = len(boost_descriptions)
    # Build fixed-length vectors for each customer.
    customer_usage = build_customer_usage(customer_boost_pairs, num_boosts)
    
    # For example, generate recommendations for customer 0.
    target_customer = 0
    recommended_boosts = recommend_boosts(customer_usage, target_customer)
    
    # Map recommended Boost IDs to their descriptions for clarity.
    recommendations_with_descriptions = [
        (boost, boost_descriptions[boost]) for boost in recommended_boosts
    ]
    
    print("Recommendations for Customer", target_customer, ":")
    for boost, desc in recommendations_with_descriptions:
        print(f"Boost {boost}: {desc}")
