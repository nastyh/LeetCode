class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """
        O(n+m), m to build the adj list. Process every node and edge once, so approx O(n+m)
        O(n+m), m to store the adj list. BFS queue can store up to n elements in the worst case

        A valid split of the tree occurs by removing some (or possibly none) edges,
        such that the sum of node values in each resulting component is divisible by k.
        The goal is to determine the maximum number of components in any valid split.
        start with the simplest parts of the tree — the leaf nodes — and work the way up

         remove processed leaf nodes, reducing the tree layer by layer.
         Remove each leaf node, updating its parent node’s value with the carry-over sum.
         If the parent node becomes a new leaf (i.e., it now has only one remaining neighbor),
         add it to the processing queue and repeat the process.
        """
        if n < 2: return 1 # edge case: only one node forms one component 
        counts = 0 # number of valid components to return 
        graph = defaultdict(set)
        for node1, node2 in edges: # for edge [node1, node2] add node2 as a neighbor of node1 and vice versa
            graph[node1].add(node2)
            graph[node2].add(node1)
        d = deque(n for n, neighbors in graph.items() if len(neighbors) == 1) # initialize with an empty neighbor
        while d:
            t = d.popleft()
            neig_n = (next(iter(graph[t])) if graph[t] else -1) # neighbor node exists and becomes a leaf node
            if neig_n >= 0:
                graph[neig_n].remove(t)
            
            if values[t] % k == 0:
                counts += 1
            else: values[neig_n] += values[t]
            if neig_n >= 0 and len(graph[neig_n]) == 1:
                d.append(neig_n)
        return counts