class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        O(n^2)
        O(n)
        Brute force 
        just two pointers and compare 
        """
        res = prices.copy()
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
        return res
    def finalPrices_monotonic(self, prices: List[int]) -> List[int]:
        """
        O(n) both
        when we find a price that is smaller than some earlier prices,
        it must be the discount for those earlier prices that are larger than it.
        stack must contain all the most recent prices before that element that
        are greater than it. This implies that each element present in the
        stack must be in increasing order of value
        continue popping prices from the stack and applying the discount
        until the stack is empty or the top price is less than the current price.
        Then, we push the current price to the top of the stack, to wait for a discount which may come further down
        """
        res = prices.copy()
        st = deque()
        for i in range(len(prices)):
            while st and prices[st[-1]] >= prices[i]:
                res[st.pop()] -= prices[i]
            st.append(i)
        return res 