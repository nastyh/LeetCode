from typing import List


class Solution:

    def maximumTripletValue_efficient(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
        accumulate the best pair differences
        and for each new element (that is k in the triplet), compute the candidate product
        if nums[k] > 0: want the largest positive value for nums[i] - nums[j]
        i nums[k] < 0: We want the most negative (i.e. smallest) value for nums[i] - nums[j] 
        so by multiplying by a negative nums[k] gives a positive product
        imax to maintain the maximum value of nums[i] and dmax to maintain the maximum value of nums[i]−nums[j].
        """
        res, imax, dmax = 0, 0, 0 
        for k in range(len(nums)):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res 
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        O(n^3) due to three loops
        O(1)
        just do what it asks, accurate with the ranges 
        """
        glob_res = 0
        for i in range(len(nums)- 2):
            for j in range(i+1, len(nums) -1):
                for k in range(j+1, len(nums)):
                    curr_res = (nums[i] - nums[j]) * nums[k]
                    glob_res = max(glob_res, curr_res)
        return glob_res
    
