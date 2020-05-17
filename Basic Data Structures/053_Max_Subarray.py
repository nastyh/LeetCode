class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if all(x >= 0 for x in nums):
            return sum(nums)
        current, glob = nums[0], nums[0]
        for i in range(1, len(nums)):
            current = max(current, current+nums[i])
            glob = max(current, glob)
        return glob
