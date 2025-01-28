from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
        sliding window or two pointers
        start moving r
        if see 0, increment the count of zeroes
        while this val > 1:
        move the left pointer
        if see a zero, decrement the count of zeroes 
        res is the best of what we have and the longest window 
        """
        if len(nums) == 1:
            return 0
        l, num_of_zeroes, res = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_of_zeroes += 1
            while num_of_zeroes > 1:
                if nums[l] == 0:
                    num_of_zeroes -=1
                l += 1
            res = max(res, r - l)
        return res