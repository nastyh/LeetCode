from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
        Brute force:
        just recalculate the whole thing and make a decision
        """
        res = 0
        for m_ix in range(1, (len(nums) - 1)):
            curr_sum = nums[m_ix - 1] + nums[m_ix + 1]
            middle = nums[m_ix] / 2 # the // division won't work for [2, -7, -6] so had to update
            if curr_sum == middle:
                res += 1
        return res 
    
    def countSubarrays_another(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
        instead of the sum, we can do a multiplication, but probably the same 
        avoids floating point 
        reduces the constant factor cost per iteration
        """
        res = 0 
        for i in range(1, len(nums) - 1):
            if nums[i] == (nums[i-1] + nums[i+1]) * 2:
                res += 1
        return res 
    
    def countSubarrays_oneliner(self, nums: List[int]) -> int:
        return sum(2 * (nums[i - 1]+nums[i + 1]) == nums[i] for i in range(1, len(nums) - 1))


        