class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        O(n) both
        l and r to create a sliding window
        need a set to make sure we don't have the repeating numbers in a subarray
        """
        l, curr_sum, glob_sum = 0, 0, 0
        s = set()
        for r in range(len(nums)):
            while nums[r] in s or r - l + 1 > k: 
                s.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            s.add(nums[r])
            curr_sum += nums[r]
            if r - l + 1 == k:
                glob_sum = max(glob_sum, curr_sum)
        return glob_sum