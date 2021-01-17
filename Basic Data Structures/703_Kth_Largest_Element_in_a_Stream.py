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
    def __init__(self, k, nums):
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


class KthLargest:
    """
    Slightly different implementation of the heap idea
    It is initialized with a list nums and with a number k. We need to only keep k largest numbers
    in this list 

    """
   def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
            
    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
        return self.heap[0] 


class KthLargest:  # O(nlogk) and O(logk)
    """
    Optimal solution:
    iterate through original nums and build a heap of size k
    In the add() function:
    if the incoming value is larger than the smallest value, add the incoming and remove the smallest
    Otherwise just add 
    Always return the smallest
    """
    def __init__(self, k, nums):
        self.h = []
        self.k = k
        for num in nums:
            if len(self.h) < self.k:
                heapq.heappush(self.h, num)
            else:
                heapq.heappushpop(self.h, num)
    
    def add(self, val):
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            if val > self.h[0]:
                heapq.heappushpop(self.h, val)
        return self.h[0]

