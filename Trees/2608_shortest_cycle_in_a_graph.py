from collections import deque
import math
from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        """
        O(V+E) to visit
        O(V) for storage 
        BFS
        adj list: node: [its neighbors]

        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        INF = math.inf
        res = INF

        for src in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = deque([src])
            dist[src] = 0

            while q:
                u = q.popleft()
                if dist[u] * 2 + 1 >= res:          # pruning: no chance to beat current best
                    continue
                for v in adj[u]:
                    if dist[v] == -1:                # tree edge
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:             # back edge → cycle
                        cycle_len = dist[u] + dist[v] + 1
                        if cycle_len < res:
                            res = cycle_len
                            if res == 3:            # cannot get any shorter
                                return 3
        return -1 if res == INF else res
