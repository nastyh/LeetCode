from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        O((m+n)*logm) -- each check is O(m+n) and O(logn)
        O(n) for a difference array of size n + 1

        for each index the maximum total decrement we can apply after processing the first k queries is the sum of all query values
        for every query that covers that index
        if we want to zero out every element in nums, then for every index i we need
        Σ (over queries j=0 to k–1, if l_j ≤ i ≤ r_j) queries[j][2] ≥ nums[i].
        to compute the cumulative effect of a set of range additions is to use a difference array.
        For a given k, you can build an array diff of length n+1 (where n = len(nums)) and, for eachquery [l, r, v] in the first k queries, do:
        diff[l] += v
        if r+1 < n: diff[r+1] -= v
        taking the prefix sum of diff gives you the maximum decrement capacity at each index.
        To find the smallest k such that all indices are “covered” (i.e. the capacity at index i is at least nums[i]),
        we can perform a binary search on k from 0 to len(queries). If even after using all queries some index cannot be reduced to 0, we return –1.

        """
        n = len(nums)
        m = len(queries)
        
        # If the initial array is already all zeros, return 0.
        if all(x == 0 for x in nums):
            return 0

        def can_zero(k):
            # Build the difference array for the first k queries.
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v
            
            # Compute prefix sum and check if capacity >= nums[i] for every index.
            current = 0
            for i in range(n):
                current += diff[i]
                if current < nums[i]:
                    return False
            return True

        low, high = 0, m + 1
        while low < high:
            mid = (low + high) // 2
            if can_zero(mid):
                high = mid
            else:
                low = mid + 1

        return low if low <= m else -1
