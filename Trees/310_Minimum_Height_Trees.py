"""
Starting from each node in the graph, we treat it as a root to build a tree. Furthermore, we would like to know the distance between this root node and the rest
 of the nodes. The maximum of the distance would be the height of this tree.
Then according to the definition of Minimum Height Tree (MHT), we simply filter out the roots that have the minimal height among all the trees.
Initially, we would build a graph with the adjacency list from the input.

We then create a queue which would be used to hold the leaves nodes.

At the beginning, we put all the current leaves nodes into the queue.

We then run a loop until there is only two nodes left in the graph.

At each iteration, we remove the current leaves nodes from the queue. While removing the nodes, we also remove the edges that are linked to the nodes. As a consequence, some of the non-leaf nodes would become leaves nodes. And these are the nodes that would be trimmed out in the next iteration.

The iteration terminates when there are no more than two nodes left in the graph, which are the desired centroids nodes.
"""
def findMinHeightTrees(n, edges):
    # base cases
    if n <= 2:
        return [i for i in range(n)]

    # Build the graph with the adjacency list
    neighbors = [set() for i in range(n)]
    for start, end in edges:
        neighbors[start].add(end)
        neighbors[end].add(start)

    # Initialize the first layer of leaves
    leaves = []
    for i in range(n):
        if len(neighbors[i]) == 1:
            leaves.append(i)

    # Trim the leaves until reaching the centroids
    remaining_nodes = n
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []
        # remove the current leaves along with the edges
        while leaves:
            leaf = leaves.pop()
            for neighbor in neighbors[leaf]:
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

        # prepare for the next round
        leaves = new_leaves

    # The remaining nodes are the centroids of the graph
    return leaves