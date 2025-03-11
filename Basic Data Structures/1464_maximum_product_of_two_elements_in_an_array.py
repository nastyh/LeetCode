import heapq
import math
from typing import List


class Solution:

    def maxProduct_easiest(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
        Update the current max as we iterate through the list.
        Multiply the current number you're at by the current max up to that point and repeat
        """
        curr_max, res = 1, 0
        for i in range(len(nums)):
            res = max(res, (nums[i] - 1) * (curr_max - 1))
            curr_max = max(curr_max, nums[i])
        return res 
    
    def maxProduct_largest(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
        Iterate 
        if you see the num larger than the first largest,
        put the current value of the first largest into the second largest
        update the first largest to num
        Otherwise, just make a decision whether the current num should 
        substitute the second largest 
        """
        first_l, second_l = 0, 0
        for num in nums:
            if num > first_l:
                second_l = first_l 
                first_l = num 
            else:
                second_l = max(second_l, num)
        return (first_l - 1) * (second_l - 1)
    

    def maxProduct_heap(self, nums: List[int]) -> int:
        """
        O(nlogn) where n is prob 2
        O(nlogn) due to the heap 
        nlargest returns a list of the n largest elements from nums
        in our case 
        a is a list of one element, thus, I take [0]
        a is a list of two elements, thus, I take [1], i.e. second largest 
        """
        a, b = heapq.nlargest(2, nums)[0], heapq.nlargest(2, nums)[1]
        return ( a- 1) * (b - 1)
        
    def maxProduct_sort(self, nums: List[int]) -> int:
        """
        O(nlogn) due to sorting
        O(n) since how sorting, in the worst case, is implemented in Python (timsort)
        but I doubt 
        sort, take two largest, since all the nums are non-negative
        """
        nums.sort()
        a, b = nums[-1] - 1, nums[-2] - 1
        return a * b
    def maxProduct_brute_force(self, nums: List[int]) -> int:
        """
        O(n^2) due to two loops
        O(1)
        do what they ask: two loops to process all possible candidates
        pick the best 
        """
        res = -math.inf
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                cand = (nums[i] - 1) * (nums[j] - 1)
                res = max(res, cand)
        return res