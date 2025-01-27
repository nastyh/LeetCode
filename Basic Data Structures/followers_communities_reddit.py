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

from collections import defaultdict, deque
from typing import Dict, List


class Community:
    def __init__(self, name):
        self.followers = []
        self.name = name
    
    def __repr__(self):
        return self.name

class Follower:
    def __init__(self, name):
        self.communities = []
        self.name = name

    def __repr__(self):
        return self.name
    
    def follow(self, communities):
        for c in communities:
            c.followers.append(self)
        self.communities += communities

C1 = Community('C1')
C2 = Community('C2')
C3 = Community('C3')
C4 = Community('C4')

F1 = Follower('F1')
F2 = Follower('F2')
F3 = Follower('F3')

F1.follow([C1, C2])
F2.follow([C2, C3])
F3.follow([C1, C4])

def get_related_communities(c):
    res = set()
    for f in c.followers:
        for fc in f.communities:
            if fc != c:
                res.add(fc)
    return list(res)

print(get_related_communities(C4)) # returns "[C1]"
print(get_related_communities(C2)) # returns "[C3, C1]"

def get_related_communities_with_degree(c, degree):
    res = get_related_communities(c)
    
    while degree > 1:
        tmp_res = []
        for comm in res:
            tmp_res += get_related_communities(comm)
        res += tmp_res
        degree -= 1
    return list(filter(lambda x: x != c, list(set(res))))

print(get_related_communities_with_degree(C4, 1)) # returns "[C1]"
print(get_related_communities_with_degree(C4, 2)) # returns "[C1, C2]"
# Time and Space Complexity Analysis:  Same as the previous version using CommunityNetwork.


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


def get_related_communities(community_id):
    # Predefined mappings
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

# Example usage
print(get_related_communities("C4"))  # Output: ["C1"]
print(get_related_communities("C2"))  # Output: ["C1", "C3"]



# BFS
class Community:
    def __init__(self, c_to_f: Dict[str, List[str]], f_to_c: Dict[str, List[str]]) -> None:
        self.c_to_f = c_to_f
        self.f_to_c = f_to_c
        
    def get_related_communities(self, c: str) -> List[str]:
        if c not in self.c_to_f:
            return []
        
        # BFS: c -> all followers -> communities -> minus c -> result
        communities_set = set()
        for f in self.c_to_f[c]:
            if f not in self.f_to_c:
                continue
            # pretty efficient - O(1) if there are large amount of data the 
            # hashing could degrade the performance.
            communities_set.update(self.f_to_c[f])
        return list(communities_set - {c,})
    
    def get_related_communities_with_degree(self, c: str, degree: int) -> List[str]:
        # graph problem 
        graph = defaultdict(list)
        for c in self.c_to_f.keys():
            graph[c].extend(self.get_related_communities(c))
        
        # use BFS to search the graph
        q = deque([c])
        visited = {c, }
        res = []
        while len(q) > 0:
            for i in range(len(q)):
                cur = q.popleft()
                
                if degree <= 0:
                    return res
                
                for direct_c in graph[cur]:
                    if direct_c not in visited:
                        res.append(direct_c)
                        visited.add(direct_c)
                        q.append(direct_c)
            degree -= 1
        
        return []
        
c = Community(community_to_followers, follower_to_communities)
assert c.get_related_communities("C4") == ["C1"]
assert c.get_related_communities("C2") == list(set(["C3", "C1"]))
assert c.get_related_communities_with_degree("C4", 1) == ["C1"]
assert c.get_related_communities_with_degree("C4", 2) == ["C1", "C2"]

