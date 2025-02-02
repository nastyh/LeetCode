from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        O(n) just one pass
        O(1) nothing to store
        If nums is rotated it will have at most only one drop
        [3, 4, 5, 1, 2] -- it drops after 5 but that's it
        means it was rotated once 
        all other cases -- not rotated
        edge case: a wrap around from the last to the first el
        so need to check num[-1] > nums[0] as a candidate, too 
        """
        decrease_points = 0
        for i in range(len(nums)):
            # we do % to cover the edge case 
            if nums[i] > nums[(i + 1) % len(nums)]:
                decrease_points += 1
                if decrease_points > 1:
                    return False
        return True
    
    def check_slightly_different(self, nums: List[int]) -> bool:
        """
        O(n) just one pass
        O(1) nothing to store
        Same idea but we check the edge case
        num[-1] > nums[0] separately in the beginning
        and then we just work through the list 
        and check decrease_points two times instead of one
        easier to comprehend
        """
        decrease_points = 0
        if nums[-1] > nums[0]: 
            decrease_points += 1
        for i in range(len(nums) - 1): # range, be careful
            if nums[i] > nums[i + 1]:
                if decrease_points > 1:
                    return False
                decrease_points += 1
                if decrease_points > 1:
                    return False
        return True
    
    def check_tweak(self, nums: List[int]) -> bool:
        """
        O(n) just one pass
        O(1) nothing to store
        same but so we don't need to check 
        if decrease_points > 1 inside the loop
        I move if nums[-1] > nums[0]: after the loop
        """
        decrease_points = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                decrease_points += 1
        if nums[-1] > nums[0]: 
            decrease_points += 1
        if decrease_points > 1:
            return False
        else:
            return True