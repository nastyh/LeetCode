from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        O(n^2) due to two loops
        O(n) for the dp list 

        sort the array and then use dynamic programming to build up the solution.
        The idea is to have a DP array where dp[i] represents the size of the largest divisible subset ending at nums[i].
        also maintain a "previous" pointer array to help reconstruct the subset.
        """
        res = []
        if not nums:
            return []
        nums.sort()
        dp = [1] * len(nums) # Each element is at least a subset of itself.
        prev = [-1] * len(nums) # To reconstruct the subset.
        max_subset_size = 0
        max_subset_index = -1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > max_subset_size:
                max_subset_size = dp[i]
                max_subset_index = i
        # reconstruct the subset                 
        while max_subset_index != -1:
            res.append(nums[max_subset_index])
            max_subset_index = prev[max_subset_index]
        res.reverse()
        return res 
    