class Solution:
    def countGoodStrings_dp(self, low: int, high: int, zero: int, one: int) -> int:
        """
        O(high) both 
        """
        mod = 10**9 + 7
        dp = [1] + [0] * high
        for e in range(1, high + 1):
            if e >= zero: 
                dp[e] += dp[e - zero]
            if e >= one:
                dp[e] += dp[e - one]
            dp[e] %= mod 
        return sum(dp[low: high + 1]) % mod
