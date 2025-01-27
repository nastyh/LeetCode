from collections import defaultdict
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        O(V^3 + E + Q), v is numCourses, and it dominates potentially

        Construct the graph: O(E), E is the num of prerequisites
        Query processing: O(Q), q is the num of queries
        O(V^2 + E), O(E) fo res, E edges 
        O(V^2) due to the reachable matrix
        Overall space is O(V^2 + E)
        Floyd-Warshall algorithm 

        reachable is a 2x2 matrix showing whether the row class
        is needed for the col class
        Propagate based on prerequisites
        the big loop uses the transitive nature of graphs
        For every intermediate course k, check if a path exists from i → k → j. If such a path exists, update reachable[i][j] = True.
        build the solution
        """
        res = []
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for pre in prerequisites:
            # whatever is in prerequisites becomes True
            reachable[pre[0]][pre[1]] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        for u, v in queries:
            res.append(reachable[u][v])
        return res
    
    def checkIfPrerequisite_dfs(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        O(V + E + Q), numCourses, E=len(prerequisites), Q -- queries
        O(V^2 + E), adj_list O(V+E), O(V^2) is the worst case. visited and recursion stak give O(E)
        During DFS, recursively compute the reachability of a node’s neighbors
        and merge their reachable courses into the current course's set.
        Use a visited array to avoid recomputing reachability for nodes that have already been processed.
        """
        adj_list = defaultdict(list)
        # class: [classes that depend on this class]
        for a, b in prerequisites:
            adj_list[a].append(b)
        reachable = [set() for _ in range(numCourses)]
        visited = [False] * numCourses

        def _helper(course):
            if visited[course]:  # If already processed, return
                return reachable[course]
            visited[course] = True
            for neighbor in adj_list[course]:
                reachable[course].add(neighbor)
                reachable[course].update(_helper(neighbor))
            return reachable[course]

        for i in range(numCourses):
            if not visited[i]:
                _helper(i)
        
        return [v in reachable[u] for u, v in queries]
                