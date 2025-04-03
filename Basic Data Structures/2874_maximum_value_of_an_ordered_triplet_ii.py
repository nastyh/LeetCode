import math
from typing import List


class Solution:
    def maximumTripletValue_prefix(self, nums: List[int]) -> int:
        """
        O(n) to preprocess nums 
        Evaluates the triplet value in another O(n)
        but overall still O(n)
        O(n) for the prefix and suffix arrays in space 

        Prefix: for each i, store the max el from index 0 to i
        Suffix: for each i, store the max el from index i to the end of nums
        For every valid j (1<=j<=len(nums) - 2) so that there exist bosth an i before 
        and k after: triplet_value = (prefix_max[j-1] - nums[j]) * suffix_max[j+1]
        """
        n = len(nums)
        if n < 3:
            return 0  # not enough elements for a triplet
        # Compute prefix maximum array
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        
        # Compute suffix maximum array
        suffix_max = [0] * n
        suffix_max[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])
        
        max_triplet_value = -math.inf 
        for j in range(1, n-1):
            current_value = (prefix_max[j-1] - nums[j]) * suffix_max[j+1]
            max_triplet_value = max(max_triplet_value, current_value)
        
        return max_triplet_value if max_triplet_value > 0 else 0

    def maximumTripletValue_efficient(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
        accumulate the best pair differences
        and for each new element (that is k in the triplet), compute the candidate product
        if nums[k] > 0: want the largest positive value for nums[i] - nums[j]
        i nums[k] < 0: We want the most negative (i.e. smallest) value for nums[i] - nums[j] 
        so by multiplying by a negative nums[k] gives a positive product
        imax to maintain the maximum value of nums[i] and dmax to maintain the maximum value of nums[i]−nums[j].
        """
        res, imax, dmax = 0, 0, 0 
        for k in range(len(nums)):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res 

    def maximumTripletValue_brute_force(self, nums: List[int]) -> int:
        """
        Will TLE unlike in 2873
        O(n^3) due to three loops
        O(1)
        just do what it asks, accurate with the ranges 
        """
        glob_res = 0
        for i in range(len(nums)- 2):
            for j in range(i+1, len(nums) -1):
                for k in range(j+1, len(nums)):
                    curr_res = (nums[i] - nums[j]) * nums[k]
                    glob_res = max(glob_res, curr_res)
        return glob_res