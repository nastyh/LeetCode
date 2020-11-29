def knapsack_brute_force(profits, weights, capacity):  # O(2^n) and O(n)
    def _helper(profits, weights, capacity, ix):
        if capacity <= 0 or ix >= len(profits):
            return 0
        profit1 = 0
        if weights[ix] <= capacity:
            profit1 = profits[ix] + _helper(profits, weights, capacity - weights[ix], ix + 1)
        profit2 = _helper(profits, weights, capacity, ix + 1)
        return max(profit1, profit2)
    return _helper(profits, weights, capacity, 0)


def knapsack_memo(profits, weights, capacity):  # O(N*C) and O(N*C) where N is the number of items and C is capacity
    """
    Create a matrix for every capacity and every index and save inside potential profits
    Cols are capacities, rows are indices
    """
    dp = [[None] * (capacity + 1) for y in range(len(profits))]
    def _helper(dp, profits, weights, capacity, ix):
        if capacity <= 0 or ix >= len(profits):
            return 0
        if dp[ix][capacity] is not None:
            return dp[ix][capacity]
        profit1 = 0
        if weights[ix] <= capacity:
            profit1 = profits[ix] + _helper(dp, profits, weights, capacity - weights[ix], ix + 1)
        profit2 = _helper(dp, profits, weights, capacity, ix + 1)
        dp[ix][capacity] = max(profit1, profit2)
        return dp[ix][capacity]
    return _helper(dp, profits, weights, capacity, 0)


def knapsack_memo_bottom_up(profits, weights, capacity):
    """
    Create a matrix for every capacity and every index and save inside potential profits
    Cols are capacities, rows are indices
    """
    dp = [[0] * (capacity + 1) for y in range(len(profits))]
    if capacity <= 0 or len(profits) == 0 or len(profits) != len(weights):
        return 0
    for row in range(len(profits)):  # first column has only zeros
        dp[row][0] = 0 
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, len(profits)):
        for c in range(1, capacity + 1):
            prof1, prof2 = 0, 0
            if weights[i] <= c:
                prof1 = profits[i] + dp[i - 1][c - weights[i]]
            prof2 = dp[i - 1][c]
            dp[i][c] = max(prof1, prof2)
    return dp[-1][-1]  # the very last cell


if __name__ == '__main__':
    print(knapsack_brute_force([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack_brute_force([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack_memo([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(knapsack_memo_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack_memo_bottom_up([4, 5, 3, 7], [2, 3, 1, 4], 5))

