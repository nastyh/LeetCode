from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maximumCount_binary(self, nums: List[int]) -> int:
        """
        O(logn) due to binary search
        O(1) nothing extra is stored
        _helper finds the first ix, where target can be inserted while 
        preserving the order. We run it on zero, so it returns the index
        that is equal to the number of negative numbers (left from the zero)
        binary_right returns a first ix where the element is > target. 
        If we run it for zero and subtract this number from len(nums), it gives 
        the number of positive numbers 
        Then compare and return
        """
        def _helper(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        def binary_right(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        neg_count = _helper(nums, 0)
        pos_count = len(nums) - binary_right(nums, 0)
        return max(neg_count, pos_count)
    
    def maximumCount_binary_one_liner(self, nums: List[int]) -> int:
        """
        Same as above but just uses bisect 
        """
        return max(len(nums) - bisect_right(nums, 0), bisect_left(nums, 0))
    def maximumCount(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
        just brute force it 
        """
        pos, neg = 0, 0
        for num in nums:
            if num > 0:
                pos += 1
            if num < 0:
                neg += 1
        return max(pos, neg)