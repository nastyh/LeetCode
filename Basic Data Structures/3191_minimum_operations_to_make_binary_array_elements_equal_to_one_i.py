from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        O(n) pass once
        O(1) nothing to store
        When you flip a subarray of three, you change the parity (even/odd state)
        of each of the three positions 
        If we see a 0, need to flip to 1. It's a greedy approach starting from the left
        If the remaining portion of the array has a 0 that cannot be flipped (fewer than 3 elements remaining),
        it's impossible to achieve an all-1 array

        Iterate 
        if 0 at index i, flip i+1 and i+2
        update res
        if we arrive to a place where there are zeroes left but fewer than three elements, it's -1
        otherwise, return res
        """
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] ^= 1 # it basically does 0-->1 or 1 -->0 respectively
                nums[i+2] ^= 1
                res += 1
        return res if all(n == 1 for n in nums) else - 1
    
    def minOperations_other(self, nums: List[int]) -> int:
        """
        Same but without a ^ sign but with some extra if statements
        to do 0-->1 or 1-->0
        """
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                if nums[i+1] == 1:
                    nums[i+1] = 0
                else:
                    nums[i+1] = 1
                if nums[i+2] == 1:
                    nums[i+2] = 0
                else:
                    nums[i+2] = 1
                res += 1
        return res if all(n == 1 for n in nums) else - 1


    