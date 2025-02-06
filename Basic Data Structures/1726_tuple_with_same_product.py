from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct_frequency_count(self, nums: List[int]) -> int:
        """
        O(N^2) two loops
        O(N^2) two store the defaultdict
        dict is product of a*b : [pairs that give this product]
        For each entry, if there are multiple pairs,
        the number of valid tuples is 8 * (k 2) b/c for each 
        combination of pairs, there are 8 possible permutations 
        """
        d = defaultdict(list)
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                curr_prod = nums[i] * nums[j]
                d[curr_prod].append((nums[i], nums[j]))
        for prod, pairs in d.items():
            k = len(pairs)
            if k > 1: # there is more than one way to get this product 
                res += 8 * (k * (k-1) // 2)
        return res
            
        