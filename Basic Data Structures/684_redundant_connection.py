from typing import List

class UnionFind:  # It's for the first solution
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False  # Cycle detected
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True
        
# UNION FIND: optimal, scroll down for others
class Solution:
    """
    Find operation: O(alpha(n)), almost const
    Union operation: same
    Overall: O(n) since we process each edge once
    Space:
    Parent array: O(n), parent of each node, n num of nodes
    Rank array: O(n), stores the rank (size) of each set 
    Overall: O(n)

    Union find:
    Initialize a parent array where each node is its own parent.
    Use a union operation to connect nodes and a find operation with path compression.
    Iterate through the edges, and for each edge
    If the two nodes of the edge are already connected (i.e., they have the same root in the DSU), then this edge is redundant.
    Otherwise, merge them using the union operation.
    Traverse edges in order, the last edge that forms a cycle is the answer.
    """
    cycle_start = -1 # it's for the second solution, not for UNION FIND
    def findRedundantConnection_union_find(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]  # The edge that forms a cycle
            
    
    def findRedundantConnection_dfs(self, edges: List[List[int]]) -> List[int]:
        """
        BFS, single traversal 
        """
        def _helper(src, visited, adj_list, parent):
            visited[src] = True
            for adj in adj_list[src]:
                if not visited[adj]:
                    parent[adj] = src
                    _helper(adj, visited, adj_list, parent)
                    # If the node is visited and the parent is different then the
                    # node is part of the cycle.
                elif adj != parent[src] and self.cycle_start == -1:
                    self.cycle_start = adj
                    parent[adj] = src
        
        N = len(edges)
        visited = [False] * N
        parent = [-1] * N
        adj_list = [[] for _ in range(N)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        _helper(0, visited, adj_list, parent)

        cycle_nodes = {}
        node = self.cycle_start
        # Start from the cycleStart node and backtrack to get all the nodes in
        # the cycle. Mark them all in the map.
        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break
        # If both nodes of the edge were marked as cycle nodes then this edge
        # can be removed.
        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0] - 1) in cycle_nodes and (
                edges[i][1] - 1
            ) in cycle_nodes:
                return edges[i]
        return []  # This line should theoretically never be reached
        
            
