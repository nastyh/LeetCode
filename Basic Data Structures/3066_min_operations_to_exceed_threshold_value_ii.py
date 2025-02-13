import heapq
from typing import List


class Solution:
    def minOperations_optimal(self, nums: List[int], k: int) -> int:
        """
        O(NlogN), len of nums
        O(N), heap has everything 
        Throw into heap
        Start processing, key here is the while loop's condition
        It defines when we stop 
        We stop when the smallest becomes >= k
        take two smallest out, make an operation, return the result to the heap
        increment res
        Finally return res
        """
        h = []
        res = 0
        for num in nums:
            heapq.heappush(h, num)
        while h[0] < k:
            smallest_1 = heapq.heappop(h)
            smallest_2 = heapq.heappop(h)
            heapq.heappush(h, min(smallest_1, smallest_2) * 2 + max(smallest_1, smallest_2))
            res += 1
        return res
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        O(NlogN), len of nums
        O(N), heap has everything 
        Throw into heap
        Start processing, key here is the while loop's condition
        It defines when we stop 
        check the condition to return res
        take two smallest out, make an operation, return the result to the heap
        increment res
        Finally return res
        """
        h = []
        res = 0
        for num in nums:
            heapq.heappush(h, num)
        while len(h) >= 2:
            if all(n >= k for n in h): return res
            smallest_1 = heapq.heappop(h)
            smallest_2 = heapq.heappop(h)
            heapq.heappush(h, min(smallest_1, smallest_2) * 2 + max(smallest_1, smallest_2))
            res += 1
        return res