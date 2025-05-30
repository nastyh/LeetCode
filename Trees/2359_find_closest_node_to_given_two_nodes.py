from collections import defaultdict, deque
import math
from typing import List


class Solution:
    def closestMeetingNode_optimal(self, edges: List[int], node1: int, node2: int) -> int:
        """
        O(n) both
        Each node points to at most one node: edges[i], or -1 if none. So you can just follow edges directly.
        walk down the chain with a loop.
        """
        def get_distances(start): # helper 
            """
            returns a list 
            [distance from this node to start,...] 
            """
            n = len(edges)
            dist = [-1] * n
            curr = start
            d = 0
            while curr != -1 and dist[curr] == -1: #meaning we don't hit a node that doesn't point anywhere
                dist[curr] = d
                curr = edges[curr]
                d += 1
            return dist
        
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        min_dist = math.inf 
        res = -1
        
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_d = max(dist1[i], dist2[i])
                if max_d < min_dist:
                    min_dist = max_d
                    res = i
        return res
    def closestMeetingNode_bfs(self, edges: List[int], node1: int, node2: int) -> int:
        """
        O(n) to loop, for helper, final comp
        O(n), adj_list, deque 
        BFS but a bit exsessive 
        build an adj_list: node = [other nodes it links to]
        distances is a list, first element for node 0, second for node 1, etc 
        In the helper function, we will fill distances with the values: how long is it 
        to go from candidate to this particular node (that is the index of the list)
        do it twice for node1 and node2
        then go over both lists and compare the values at the respective indices 
        take the larger value (distance)
        but we need need a node with a smaller value that has a large distance
        pick and return
        """
        adj_list = defaultdict(list)
        for node in range(len(edges)):
            if edges[node] != -1:
                adj_list[node].append(edges[node])
            else: adj_list[node].append(None)

        def _helper_distances(edges, candidate):
            distances = [-1] * len(edges)
            distances[candidate] = 0
            d = deque([candidate])
            while d:
                curr = d.popleft()
                for neighbor in adj_list[curr]:
                    if neighbor != None: 
                        if distances[neighbor] == -1:
                            distances[neighbor] = distances[curr] + 1 
                            d.append(neighbor)
                    else:
                        continue
            return distances 

        from_node1, from_node2 = _helper_distances(edges, node1), _helper_distances(edges, node2)
        min_dist, res = math.inf, -1 
        for i in range(len(edges)):
            if from_node1[i] != -1 and from_node2[i] != -1:
                max_d = max(from_node1[i], from_node2[i])
                if max_d < min_dist:
                    min_dist = max_d
                    res = i
        return res