from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        O(n) both
        The question asks the number of distinct numbers in nums than are > k
        edge case: if any number is < k, return -1 (due to the question)
        then just throw numbers in a set and build res 
        return res
        """
        s, res = set(nums), 0
        if any(n < k for n in s): 
            return -1
        for n in s: 
            if n > k: 
                res += 1
        return res 
    
    def minOperations_one_liner(self, nums: List[int], k: int) -> int:
        return -1 if min(nums) < k else len(set(nums).difference({k}))