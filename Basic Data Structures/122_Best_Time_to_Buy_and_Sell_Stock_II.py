class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                m_profit += prices[i] - prices[i-1]
        return m_profit
