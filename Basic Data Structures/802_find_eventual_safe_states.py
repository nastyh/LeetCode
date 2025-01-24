from collections import deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        O(m+n) m is edges, n is the number of nodes
        O(m+n), adj_list is O(m), in_degree is O(n)
        in_degree is the list storing the num of edges entering node i
        adj_list is a list where adj[x] has the nodes with an incoming edge from x 
        create it by adding the reverse edges
        deque is initialized for BFS to move from the leaf nodes to the parent nodes
        leaf nodes have in_degree of 0
        safe_nodes tracks safe nodes
        """
        adj_list = [[] for _ in range(len(graph))]
        in_degree = [0] * len(graph)
        safe_nodes = [False] * len(graph)
        d = deque()
        res = []
        for i in range(len(graph)):
            for node in graph[i]:
                adj_list[node].append(i)
                in_degree[i] += 1
        # print(f"this is adj_list: {adj_list}")
        # print(f"this is in_degree: {in_degree}")
        for i in range(len(graph)):
            if in_degree[i] == 0:
                """
                means that neighbor behaves as a leaf node, so we push neighbor in the d.
                """
                d.append(i)
        
        while d:
            curr_n = d.popleft()
            safe_nodes[curr_n] = True 
            for neighbor in adj_list[curr_n]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    d.append(neighbor)
        # build the answer 
        for i in range(len(graph)):
            if safe_nodes[i]:
                res.append(i)
        return res
            

