class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        O(nlogn). Logn to add an element, for the whole nums it's nlogn
        O(n) due to two heaps
        sliding window 
        greatest abs diff is always between the largest and the smallest elements in the subarray
        if this diff under the limit, then everything inside is under the limit, too 
        max heap to store potential maximum values and a min heap to store potential minimum values.
        If the absolute difference between these values exceeds the limit, we move the left pointer to exclude
        the element with the lower index. This removes the violating element from the window.
        keep the heaps updated by deleting elements outside the new window after moving the left pointer.
        This requires storing the indices of elements along with their values in the heap.
        """
        l = 0
        res = -math.inf
        max_h, min_h = [], []
        for r in range(len(nums)):
            heapq.heappush(max_h, (-nums[r], r))
            heapq.heappush(min_h, (nums[r], r))
            # absolute diff between the maximum and minimum values in the current window exceeds the limit
            while -max_h[0][0] - min_h[0][0] > limit:
                # remove the element causing the violation
                l = min(max_h[0][1], min_h[0][1]) + 1
                # Remove elements from the heaps that are outside the current window
                while max_h[0][1] < l:
                    heapq.heappop(max_h)
                while min_h[0][1] < l:
                    heapq.heappop(min_h)
            
            res = max(res, r - l + 1) # build the result 
        return res