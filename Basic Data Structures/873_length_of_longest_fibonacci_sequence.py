from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        O(n^2) due to two loops
        O(n^2) due to a 2d array
        2D DP table, where for every pair of indices (i, j) with i < j, we try to find an index k (with k < i) such that:
        arr[k] + arr[i] == arr[j]
        If such a k exists, then we can extend a Fibonacci-like sequence ending with arr[k] and arr[i] by including arr[j]
        We define dp[i][j] as the length of the Fibonacci-like subsequence ending with arr[i] and arr[j]. 
        any two numbers form a trivial sequence of length 2, so the default value is 2.
        update dp[i][j] as:
        dp[i][j] = dp[k][i] + 1
        and keep track of the maximum length
        """
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        # dp[i][j] will store the length of the Fibonacci-like subsequence ending with arr[i] and arr[j]
        dp = [[2] * n for _ in range(n)]
        res = 0

        for j in range(n):
            for i in range(j):
                # The potential previous number in the sequence should be arr[j] - arr[i]
                k = index.get(arr[j] - arr[i])
                if k is not None and k < i:
                    dp[i][j] = dp[k][i] + 1
                    res = max(res, dp[i][j])
        
        return res if res >= 3 else 0