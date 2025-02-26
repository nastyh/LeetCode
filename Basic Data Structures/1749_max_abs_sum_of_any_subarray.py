from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        O(n) to run Kadane's alg twice
        O(1) nothing extra is stored
        Run Kadane's twice
        First to find the subarray with the max sum (and return this sum)
        Second to find the subarray with the min sum (and return this sum)
        Then take the max of these two values
        The key is to apply abs() to th min sum 
        since the question is concerned about the abs value 
        """
        if len(nums) == 1:  # edge case
            return abs(nums[0])
        def _kadane_max(nums):
            """
            we assume the first element is the answer
            in the loop, we decide whether it's better 
            to add the i-th element to what we already have, or
            start from scratch from the i-th element 
            """
            max_end, res = nums[0], nums[0]
            for i in range(1, len(nums)):
                max_end = max(max_end + nums[i], nums[i])
                res = max(res, max_end)
            return res
        def _kadane_min(nums):
            """
            same but 
            the decision in the loop is whether adding the i-th 
            element will make everything smaller, or rather we should start 
            from scratch from the i-th element 
            """
            min_end, res = nums[0], nums[0]
            for i in range(1, len(nums)):
                min_end = min(min_end + nums[i], nums[i])
                res = min(res, min_end)
            return abs(res)  # important, since we want the abs values at the end 
        return max(_kadane_max(nums), _kadane_min(nums))