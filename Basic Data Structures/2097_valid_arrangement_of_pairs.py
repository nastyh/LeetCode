from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        """
        O(ElogE), E -- number of degrees/pairs 
        O(E) for the dfs traversal
        O(n) space due to the adj list, n is the num of pairs in pairs 

        Eulerian path in a directed graph.
        Each pair [u, v] in the input represents a directed path from u to v
        A valid arrangement means that for every adjacent pair, the second element of 
        one part is equal to the first element of the other part 
        Construct the ad_list: first val in each list: [second val associated with this val]
        Sort, for the determenistic behavior, the values in the dict

        _dfs() traverses the graph 
        outgoing edges from the current node, expore one and remove the edge from the graph
        Add the edge to the answer after exploring all outgoing edges from a given node. 
        The answer list is built in reverse 

        Reverse it at the end to get the right result and return res 
        """
        adj_list = defaultdict(list) # key is starting point, value are the lists of ending points
        path = []
        res = []
        for pair in pairs:
            adj_list[pair[0]].append(pair[1]) # first val in each list: [second val in each list]
        for node in adj_list:
            adj_list[node].sort(reverse=True)

        def _dfs(node):
            while adj_list[node]:
                next_node = adj_list[node].pop() # take out an element from the list 
                _dfs(next_node)
            path.append(node)
        
        # We need to start from a node that has one more outgoing edge than incoming, if it exists
        # Otherwise, any node can start; we choose the start of the first pair as a default.
        start_node = pairs[0][0]
        # To determine a valid starting point, count the difference between outdegree and indegree.
        outdegree = defaultdict(int)
        indegree = defaultdict(int)
        for u, v in pairs:
            outdegree[u] += 1
            indegree[v] += 1
        for u, v in pairs: 
            #  # If a node has an extra outgoing edge, it is the ideal start.
            if outdegree[u] - indegree[u] == 1:
                start_node = u
                break
        
        _dfs(start_node)
        path = path[::-1]

        for i in range(1, len(path)): # 1 since we compare the neighboring elements 
            res.append([path[i - 1], path[i]])
        
        return res 
        