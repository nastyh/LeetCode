"""
Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the profit.
We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.
Example:

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5

Output: 14 (two pieces of length  and one piece of length 1)
"""

def rod_cutting(lengths, prices, n):  # O(len(lenghts) * (n + 1))
    """
    2d array
    Start filling out. Every time make a decision: take current prices[row] and whatever fits afterwards
    or don't take and just select the previous iteration from the row above 
    """
    dp = [[0] * (n + 1) for _ in range(len(lengths))]
    for row in range(len(lengths)):
        for col in range(1, n + 1):
            _take, _no_take = 0, 0  # need to have this line, won't work otherwise
            if lengths[row] <= col:
                _take = prices[row] + dp[row][col - lengths[row]]
            if row > 0:  # edge case for the first row, we can't go higher
                _no_take = dp[row - 1][col]
            else:
                _no_take = 0
            dp[row][col] = max(_take, _no_take)
    return dp[-1][-1]


if __name__ == '__main__':
    print(rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))