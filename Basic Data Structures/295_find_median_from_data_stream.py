class MedianFinder:

    def __init__(self):
        # we are only concerned with the middle situation
        # Let's have to heaps as:
        # [left heap] current number [right heap]
        # left heap: largest element from here is smaller thatn our current number
        # right heap: smallest element from here is larger than our current number
        # heaps' lengths should be different by not more than 1
        self.lh = []
        heapq.heapify(self.lh)  # left heap: return the largest number smaller than current num
        self.rh = []
        heapq.heapify(self.rh)  # right heap: returns the smallest number that is larget than current num

        

    def addNum(self, num: int) -> None:
        # the top of the heaps will comprise the elements we need essentially
        # we just need to keep their sizes not more different than 1
        if len(self.lh) > 0 and num > -self.lh[0]:  # the first element by module is the largest but we'll store with a diff sign since it's a heap
            heapq.heappush(self.rh, num)
            if len(self.rh) > len(self.lh):
                item = heapq.heappop(self.rh)
                heapq.heappush(self.lh, -item)
        else:
            heapq.heappush(self.lh, -num)
            if len(self.lh) - len(self.rh) > 1:
                item = heapq.heappop(self.lh)
                heapq.heappush(self.rh, -item)

    def findMedian(self) -> float:
        # if there are even numbers of elements 
        if len(self.lh) == len(self.rh):
            return (-self.lh[0] + self.rh[0]) / 2 # to the left and to the right
        else:
            return -self.lh[0] # otherwise it's just the middle one

