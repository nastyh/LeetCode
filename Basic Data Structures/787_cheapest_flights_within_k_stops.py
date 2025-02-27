import math
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        O((k+1)*E) simplifies to O(k*E)
        runs k+1 times since it's up to k+1 flights to k stops
        Then there are E flights 
        O(n) due to dp of size n

        modified version of the Bellman–Ford algorithm
        The key idea is that having at most k stops means you can take at most k + 1 flights.
        In each iteration, you “relax” all the flights (i.e. try to update the cost to reach each destination)
        but only using one more flight than in the previous iteration.
        """
        dp = [math.inf] * n 
        dp[src] = 0
        for i in range(k + 1):
            temp = dp.copy()
            for u, v, w in flights:
                if dp[u] == math.inf:
                    continue
                if dp[u] + w < temp[v]:
                    temp[v] = dp[u] + w
            dp = temp
        return -1 if dp[dst] == math.inf else dp[dst]