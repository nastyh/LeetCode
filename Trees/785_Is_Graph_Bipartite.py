"""
a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
"""
def isBipartite(graph):
    """
    Color a node blue if it is part of the first set, else red. We should be able to greedily color the graph if and only if it is bipartite: one node being blue implies all it's neighbors are red, all those neighbors are blue, and so on.
    We'll keep an array (or hashmap) to lookup the color of each node: color[node]. The colors could be 0, 1, or uncolored (-1 or null).
    To perform the depth-first search, we use a stack. For each uncolored neighbor in graph[node], we'll color it and add it to our stack, which acts as a sort of "todo list" of nodes to visit next.
    """
    color = {}
    for node in xrange(len(graph)):
        if node not in color:
            stack = [node]
            color[node] = 0
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if nei not in color:
                        stack.append(nei)
                        color[nei] = color[node] ^ 1
                    elif color[nei] == color[node]:
                        return False
        return True

        """
        Time Complexity: O(N + E)O(N+E), where NN is the number of nodes in the graph, and EE is the number of edges
        Space Complexity: O(N)O(N), the space used to store the color
        """

def isBipartite_recurs(graph):
    colors = {} #store node and its corresponding color
        #DFS recursive
        def dfs(node, color=1): # current node and current color
            if node in self.colors:
                return self.colors[node] == color
            self.colors[node] = color
            return all(dfs(n,-color) for n in graph[node])

        return all(dfs(node) for node in range(len(graph)) if node not in self.colors)
