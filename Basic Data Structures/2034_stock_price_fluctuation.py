class StockPrice:

    def __init__(self):
        """
        O(nlogn) -- add n items, each takes logn time
        O(n) due to the dict
        heaps to keep the lowest and highest prices
        we get a new price, we push it into each heap 
        and only while getting the top element we need to verify if the price is correct or outdated.
        The dict is for that 
        when we get a tuple (ts, price), we check if this ts exists in the ds. 
        if yes, means we overwrite. 
        if no, just add to the dict 
        when looking for min/max prices, we check whether top of the heap == d[ts] 
        if no, it's outdated, throw it away and keep looking
        if yes, we're good 
        """
        self.latest_time = 0
        self.d = {}
        self.max_h = []
        self.min_h = []
    
    def update(self, timestamp: int, price: int) -> None:
        self.d[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
    
        heapq.heappush(self.min_h, (price, timestamp)) # lowest price at this timestamp
        heapq.heappush(self.max_h, (-price, timestamp)) # highest price at this timestamp

    def current(self) -> int:
        # overall latest price
        return self.d[self.latest_time]
 
    def maximum(self) -> int:
        price, ts = self.max_h[0] # take the top element
        # while price in the heap doesn't match one in the dict, keep popping
        while -price != self.d[ts]:
            heapq.heappop(self.max_h)
            price, ts = self.max_h[0]
        return -price

    def minimum(self) -> int:
        price, ts = self.min_h[0] # take the top element
        # while price in the heap doesn't match one in the dict, keep popping
        while price != self.d[ts]:
            heapq.heappop(self.min_h)
            price, ts = self.min_h[0]
        return price
