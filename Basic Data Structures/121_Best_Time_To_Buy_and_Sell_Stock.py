class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gl_max = 0
        if len(prices) < 2:
            return gl_max

        loc_min = prices[0]
        for k in prices[1:]:
            loc_min = min(k, loc_min)
            gl_max = max(gl_max, k-loc_min)
        return gl_max

    def maxProfit_another(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price = float('inf')
        profit = 0
        for p_ix in range(len(prices)):
            if prices[p_ix] < min_price:
                min_price = prices[p_ix]
            elif prices[p_ix] - min_price > profit:
                profit = prices[p_ix] - min_price
        return profit

    def maxProfit_best(stock_prices):
        if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')
        min_price  = stock_prices[0]
        max_profit = stock_prices[1] - stock_prices[0]

        for current_time in range(1, len(stock_prices)):
            current_price = stock_prices[current_time]

        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

        return max_profit
