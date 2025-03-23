import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        O(ElogN), E num of roads, N num of intersections. Due to a prioritiy queue 
        O(N+E) to store the graph (E) and distance&ways lists (N) and a priority queue

        track the minimum time to reach each intersection,
        also maintain a count of the number of ways to achieve that minimum time.
        When we relax an edge, if we find a shorter path to a neighbor,
        we update both the time and the ways.
        If we find an equally short path, we add the count of ways.
        """
        mod, gr = 10**9 +7, [[] for _ in range(n)]
        for u, v, time in roads:
            """
            structure of gr below is it's a list of lists 
            it has n sublists (n intersections)
            Each sublist represents the neighbors of this intersection
            if you have a road between 0 and 1 and it takes 2 minutes, we have
            gr[0] has [1, 2]
            gr[1] has [0, 2]
            """
            gr[u].append((v, time))
            gr[v].append((u, time))
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        h = [(0, 0)]

        while h:
            curr_time, u = heapq.heappop(h)
            if curr_time > dist[u]:
                continue
            for v, t in gr[u]:
                new_time = curr_time + t
                if new_time < dist[v]:
                    # Found a shorter way: update distance and ways
                    dist[v] = new_time
                    ways[v] = ways[u]
                    heapq.heappush(h, (new_time, v))
                elif new_time == dist[v]:
                    # Found another shortest path: add the ways
                    ways[v] = (ways[v] + ways[u]) % mod
        return ways[n - 1]
    
    def countPaths_dict(self, n: int, roads: List[List[int]]) -> int:
        """
        same but with a dict for the graph instead
        """
        MOD = 10**9 + 7
        # Build the graph using a dictionary where each key is a node
        # and its value is a list of tuples (neighbor, travel_time)
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Initialize distance and ways dictionaries:
        # dist[node] stores the shortest time to reach the node,
        # ways[node] stores the number of ways to reach the node in the shortest time.
        dist = {i: float('inf') for i in range(n)}
        ways = {i: 0 for i in range(n)}
        
        # Starting from node 0
        dist[0] = 0
        ways[0] = 1
        
        # Priority queue to get the next node with the minimum travel time
        heap = [(0, 0)]
        
        while heap:
            curr_time, u = heapq.heappop(heap)
            # Skip if we have already found a better route
            if curr_time > dist[u]:
                continue
            # Check neighbors of the current node
            for v, t in graph[u]:
                new_time = curr_time + t
                # Found a shorter path to neighbor v
                if new_time < dist[v]:
                    dist[v] = new_time
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_time, v))
                # Found another shortest path to neighbor v
                elif new_time == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n - 1]