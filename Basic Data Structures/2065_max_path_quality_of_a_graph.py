import collections
from typing import List

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        """
        O(b^n), where b is the max branching factor, n num of nodes
        O(n+e), e is the num of edges
        graph contains the neighbors of a node a in graph[a]
        time is the dict contains the time traversals between all the combinations: a->b, or b->a
        """
        graph = collections.defaultdict(set)
        time = {}
        for a, b, t in edges:
            time[(a,b)] = t
            time[(b,a)] = t
            graph[a].add(b)
            graph[b].add(a)
        ans  = 0
        def dfs(root, t, visit, s):
            """
            t -- total traversal time
            visit -- what we've seen
            s -- cumulative path quality (sum of node values)
            """
            if t > maxTime:
                return
            if root == 0:
                nonlocal ans
                ans = max(ans, s)
            visit.add(root)
            for v in graph[root]:
                if v not in visit:
                    dfs(v, t+time[(root,v)], set(visit), s+values[v])
                else:
                    dfs(v,t+time[(root,v)], set(visit), s)
        
        
        dfs(0,  0, set(), values[0])