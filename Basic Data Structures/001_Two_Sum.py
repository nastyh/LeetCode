class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            r = target - n
            if r in nums[i+1:]:
                j = nums.index(r,i+1)
                return [i, j]
