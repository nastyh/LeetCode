import math
def maxProfit_dp(prices, fee):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash

def maxProfit(prices, fee):  # O(N) and O(1)
    profit, hold = 0, -math.inf
    for p in prices:
        hold, profit = max(hold, profit - p), max(profit, hold + p - fee)
    return profit


def maxProfit_greedy(prices, fee):   # O(N) and O(1)
    """
    Start w/ the second element
    If the current price is smaller than the minimum, update the minimum
    If the current price is > that minimum + fee, then make a transaction (it goes to ans)
    and update minimum
    """
    n = len(prices)
    if n < 2:
        return 0
    ans = 0
    minimum = prices[0]
    for i in range(1, n):
        if prices[i] < minimum:
            minimum = prices[i]
        elif prices[i] > minimum + fee:
            ans += prices[i] - fee - minimum
            minimum = prices[i] - fee
    return ans


def maxProfit_dp_another(prices, fee):  # O(n) both
    """
    don't have a stock denoted by dp[i][0]
    have a stock denoted by dp[i][1]
     if you don't have a stock, it means
    a) either you didn't have it on the previous day and doing no transactions today or
    b) had a stock from previous day and selling it today plus paying the fees for the transaction
    the above can be written as below ::
    dp[i][0] = max ( dp[i-1][0], dp[i-1][1] + prices[i] - fee)
    since our goal is to have maximum profit, we take max

    if you have a stock, it means
    a) either you had it on the previous day and doing no transactions today or
    b) had no stock on previous day and buying it today
    the above can be written as below ::
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    since our goal is to have maximum profit, we take max
    """
    dp = [[0 for _ in range(2)] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] =  - prices[0]
    for i in range(1,len(prices)):
        dp[i][0] = max ( dp[i-1][0], dp[i-1][1] + prices[i] - fee)
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    return dp[-1][0]