from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        O(n) linear scan
        O(1)
        Trick is to properly initialize glob_res, curr_res
        so we handle decreasing lists [10, 8, 3]
        Then start from the second element and compare it to the prev
        and keep track of the best result
        """
        glob_res, curr_res = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_res += nums[i]
                glob_res = max(glob_res, curr_res)
            else: 
                curr_res = nums[i] # set curr_res back 
        return glob_res