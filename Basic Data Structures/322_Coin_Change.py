def coinchange(coins, target):
	dp = [float('inf')] * (target + 1)
	dp[0] = 0
	for coin in coins:
		for x in range(coin, target + 1):
			dp[x] = min(dp[x], dp[x - coin] + 1)
	return dp[target] if dp[target] != float('inf') else -1 


def coinchange_bottoms_up(coins, target):  # doesn't work
	dp = [[0] * (target + 1) for _ in range(len(coins))]
	for col in range(1, target + 1):  # first row
		if coins[0] <= col:
			dp[0][col] = 1 + dp[0][col - coins[0]]
	print(dp)
	for row in range(1, len(coins)):
		for col in range(1, target + 1):
			if coins[row] > col:
				dp[row][col] = dp[row - 1][col]
			else:
				dp[row][col] = min(dp[row - 1][col], 1 + dp[row][col - coins[row]])
	# print(dp)
	return dp[-1][-1] if dp[-1][-1] != 0 else -1


def coinchange_bottoms_up_alt(denominations, total):  # doesn't work
	n = len(denominations)
	dp = [[0 for _ in range(total+1)] for _ in range(n)]

	# populate the total = 0 columns, as we will always have an empty set for zero total
	for i in range(n):
		dp[i][0] = 1

	# process all sub-arrays for all capacities
	for i in range(n):
		for t in range(1, total+1):
			if i > 0:
				dp[i][t] = dp[i - 1][t]
			if t >= denominations[i]:
				dp[i][t] += dp[i][t - denominations[i]]

	# total combinations will be at the bottom-right corner.
	return dp[-1][-1] if dp[-1][-1] != 0 else -1



if __name__ == '__main__':
	# print(coinchange([1, 2, 5], 11))
	# print(coinchange([2], 3))
	print(coinchange_bottoms_up([1, 2, 5], 11))
	print(coinchange_bottoms_up([2], 3))
	print(coinchange_bottoms_up_alt([1, 2, 5], 11))
	print(coinchange_bottoms_up_alt([2], 3))



