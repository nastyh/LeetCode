def stairs(n):
	if n == 1:
		return 1
	dp = [None] * (n + 1)
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2
	for i in range(3, len(dp)):
		dp[i] = dp[i - 2] + dp[i - 1]
	return dp[n]


def stairs_alt(n):
	if n <= 2:
		return n 
	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2
	for i in range(3, n + 1):
		dp[i] = dp[i - 2] + dp[i - 1]
	return dp[-1]
	
	
if __name__ == '__main__':
	print(stairs(3))
	print(stairs(4))
	print(stairs(5))
	print(stairs_alt(3))
	print(stairs_alt(4))
	print(stairs_alt(5))