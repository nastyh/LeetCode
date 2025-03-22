from collections import deque
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        O(n+m): m the num of edges; n -- num of edges 
        O(n+m) 
        """
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def _dfs(node):
            stack = [node]
            vertices = []
            edge_count = 0
            while stack:
                curr = stack.pop()
                if visited[curr]:
                    continue
                visited[curr] = True
                vertices.append(curr)
                for neighbor in graph[curr]:
                    edge_count += 1  # each edge will be counted twice overall
                    if not visited[neighbor]:
                        stack.append(neighbor)
            return vertices, edge_count // 2
        
        complete_components = 0
        for i in range(n):
            if not visited[i]:
                component, edges_in_component = dfs(i)
                k = len(component)
                # For a complete graph with k nodes, number of edges must be k*(k-1)/2
                if edges_in_component == k * (k - 1) // 2:
                    complete_components += 1

        return complete_components
    
    def countCompleteComponents_bfs(self, n: int, edges: List[List[int]]) -> int:
        """
        bfs 
        O(n+m), vertex and edge 
        O(n+m), same 
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n

        def bfs(start):
            queue = deque([start])
            visited[start] = True
            component_nodes = []
            edge_count = 0
            
            while queue:
                node = queue.popleft()
                component_nodes.append(node)
                # Count all edges from the current node
                for neighbor in graph[node]:
                    edge_count += 1  # each edge will be counted twice overall
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            # Since each edge is counted twice, divide the total by 2.
            return component_nodes, edge_count // 2

        complete_components = 0

        for i in range(n):
            if not visited[i]:
                component, edges_in_component = bfs(i)
                k = len(component)
                # For a complete graph with k nodes, there should be k*(k-1)//2 edges
                if edges_in_component == k * (k - 1) // 2:
                    complete_components += 1

        return complete_components


