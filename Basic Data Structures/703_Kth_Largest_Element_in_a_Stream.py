# brute force
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums


    def add(self, val: int) -> int:
        self.nums.append(val)
        res = sorted(self.nums, reverse = True)
        return res[self.k - 1]




# using heap
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap,i)
            else:
                if i > self.heap[0]:
                    heapq.heappushpop(self.heap,i)


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap,val)
        return self.heap[0]
