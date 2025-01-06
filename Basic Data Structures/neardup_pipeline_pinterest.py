def form_neardup_clusters(near_dups):
    """
    O(V+E) V is the num of nodes, E tot number of edges
    Same 
    For each unvisited node, perform a DFS to explore all connected nodes and add them to the current cluster.
    Mark all visited nodes to ensure each node is processed only once.
    """
    def dfs(node, cluster):
        visited.add(node)
        cluster.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, cluster)

    # Step 1: Build an undirected graph from near_dups
    graph = {key: set() for key in near_dups}
    for key, values in near_dups.items():
        for value in values:
            graph[key].add(value)
            graph[value].add(key)

    # Step 2: Find connected components using DFS
    visited = set()
    clusters = []

    for node in graph:
        if node not in visited:
            cluster = []
            dfs(node, cluster)
            clusters.append(cluster)

    return clusters

# Example Input
near_dups = {
    "A": ["B", "I", "K"],
    "B": ["A", "D"],
    "C": ["E"],
    "D": [],
    "E": [],
    "F": [],
    "G": ["K"],
    "I": [],
    "K": [],
}

# Output Clusters
clusters = form_neardup_clusters(near_dups)
print(clusters)
