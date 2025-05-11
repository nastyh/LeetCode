from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        O(n)
        O(1)
        brute force it with the three pointers
        pay attention to the task, there can be a list with fewer than three elements
        """
        if len(arr) < 3: return False
        l, m, r = 0, 1, 2
        while r < len(arr):
            if arr[l] % 2 == 1 and arr[m] % 2 == 1 and arr[r] % 2 == 1:

                return True 
            l += 1
            m += 1
            r += 1
        return False 
    
    def threeConsecutiveOdds_counter(self, arr: List[int]) -> bool:
        """
        O(n)
        O(1)
        just count odd numbers using d
        restart when you see an even num
        """
        d = 0
        i = 0
        while i < len(arr):
            if arr[i] % 2 == 1:
                d += 1
            else: 
                d = 0 
            i += 1
            if d == 3: return True

        return False 
    
    def threeConsecutiveOdds_multiply(self, arr: List[int]) -> bool:
        """
        O(n)
        O(1)
        odd * odd = even 
        even * odd = odd 
        multiply three numbers and make a decision 
        """
        for i in range(len(arr) - 2):
            product = arr[i] * arr[i+1] * arr[i+2]
            if product % 2 == 1:
                return True
        return False 
