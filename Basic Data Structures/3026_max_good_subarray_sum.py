import math
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        O(n)
        prefix_sum list where at each element we keep the running sum 
        of everything to the left. It's one element longer than nums b/c the first value 
        will be zero
        for i, j, we can compute the sum of elements between i and j by 
        prefix_sum[j+1] - prefix_sum[i]
        
        d has a key of num, and the best index for this num we found so far
        The best is w/ the min prefix sum up to this value 
        when considering a certain element n in nums as the start/end of the current subarray,
        the only possible end/start values for the current subarray to form a "good subarray" are n - k and n + k.
        For each of these two values, we use the hash map to locate its best index we have found so far,
        use that index and the prefix sum array to get the subarray sum, and update the result if needed.
        """
        s = 0
        psum = [0]
        h = {}
        res = -math.inf
        for i, n in enumerate(nums):
            s += n
            psum.append(s)
            if h.get(n - k) != None:
                res = max(s - psum[h[n - k]], res)
            if h.get(n + k) != None:
                res = max(s - psum[h[n + k]], res)
            if h.get(n) == None or psum[h[n]] > psum[-2]:
                h[n] = i
        return res if res != -math.inf else 0