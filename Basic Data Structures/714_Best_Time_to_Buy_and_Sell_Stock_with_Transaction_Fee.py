def maxProfit_dp(self, prices, fee):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash

def maxProfit(prices, fee):
    profit, hold = 0, float('-inf')
    for p in prices:
        hold, profit = max(hold, profit - p), max(profit, hold + p -fee)
    return profit