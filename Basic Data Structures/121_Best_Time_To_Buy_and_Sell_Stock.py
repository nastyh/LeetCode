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
