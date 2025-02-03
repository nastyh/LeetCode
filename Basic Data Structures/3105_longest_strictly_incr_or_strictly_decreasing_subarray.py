from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        O(n) one path
        O(1) nothing stored
        two vars, one pass
        compare elements
        if it's an upward trend, increase incr_l, zero out decr_l
        and other way around 
        in else cover when numbers are the same 
        every time update res 
        """
        incr_l, decr_l = 1, 1
        res = 1 
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                incr_l += 1
                decr_l = 1 
            elif nums[i] < nums[i-1]:
                decr_l += 1
                incr_l = 1
            else:
                incr_l = 1
                decr_l = 1 
            res = max(res, incr_l, decr_l)
        return res
    