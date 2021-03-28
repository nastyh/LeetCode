"""
You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change
for a given amount of money. For example, Canada has given up the 1-cent penny. If you're owed 94 cents in Canada, a shopkeeper will graciously supply you
with 95 cents instead since there exists a 5-cent coin.
Given a list of the available denominations, determine if it's possible to receive exact change for an amount of money targetMoney.
Both the denominations and target amount will be given in generic units of that currency.

denominations = [5, 10, 25, 100, 200]
targetMoney = 94
output = false
Every denomination is a multiple of 5, so you can't receive exactly 94 units of money in this currency.

denominations = [4, 17, 29]
targetMoney = 75
output = true
You can make 75 units with the denominations [17, 29, 29].
"""


def canGetExactChange(targetMoney, denominations):  # O((targetMoney + 1) * len(denominations)) both 
  """
  Essentially it's an unbounded knapsack problem but with True/False instead of numbers
  """
  dp = [[False] * (targetMoney + 1) for _ in range(len(denominations))]
  for col in range(1, targetMoney + 1):  # have exactly one coin to work with 
    if denominations[0] <= col:  # if this coin is smaller than the current targetMoney
      if col % denominations[0] == 0:  # if I can get to targetMoney only using this one coin
        dp[0][col] = True 
  for row in range(1, len(denominations)):
    for col in range(1, targetMoney + 1):
      if denominations[row] > col:  # if the current coin is too large
        dp[row][col] = dp[row - 1][col]  # don't take it 
      else:  # if the current coin is <= to the current target 
        dp[row][col] = dp[row - 1][col] or dp[row][col - denominations[row]]  # either still don't take it or take it and look to the left: whether the leftovers can make it 
  return dp[-1][-1]


def canGetExactChange_space_efficient(targetMoney, denominations):  # O((targetMoney + 1) * len(denominations)) and  O((targetMoney + 1) * 2)
    """
    Optimized b/c we only need to rows of data 
    """
    dp = [[False] * (targetMoney + 1) for _ in range(2)]
    for col in range(1, targetMoney + 1):  # have exactly one coin to work with 
        if denominations[0] <= col:  # if this coin is smaller than the current targetMoney
            if col % denominations[0] == 0:  # if I can get to targetMoney only using this one coin
                dp[0][col] = True 
    for row in range(1, len(denominations)):
        for col in range(1, targetMoney + 1):
            if denominations[row] <= col:
                dp[row % 2][col] = dp[(row - 1) % 2][col] or dp[(row) % 2][col - denominations[row]]
    return dp[(len(denominations) - 1) % 2][col]


if __name__ == '__main__':
    print(canGetExactChange(94, [5, 10, 25, 100, 200]))
    print(canGetExactChange(75, [4, 17, 29]))
    print(canGetExactChange(15, [5, 10, 20]))
    print(canGetExactChange_space_efficient(94, [5, 10, 25, 100, 200]))
    print(canGetExactChange_space_efficient(75, [4, 17, 29]))
    print(canGetExactChange_space_efficient(15, [5, 10, 20]))