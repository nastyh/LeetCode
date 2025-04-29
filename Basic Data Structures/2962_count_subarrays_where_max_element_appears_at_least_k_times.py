from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        O(n) to go via nums
        O(1) nothing to store

        Sliding window
        start expanding the right side of the window
        If we encounter a value == max_element, increment max_elements_in_window
        once we hit a window of the size k, start moving the left pointer
        if the left point to the max_element, we are leaving it, so decrement max_elements_in_window
        build res since it's the number of the subarrays where all the conditions are met 
        """
        max_element = max(nums)
        res = 0
        max_elements_in_window = 0 
        l = 0
        for r in range(len(nums)):
            if nums[r] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[l] == max_element:
                    max_elements_in_window -= 1 
                l += 1 
            res += l 
        return res 