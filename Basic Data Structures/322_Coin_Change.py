def coinchange(coins, target):
	dp = [float('inf')] * (target + 1)
	dp[0] = 0
	for coin in coins:
		for x in range(coin, target + 1):
			dp[x] = min(dp[x], dp[x - coin] + 1)
	return dp[target] if dp[target] != float('inf') else -1 


def coinchange_bottoms_up(coins, target):
	dp = [[0] * (target + 1) for _ in range(len(coins))]
	for row in range(len(coins)):  # first col
		dp[row][0] = 1
	for row in range(len(coins)):
		for col in range(1, target):


if __name__ == '__main__':
	print(coinchange([1,2,5], 11))
	print(coinchange([2], 3))



