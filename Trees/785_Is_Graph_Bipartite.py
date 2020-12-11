from collections import deque
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
    for node in range(len(graph)):
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
        Space Complexity: O(N); O(N), the space used to store the color
        """


def isBipartite_alt(graph):
    """
    Dictionary starts with graph_value : 0. Everything is unvisited
    _helper checks if a given node is unvisited. If it's visited, check if it's of the color that we're passing
    Otherwise, color it using a color that we're passing
    Then process this node's neighbors. If you can't color it in a different color, return False. Otherwise it's True for this neighbor.
    """
    d = {i : 0 for i in range(len(graph))}
    def _helper(graph, d, color, node):
        if d[node] != 0:
            return d[node] == color
        else:
            d[node] = color
            for neighbor in graph[node]:
                if not _helper(graph, d, -color, neighbor):
                    return False
        return True
    for i in range(len(graph)):
        if d[i] == 0 and not _helper(graph, d, 1, i):  # if a node is unvisited and we can't color everything appropriately
            return False
    return True


def isBipartite_recurs(graph):
    colors = {} #store node and its corresponding color
        #DFS recursive
    def dfs(node, color = 1): # current node and current color
        if node in self.colors:
            return self.colors[node] == color
        self.colors[node] = color
        return all(dfs(n, -color) for n in graph[node])

    return all(dfs(node) for node in range(len(graph)) if node not in self.colors)


def isBipartite_stack(graph):
    colors = {}
    for from_node in range(len(graph)):
        if from_node in colors:
            continue

        stack = [from_node]
        colors[from_node] = 1  # 1 is just starting color
        while stack:
            from_node = stack.pop()

            for to_node in graph[from_node]:
                if to_node in colors:
                    if colors[to_node] == colors[from_node]:
                        return False
                else:
                    stack.append(to_node)                        
                    colors[to_node] = colors[from_node] * -1
    return True


def isBipartite_queue(graph):
    def bfs(graph, node, colors):
        queue = deque([node])
        colors[node] = 1
        while queue:
            node_from = queue.popleft()
            for node_to in graph[node_from]:
                if node_to in colors:
                    if colors[node_to] == colors[node_from]:
                        return False
                else:
                    colors[node_to] = colors[node_from] * -1
                    queue.append(node_to)
        return True
    colors = {}
    for node_from in range(len(graph)):
        if node_from not in colors and not bfs(graph, node_from, colors):
            return False
    return True


if __name__ == '__main__':
    print(isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
    print(isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    print(isBipartite_queue([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
