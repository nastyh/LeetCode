import heapq
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:  # O(n(logn)) and O(1)
        # greedy approach
        # sort first since we want to fit as many as possible
        sorted_weight = sorted(weight)
        max_w = 5000
        res, curr_w = 0, 0
        for w in sorted_weight:
            if curr_w + w <= max_w: # this is the trick
                # otherwise we won't catch when it's 4150 but then we add 1000 and go over
                curr_w += w
                res += 1
        return res
    
    def maxNumberOfApples_heap(self, weight: List[int]) -> int:  # O(N + Klogn) and O(N)
        # tiny change: using a min heap instead of sorting
        heapq.heapify(weight)
        max_w = 5000
        res, curr_w = 0, 0
        for _ in range(len(weight)):
            curr_el = heapq.heappop(weight) # taking the current element 
            if curr_w + curr_el <= max_w: 
                curr_w += w 
                res += 1
        return res 
