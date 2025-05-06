from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        O(n) both
        nums[i] gives an index 
        then fill out res one by one
        """
        res = [None] * len(nums)
        for i in range(len(nums)):
            candidate = nums[i]
            res[i] = nums[candidate]
        return res
    
    def buildArray_efficient(self, nums: List[int]) -> List[int]:
        """
        O(n)
        O(1)
        Encode two numbers into each slot.
        Extract the new values.
        """
        for i in range(len(nums)):
            nums[i] += len(nums) * (nums[nums[i]] % len(nums))
        for i in range(len(nums)):
            nums[i] //= len(nums)                        # keep only the encoded answer
        return nums
    
    def buildArray_one_liner(self, nums: List[int]) -> List[int]:
        """
        O(n)
        O(1)
        fastest, actually 
        """
        return [nums[_] for _ in nums]