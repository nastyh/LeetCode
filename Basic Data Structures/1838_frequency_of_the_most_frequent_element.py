from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        O(nlogn) -- sorting
        O(1) -- nothing extra is saved
        sort the array so that when we increment the values, we are working toward making contiguous values the same
        goal is to find the largest subarray where all elements can be made equal using at most k operations
        expand the window to include nums[right], calculate the total number of operations required to make all elements in the window equal to nums[right].
        if the total operations exceed k, shrink the window from the left
        Keep track of the maximum size of the valid window.
        To make all elements between l and r equal to nums[r], we need this many operations:
        operations = (nums[r] * window size) - sum of elements in the window
        """
        nums.sort()
        l, tot_sum, max_freq = 0, 0, 1
        for r in range(len(nums)):
            tot_sum += nums[r] 
            while nums[r] * (r - l + 1) - tot_sum > k:
                tot_sum -= nums[l]
                l += 1
            max_freq = max(max_freq, r - l + 1)
        return max_freq 