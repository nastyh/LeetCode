from typing import Counter, List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
        O(n), single pass with occasional left‐pointer advances
        O(n) due to the counter
        in linear time, maintaining a left and right pointer and a running Counter of frequencies, plus a distinct count.
        """
        if len(nums) <= 1: return len(nums)  # edge case
        s_len = len(set(nums))
        def _helper(nums, s_len):
            d = Counter()
            left = 0
            res = 0
            distinct = 0
            for right, x in enumerate(nums):
                # include nums[right]
                if d[x] == 0:
                    distinct += 1
                d[x] += 1

                # shrink window until we have ≤ K distinct
                while distinct > s_len:
                    d[nums[left]] -= 1
                    if d[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                # any subarray ending at `right` and starting anywhere in [left..right]
                # has ≤ K distinct
                res += right - left + 1
            return res
        return _helper(nums, s_len) - _helper(nums, s_len - 1)