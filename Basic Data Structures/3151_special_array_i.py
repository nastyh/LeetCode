from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        O(n) to traverse nums once
        O(1) nothing to store
        Just compare pair by pair
        if you have "even even" or "odd odd", it's False
        """
        if len(nums) == 1: return True
        for ix in range(1, len(nums)):
            if (nums[ix - 1] % 2 == 0 and nums[ix] % 2 == 0) or (nums[ix - 1] % 2 == 1 and nums[ix] % 2 == 1):
                return False
        return True
    
    def isArraySpecial_bits(self, nums: List[int]) -> bool:
        """
        O(n) to traverse nums once
        O(1) nothing to store
        We have 0 for evens and 1 for odds 
        0 xor 0 = 0. 1 xor 1 = 0
        1 xor 0 or 0 xor 1 is 1. 
        So if we have 0, it means it's either two odds or two evens next to each other
        return False
        Otherwise, return True at the end 
        """
        if len(nums) == 1: return True
        for ix in range(1, len(nums)):
            if (nums[ix - 1] % 2) ^ (nums[ix] % 2) == 0: return False
        return True 