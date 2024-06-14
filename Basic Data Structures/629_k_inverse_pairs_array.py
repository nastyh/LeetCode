class Solution:
    def kInversePairs_recursive(self, n: int, k: int) -> int:
        """
        O(N*K) both
        For example, if n is 3, you have these possible arrangements:
        1, 2, 3 -> no bigger number comes before a smaller number, so the count is 0
        1, 3, 2 -> only 3 comes before 2, so the count is 1
        2, 1, 3 -> only 2 comes before 1, so the count is 1
        2, 3, 1 -> 2 comes before 1, and 3 comes before 1, so the count is 2
        3, 1, 2 -> 3 comes before 1, and 3 comes before 2, so the count is 2
        3, 2, 1 -> 3 comes before 2, 3 comes before 1, and 2 comes before 1, so the count is 3
        How many ways to arrange n numbers with k pairs of numbers that are out of order?
        It is equal to the sum of:
        How many ways to arrange n - 1 numbers with k pairs of numbers that are out of order, and then add n to the end.
        This does not change the number of pairs of numbers that are out of order, because n is bigger than all the other numbers and it is at the end.

        How many ways to arrange n numbers with k - 1 pairs of numbers that are out of order, and then remove n from the end. 
        This reduces the number of pairs of numbers that are out of order by 1, because n is bigger than all the other numbers and it
        removes one pair of numbers that are out of order with the last number in the original arrangement.
        How many ways to arrange n - 1 numbers with k - n pairs of numbers that are out of order, and then add 1 to the end.
        This increases the number of pairs of numbers that are out of order by n - 1, because 1 is smaller than all the other numbers and it creates n - 1 pairs of numbers that are out of order with the last number in the original arrangement.

        Edge cases
        If k is 0, then there is only one way to arrange the numbers in increasing order, like 1, 2, 3. So the function returns 1.
        If k is negative, then there is no way to arrange the numbers that has a negative number of times that a bigger number comes before a smaller number. Return 0.
        If n is 1, then there is only one element in an array - it is not possible to creae a pair from 1 element. Return 0.
        """
        MOD = 10**9 + 7
        @cache
        def dp(n, k):
            if k == 0:
                # there is exactly one way to arrange the array (in increasing order)
                return 1
            if k < 0:
                # k in negative area - ivalid
                return 0
            if n == 1:
                # can't create any (k) pairs if array has only 1 element
                return 0
            
            return (dp(n - 1, k) + dp(n, k - 1) - dp(n - 1, k - n)) % MOD
        return dp(n, k)

        def kInversePairs_dp(self, n: int, k: int) -> int:
            """
            O(n * k) both
            dp[i][j] represents the number of sequences of length i with exactly j inverse pairs.
            This recurrence relation considers two cases:
            one where the current element is not part of an inverse pair (dp[i-1][j])
            and another where it is part of an inverse pair (dp[i][j-1]).
            Additionally, it adjusts for cases where j >= i to exclude invalid inverse pairs.
            """
            dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
            dp[0][0] = 1
            for i in range(1, n+1):
                dp[i][0] = 1
                for j in range(1, k+1):
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % (10**9 + 7)
                    if j >= i:
                        dp[i][j] = (dp[i][j] - dp[i-1][j-i]) % (10**9 + 7)
            return dp[n][k]