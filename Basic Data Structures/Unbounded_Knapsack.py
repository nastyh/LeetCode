def unbounded_knapsack(profit, weight, capacity):  # O(N*capacity) both, where N = len(profit)
    dp = [[0] * (capacity + 1) for _ in range(len(profit))]
    for col in range(1, capacity + 1):  # first row
        if weight[0] <= col:
            dp[0][col] = profit[0] + dp[0][col - weight[0]]
    for row in range(1, len(profit)):  # starting from cell (1, 1)
        for col in range(1, capacity + 1):
            if weight[row] > col:  # if current weight is larger than the capacity
                dp[row][col] = dp[row - 1][col]  # don't take, but go with the previous choice
            else:  # otherwise, choose the max between the previous choice and taking the current profit and whatever the profit is from the leftovers above
                dp[row][col] = max(dp[row - 1][col], dp[row - 1][col - weight[row]] + profit[row])
    return dp[-1][-1]


if __name__ == '__main__':
    print(unbounded_knapsack([15, 20, 50], [1, 2, 3], 5))
    print(unbounded_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))