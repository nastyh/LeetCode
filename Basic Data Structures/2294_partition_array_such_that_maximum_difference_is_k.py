from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        O(nlogn) for sorting
        O(1) assuming in-place sorting

        Sorting and greedy 
        group adjacent elements into a subsequence as long as the
        difference between the first (minimum) and the current element is <=k
        Sort 
        res is 1 since at least one subsequence is needed
        start is the smallest element since we sorted 
        iterate through nums
        if num - start > k: 
        start a new subsequence w/ num as a new start
        increment res
        """
        nums.sort()
        res, start = 1, nums[0]
        for num in nums:
            if num - start > k: 
                res += 1
                start = num
        return res