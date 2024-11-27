import math
def coinchange(coins, target):  # O(mn) and O(n) where m is len(coins) and n is target
	dp = [float('inf')] * (target + 1)
	dp[0] = 0
	for coin in coins:
		for x in range(coin, target + 1):
			dp[x] = min(dp[x], dp[x - coin] + 1) # +1 means taking one more coin and working with the rest of the sum
	return dp[target] if dp[target] != float('inf') else -1 


def coinchange_bottoms_up(coins, target):  # doesn't work
	if target == 0: return 0
	dp = [[0] * (target + 1) for _ in range(len(coins))]
	for col in range(1, target + 1):  # first row
		if coins[0] <= col:
			if col % coins[0] == 0:
				dp[0][col] = 1 + dp[0][col - coins[0]]
	# print(dp)
	for row in range(1, len(coins)):
		for col in range(1, target + 1):
			if coins[row] > col:
				dp[row][col] = dp[row - 1][col]
			else:
				dp[row][col] = min(dp[row - 1][col], 1 + dp[row][col - coins[row]])
	# print(dp)
	return dp[-1][-1] if dp[-1][-1] != 0 else -1


def coinchange_bottoms_up_alt(coins, target):
	dp = [[float("inf") for x in range(target + 1)] for y in range(len(coins) + 1)]
	for i in range(1, len(coins) + 1):
		dp[i][0] = 0
	for i in range(len(coins) + 1):
		for j in range(target + 1):
			if coins[i - 1] <= j:
				dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[-1][-1] if dp[-1][-1] != float("inf") else -1


def coinchange_bottoms_up_alt_another(coins, target):
	"""
	dp with an extra col and an extra row; initially all zeros
	first column is all zeros (need no coins to achieve the target of 0)
	first row is all math.inf (to handle edge cases)
	the main portion starts from the cell (1, 1)
	accurate with indices for rows because coins start at index 1, not 0
	"""
	dp = [[0] * (target + 1) for _ in range(len(coins) + 1)]
	for row in range(len(coins) + 1):  # first col
		dp[row][0] = 0
	for col in range(1, target + 1):  # first row separately
		dp[0][col] = math.inf
	for row in range(1, len(coins) + 1):  # main portion
		for col in range(1, target + 1):
			if col < coins[row - 1]:
				dp[row][col] = dp[row - 1][col]  # careful with indices
			else:
				dp[row][col] = min(dp[row - 1][col], dp[row][col - coins[row - 1]] + 1) # careful with indices
	return dp[-1][-1] if  dp[-1][-1] != math.inf else -1



if __name__ == '__main__':
	# print(coinchange([1, 2, 5], 11))
	# print(coinchange([2], 3))
	print(coinchange_bottoms_up([1, 2, 5], 11))
	print(coinchange_bottoms_up([2], 3))
	print(coinchange_bottoms_up([1], 1))
	print(coinchange_bottoms_up([1], 2))
	print(coinchange_bottoms_up([1, 5, 6, 8], 11))
	# print(coinchange_bottoms_up_alt([1, 2, 5], 11))
	# print(coinchange_bottoms_up_alt([2], 3))
	print(coinchange_bottoms_up_alt_another([1, 2, 5], 11))
	print(coinchange_bottoms_up_alt_another([2], 3))



