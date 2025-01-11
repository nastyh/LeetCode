class StockSpanner:
    """
    O(n) due to next()
    O(n) due to the stack

    Monotonic decreasing stack: [element, smaller, smaller, smaller]
    Stack has (price, span)
    price is the stock price, span is the num of consecutive days st price <= current price
    """

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        span = 1  # current day is included into the span
        # while non-empty and the last added price <= curr price
        while self.st and self.st[-1][0] <= price:
            # build span since it's the consecutive days with the lower prices 
            span += self.st.pop()[1]
        self.st.append((price, span)) # curr price and calculated span goes to the stack 
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)