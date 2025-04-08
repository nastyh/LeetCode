from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        O(n^2): n interations and n work per iteration
        O(n) for the set 
        after r operations, the array becomes
        remaining = nums[r*3:]
        task is find the smallest r so that all numbers in remaining
        are distinct
        """
        res = 0
        l = len(nums)
        while True:
            start_ix = res * 3
            if start_ix >= len(nums):
                return res 
            remaining = nums[start_ix:]
            if len(set(remaining)) == len(remaining):
                return res 
            res += 1
