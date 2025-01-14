from typing import List


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        """
        O(2^n * n^3), Subset gen and validation: O(2^n * n^3); Floyd-Warshall for the matris: O(n^3)
        Space: O(n^2) due to distance matrix and temp dist matrix for each subset
        The graph is represented as an adjacency matrix where dist[u][v] is the min weight
        of the edge between the nodes. If no direct edge, make inf
        """
        inf = 10**9+7
        dist = [[inf]*n for _ in range(n)]
        
        for u,v,w in roads: 
            dist[u][v] = min(dist[u][v],w)
            dist[v][u] = min(dist[v][u],w)
        
        def check(D,rem):
            """
            ensures that the remaining branches in a subset:

            Are reachable within maxDistance.
            Form a connected graph.
            The Floyd-Warshall algorithm is used to compute the shortest paths in the graph,
            allowing us to determine the pairwise distances between any two branches.
            """
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if D[i][k] < inf and D[k][j] <inf: 
                            D[i][j] = min(D[i][j],D[i][k]+D[k][j])
                            
            for x in rem:
                for y in rem:
                    if x == y:continue
                    if D[x][y]>maxDistance: return False
                    
            return True
                        
        """
        All subsets of nodes are generated using a bitmask approach. 
        mask represents which nodes are active in the subset.
        if the i-th bit in mask is 1, branch i is included in the active subset
        For nodes that are excluded (branches marked as closed), their corresponding distances are inf
        """
        ans = 0 
        for mask in range(1<<n):
            newDist = [dist[i].copy() for i in range(n)]
            
            rem = []
            for i in range(n):
                if (mask>>i)&1 == 0: 
                    for j in range(n):
                        newDist[i][j] = inf
                        newDist[j][i] = inf
                else: 
                    rem.append(i)
            
            if check(newDist,rem): 
                ans+=1
            
        
        return ans
        