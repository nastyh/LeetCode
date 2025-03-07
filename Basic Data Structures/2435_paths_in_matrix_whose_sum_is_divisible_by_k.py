from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        """
        O(mnk), sizes* k possible remainders 
        Same for size due to the 3d dp list
        dp[i][j][r] is the number of ways to reach cell (i, j) such that the sum modulo k is r.
        From cell (i, j) with a remainder r, you can move:
        Down to (i + 1, j), updating the new remainder as (r + grid[i+1][j]) % k.
        Right to (i, j + 1), updating the new remainder as (r + grid[i][j+1]) % k.
        Accumulate the number of ways for each new remainder, taking modulo 10^9 + 7 at each update.
        dp[m-1][n-1][0], which represents the number of paths reaching the bottom-right cell
        where the total sum is divisible by k.
        """
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        # Initialize dp table with dimensions m x n x k
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Start from (0, 0) with the initial remainder
        dp[0][0][grid[0][0] % k] = 1
        
        # Iterate over all cells
        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if dp[i][j][r] > 0:
                        # Move Down if possible
                        if i + 1 < m:
                            newR = (r + grid[i+1][j]) % k
                            dp[i+1][j][newR] = (dp[i+1][j][newR] + dp[i][j][r]) % mod
                        # Move Right if possible
                        if j + 1 < n:
                            newR = (r + grid[i][j+1]) % k
                            dp[i][j+1][newR] = (dp[i][j+1][newR] + dp[i][j][r]) % mod
                            
        return dp[m-1][n-1][0]