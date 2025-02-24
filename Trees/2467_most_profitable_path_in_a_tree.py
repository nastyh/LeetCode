from collections import defaultdict
import math
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """
        O(n), initial DFS, Bob's path, Alice's path, all O(n)
        O(n), graph representation, arrays, recursive stack, all O(n)
        """
        n = len(amount)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 1: Compute Bob's arrival times using parent pointers.
        parent = [-1] * n
        def dfs(u: int, par: int):
            parent[u] = par
            for v in graph[u]:
                if v == par:
                    continue
                dfs(v, u)
        dfs(0, -1)
        bobTime = [math.inf] * n
        time = 0
        cur = bob
        while cur != -1:
            bobTime[cur] = time
            time += 1
            cur = parent[cur]
        # Step 2: DFS for Alice from node 0 to each leaf.
        maxProfit = -math.inf
        def dfsAlice(u: int, par: int, time: int, currProfit: int):
            nonlocal maxProfit
            # Determine how much profit Alice gets at node u
            if time < bobTime[u]:
                currProfit += amount[u]
            elif time == bobTime[u]:
                currProfit += amount[u] // 2  # split the amount if arriving simultaneously
            # else, Bob has already visited, so Alice gets nothing here.
            
            # If u is a leaf (and not the root), update maxProfit.
            if u != 0 and len(graph[u]) == 1:
                maxProfit = max(maxProfit, currProfit)
            
            # Continue the DFS.
            for v in graph[u]:
                if v == par:
                    continue
                dfsAlice(v, u, time + 1, currProfit)
        
        dfsAlice(0, -1, 0, 0)
        return maxProfit