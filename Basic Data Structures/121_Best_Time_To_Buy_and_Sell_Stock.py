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
