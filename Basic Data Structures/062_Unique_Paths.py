def uniquePaths(m, n):
    dp = [[1 for j in range(m)] for i in range(n)]
    for i in range(1, n):
	    for j in range(1, m):
		    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


def uniquePath_recur(m, n):
    if m == 1 or n == 1:
	    return 1 
    return uniquePath_recur(m - 1, n) + uniquePath_recur(m, n - 1)


def uniquePath_another_dp(m, n):
    dp = [[0 for j in range(m)] for i in range(n)]
    for col in range(1, len(dp[0])):
        dp[0][col] = 1
    for row in range(1, len(dp)):
        dp[row][0] = 1
    for r in range(1, n):
        for c in range(1, m):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    # print(uniquePaths(3,2))
    # print(uniquePath_recur(3,2))
    print(uniquePath_another_dp(3, 2))
    print(uniquePath_another_dp(3, 7))

