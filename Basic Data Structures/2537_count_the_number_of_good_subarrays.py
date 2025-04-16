from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        O(n) to go over nums 
        O(n) to build a dictionary 
        expand a right pointer over the array while maintaining
        a frequency dictionary (or counter) that keeps track of how many
        times each element appears in the current window.
        Using this dictionary, we can count the number of identical pairs in the current window. When the number of pairs reaches or exceeds
        k, every further expansion of the window will also be good. 
        By moving the left pointer appropriately while adjusting the counts, we can count all such good subarrays.
        """
        res, l, curr_pairs, d = 0, 0, 0, defaultdict(int)
        for r in range(len(nums)):
            """
            add nums[right], it forms 'd[nums[r]]' new pairs
            because every previous occurrence of nums[r] in the window will pair with this one.
            """
            curr_pairs += d[nums[r]]
            d[nums[r]] += 1 
            """
            If the current window has at least k pairs, then all subarrays starting from l to r
            and extending to any index after r are good subarrays
            """
            while curr_pairs >= k and l <= r: 
                """
                All subarrays with the current right as the start of the tail are good.
                """
                res += (len(nums) - r)
                d[nums[l]] -= 1
                curr_pairs -= d[nums[l]]
                l += 1 # shrink the window from the left 
        return res 