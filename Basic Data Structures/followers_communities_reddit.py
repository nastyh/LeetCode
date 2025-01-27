"""
We have communities with IDs C1,C2,... and followers with IDs F1,F2,..., where each user can follow any of the communities.

We would like to find “similar” or “related” communities by finding all communities that share followers with the input one, Cx.
Implement a function to return all related communities of Cx.

Example:
Community -> follower data:
C1: [F1, F3]
C2: [F1, F2]
C3: [F2]
C4: [F3]


Follower -> community data (mirrored data):
F1: [C1, C2]
F2: [C2, C3]
F3: [C1, C4]


get_related_communities(C4) -> [C1]
get_related_communities(C2) -> [C1,C3]


Assume the data for both maps is pre populated and you can use it for the problem.

"""

class Community:
    def __init__(self, community_id, followers=None):
        self.community_id = community_id
        self.followers = followers if followers is not None else []

    def add_follower(self, follower_id):
        self.followers.append(follower_id)


class Follower:
    def __init__(self, follower_id, communities=None):
        self.follower_id = follower_id
        self.communities = communities if communities is not None else []

    def add_community(self, community_id):
        self.communities.append(community_id)


def get_related_communities(community_id, community_to_followers, follower_to_communities):
    """
    takes the input community ID and pre-populated mappings (community_to_followers and follower_to_communities)
    to determine the related communities. It gathers all communities that share followers with the input one and
    excludes the input community itself from the result.
    """
    # Get the followers of the input community
    followers_of_community = community_to_followers.get(community_id, [])

    # Initialize a set to store related communities
    related_communities = set()

    # Loop through each follower of the input community
    for follower in followers_of_community:
        # Get the communities followed by this follower
        communities = follower_to_communities.get(follower, [])
        # Add these communities to the related communities set
        related_communities.update(communities)

    # Remove the input community from the result (if it exists)
    related_communities.discard(community_id)

    # Return the result as a sorted list (optional, for consistent order)
    return sorted(related_communities)

# Example data
community_to_followers = {
    "C1": ["F1", "F3"],
    "C2": ["F1", "F2"],
    "C3": ["F2"],
    "C4": ["F3"]
}

follower_to_communities = {
    "F1": ["C1", "C2"],
    "F2": ["C2", "C3"],
    "F3": ["C1", "C4"]
}

# Example usage
print(get_related_communities("C4", community_to_followers, follower_to_communities))  # Output: ["C1"]
print(get_related_communities("C2", community_to_followers, follower_to_communities))  # Output: ["C1", "C3"]

"""
Now, we want to explore communities which might not share followers directly but are related by indirect relationships
(eg. C4 is indirectly related to C2 through C1). Extend the solution to accept degrees of indirect relationship as an input.
Each degree adds to the result the communities directly related (sharing followers) to the communities from the previous degrees.
Please note that we’re interested in related communities up-to a specific degree (as opposed to only at a specific degree).


Example:
get_related_communities_with_degree(C4, 1) -> [C1]
get_related_communities_with_degree(C4, 2) -> [C1, C2]


community_map = {
'C1': ['F1', 'F3'],
'C2': ['F1', 'F2'],
'C3': ['F2'],
'C4': ['F3'],
}


follower_map = {
'F1': ['C1', 'C2'],
'F2': ['C2', 'C3'],
'F3': ['C1', 'C4'],
}

"""

"""
# Time Complexity: O(d * (F + C))
# - d: degree of relationship
# - F: average number of followers per community
# - C: average number of communities per follower
# In each iteration up to degree d, we traverse followers of communities and their related communities.

# Space Complexity: O(C + F)
# - Space for storing related communities and intermediate layers
# - Input maps (community_to_followers and follower_to_communities) are assumed to be preloaded.
"""

class Community:
    def __init__(self, community_id, followers=None):
        self.community_id = community_id
        self.followers = followers if followers is not None else []

    def add_follower(self, follower_id):
        self.followers.append(follower_id)


class Follower:
    def __init__(self, follower_id, communities=None):
        self.follower_id = follower_id
        self.communities = communities if communities is not None else []

    def add_community(self, community_id):
        self.communities.append(community_id)


def get_related_communities_with_degree(community_id, degree, community_to_followers, follower_to_communities):
    # Initialize a set to store all related communities
    all_related_communities = set()
    # Initialize the current layer with the input community
    current_layer = {community_id}

    for _ in range(degree):
        next_layer = set()
        # Process each community in the current layer
        for community in current_layer:
            # Get the followers of the community
            followers_of_community = community_to_followers.get(community, [])
            for follower in followers_of_community:
                # Get the communities followed by this follower
                communities = follower_to_communities.get(follower, [])
                # Add these communities to the next layer
                next_layer.update(communities)
        # Add the next layer to all related communities
        all_related_communities.update(next_layer)
        # Update the current layer
        current_layer = next_layer

    # Remove the input community from the result (if it exists)
    all_related_communities.discard(community_id)

    # Return the result as a sorted list (optional, for consistent order)
    return sorted(all_related_communities)



# Example data
community_to_followers = {
    "C1": ["F1", "F3"],
    "C2": ["F1", "F2"],
    "C3": ["F2"],
    "C4": ["F3"]
}

follower_to_communities = {
    "F1": ["C1", "C2"],
    "F2": ["C2", "C3"],
    "F3": ["C1", "C4"]
}

# Example usage
print(get_related_communities_with_degree("C4", 1, community_to_followers, follower_to_communities))  # Output: ["C1"]
print(get_related_communities_with_degree("C4", 2, community_to_followers, follower_to_communities))  # Output: ["C1", "C2"]
