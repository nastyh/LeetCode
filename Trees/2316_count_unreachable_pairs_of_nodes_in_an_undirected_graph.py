from collections import defaultdict, deque
from typing import List


class Solution:
    def countPairs_bfs(self, n: int, edges: List[List[int]]) -> int:
        """
        O(n+e), where e = len(edges) to visit all nodes and edges once

        O(n+e), for adj list, visited and deque
        Build the adj list
        helper takes a value as an input
        checks via visited if we've already seen it 
        if no, marks as such
        increments the size (length, basically)
        then goes to the adj_list, takes the neighbor from the values of this dict
        puts into the deque, repeats 
        Overall it calculates the size of connected components for a given input
        We need to substract it from all possible pairs to arrive at the number of unreachable pairs
        """
        # # first: [second] and second: [first] for each edge 
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = [False] * n

        def bfs(start): # bfs is here 
            d = deque([start])
            size = 0
            while d:
                node = d.popleft()
                if visited[node]:
                    continue
                visited[node] = True
                size += 1
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        d.append(neighbor)
            return size
        
        total_pairs = n * (n - 1) // 2  # total possible pairs
        for i in range(n):
            if not visited[i]:
                component_size = bfs(i)
                # Subtract reachable pairs within this component
                total_pairs -= component_size * (component_size - 1) // 2

        return total_pairs

    def countPairs_dfs(self, n: int, edges: List[List[int]]) -> int:
        """
        O(n+e), where e = len(edges) for the DFS traversal, and n i for computing total pairs ad iterating nodes
        O(n+e), for adj list and for visited 

        Traverse each component using DFS
        For each component of size c, it contributes c * (n - c) unreachable pairs
        To avoid double counting, keep a running total and subtract from the total possible pairs n * (n - 1) // 2.
        """
        # first: [second] and second: [first] for each edge 
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = [False] * n

        def dfs(node):
            stack = [node]
            size = 0
            while stack:
                curr = stack.pop()
                if not visited[curr]:
                    visited[curr] = True
                    size += 1
                    for neighbor in adj_list[curr]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            return size

        total_pairs = n * (n - 1) // 2
        for i in range(n):
            if not visited[i]:
                size = dfs(i)
                total_pairs -= size * (size - 1) // 2  # reachable pairs within this component

        return total_pairs
