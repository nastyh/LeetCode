def countVowelStrings_dp(n):  # O(n) and O(5n)
    """
    for any n, create a 2d array with 5 columns and n rows
    store the cumulative sum values 
    the sum of the last row is the answer
    """
    dp = [[0 for j in range(5)] for i in range(n)]
    for i in range(5):
        dp[0][i] = 1
    for i in range(n):
        dp[i][0] = 1
    for i in range(1, n):
        for j in range(5):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return sum(dp[n - 1])


def countVowelStrings_math(n):  # O(1) both
    """
    You can place any letter in the first position
    Only 4 positions for the next letter, etc.
    """
    return int((n + 1) * (n + 2) * (n + 3) * (n + 4) / 24)


def countVowelStrings_dfs(n):  # probably O(n^5) and O(n) for the recursion stack
    ans = 0
    def dfs(c, idx):
        if c == n:
            self.ans += 1
            return
        else:
            for i in range(idx, 5):
                dfs(c + 1, i)
    dfs(0, 0)
    return ans