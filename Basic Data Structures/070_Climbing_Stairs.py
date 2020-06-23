def stairs(n):
	if n == 1: return 1
	dp = [None] * (n + 1)
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2
	for i in range(3, len(dp)):
		dp[i] = dp[i - 2] + dp[i - 1]
	return dp[n]


if __name__ == '__main__':
	print(stairs(3))