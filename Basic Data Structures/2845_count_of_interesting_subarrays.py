from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        """
        O(n)
        O(m), m is modulo 
        we only care how many good elements (nums[k] / modulo m == k) appear in each subarray
        and then take that count modulo m
        """
        # count_mod[r] = how many prefixes have sum%modulo == r
        count_mod = defaultdict(int)
        count_mod[0] = 1

        res = 0
        prefix = 0
        for x in nums:
            # indicator: 1 if x%modulo == k, else 0
            prefix += (1 if x % modulo == k else 0)

            cur_mod = prefix % modulo
            # we want prior_prefix_mod == (cur_mod - k) mod modulo
            target = (cur_mod - k) % modulo

            res += count_mod[target]
            count_mod[cur_mod] += 1

        return res