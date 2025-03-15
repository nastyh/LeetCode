from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        O(nlogR) where R is the range max(nums) - min(nums)
        traverse using _helper n times
        O(1) nothing else to store
        “capability” is the maximum amount of money the robber takes from a single house.
        Our goal is to minimize this capability while still robbing at least k houses
        under the condition that no two adjacent houses are robbed.
        The capability can only be as low as the smallest value in the array and as high as the largest value.
        For a candidate capability X, we need to check if it is possible to rob at least k houses by only considering houses with nums[i] <= X.
        Iterate through the list.
        If a house’s value is ≤ X, count it as robbed and skip the next house (to respect the “no adjacent houses” rule).
        If the count reaches at least k, the candidate capability is feasible.
        If a candidate capability is feasible, try to lower it by adjusting the high pointer.
        Otherwise, increase the low pointer.
        The answer is the smallest candidate capability for which the feasibility check passes.
         """
        def _helper(nums, k, capability):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        l, r = min(nums), max(nums)
        while l < r :
            m = l + (r - l) //2 
            if _helper(nums, k, m):
                r = m 
            else:
                l = m + 1
        return l