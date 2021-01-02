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


def knapsack_memo_bottom_up(profits, weights, capacity): # both O(NC), N total items, C capacity
    """
    Create a matrix for every capacity and every index and save inside potential profits
    Cols are capacities, rows are indices
    """
    dp = [[0] * (capacity + 1) for y in range(len(profits))]
    if capacity <= 0 or len(profits) == 0 or len(profits) != len(weights):
        return 0
    for row in range(len(profits)):  # first column has only zeros
        dp[row][0] = 0 
    for c in range(0, capacity + 1):  # filling out the first row. If the current weight is <= to the capacity, put the item and collect the profit
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, len(profits)):
        for c in range(1, capacity + 1):
            prof1, prof2 = 0, 0
            if weights[i] <= c:
                prof1 = profits[i] + dp[i - 1][c - weights[i]]  # take the current element and a smaller one that will still fit
            prof2 = dp[i - 1][c]  # not taking the current element but going with what is already in the knapsack (one row above)
            dp[i][c] = max(prof1, prof2)
    return dp[-1][-1]  # the very last cell


def knapsack_bottom_up_alt(profits, weights, capacity):  # both O(NC), N total items, C capacity
    """
    as above with slight changes in filling out dp
    """
    dp = [[0] * (capacity + 1) for y in range(len(profits))]
    if capacity <= 0 or len(profits) == 0 or len(profits) != len(weights):
        return 0
    for col in range(0, capacity + 1):  # first row 
        if weights[0] < col:
            dp[0][col] = profits[0]
    for row in range(1, len(profits)):
        for col in range(1, capacity + 1):
            if col >= weights[row]:
                dp[row][col] = max(dp[row - 1][col], profits[row] + dp[row - 1][col - weights[row]])
    return dp[-1][-1]


def knapsack_memo_bottom_up_efficient(profits, weights, capacity):  # O(NC), N total items, C capacity, space O(2C)
    """
    We don't need to maintain the whole dp matrix but just need one previous row
    """
    if capacity <= 0 or len(profits) == 0 or len(profits) != len(weights):
        return 0
    dp = [[0 for x in range(capacity + 1)] for y in range(2)]  # the only difference is that we use `i % 2` instead if `i` and `(i-1) % 2` instead if `i-1`
    for col in range(0, capacity + 1):
        if weights[0] <= col:
            dp[0][col] = dp[1][col] = profits[0]
    for row in range(1, len(profits)):
        for col in range(1, capacity + 1):
            if weights[row] <= col:
                dp[row % 2][col] = max(profits[row] + dp[(row - 1) % 2][col - weights[row]], dp[(row - 2) % 2][col])
    return dp[(len(profits) - 1) % 2][col]


if __name__ == '__main__':
    # print(knapsack_brute_force([1, 6, 10, 16], [1, 2, 3, 5], 5))
    # print(knapsack_brute_force([4, 5, 3, 7], [2, 3, 1, 4], 5))
    # print(knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack_memo([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(knapsack_memo_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack_memo_bottom_up([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(knapsack_bottom_up_alt([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(knapsack_memo_bottom_up_efficient([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack_bottom_up_alt([1, 6, 10, 16], [1, 2, 3, 5], 5))

