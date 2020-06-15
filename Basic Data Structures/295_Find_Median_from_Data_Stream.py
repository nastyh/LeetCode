import bisect, heapq
class MedianFinder: # easy way: using bisect

    def __init__(self):
        self.l = []
        self.size = 0


    def addNum(self, num: int) -> None:
        bisect.insort_right(self.l, num)
        self.size += 1


    def findMedian(self) -> float:
        m_ix = self.size // 2
        if self.size % 2 == 1:
            return self.l[m_ix]
        else:
            return (self.l[m_ix - 1] + self.l[m_ix]) / 2


class MedianFinder_heap:
    def __init__(self):
        self.lh = []
        self.rh = []
        heapq.heapify(self.lh)
        heapq.heapify(self.rh)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.rh, -heapq.heappushpop(self.lh, num))
        if len(self.rh) > len(self.lh):
            heapq.heappush(self.lh, -heapq.heappop(self.rh))

    def findMedian(self) -> float:
        even_number_of_elements = len(self.lh) == len(self.rh)
        if even_number_of_elements:
            return (self.lh[0] + (-self.rh[0]))/2
        else:
            return self.lh[0]




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
