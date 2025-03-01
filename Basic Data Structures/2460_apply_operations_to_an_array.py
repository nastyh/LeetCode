from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        O(n) and O(1)
        two steps
        first is to compare and increment
        Second is to move all the zeroes to the left
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        """
        j is the next index where a nonzero element should be placed
        at the end all the zeroes will be at the end or will never moved
        when encountered 
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1 # ensures every nonzero element is moved to the beginning 
        return nums
    
    def applyOperations_alt(self, nums: List[int]) -> List[int]:
        """
        O(n)
        O(1) since res is the expected output
        First step to update the nums is the same
        Then create res
        Put all non-zero values
        Then extend it with the leftover zeroes from nums
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0 
        res = []
        for num in nums:
            if num != 0:
                res.append(num)
        res.extend(i for i in nums if i == 0)
        return res
    
    
