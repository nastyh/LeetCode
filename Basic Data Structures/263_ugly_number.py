class Solution:
    def isUgly(self, n: int) -> bool:
        """
        O(logn) probably due to division
        O(1)
        Make sure if you can turn a number into 1
        by dividing by 2, or 3, or 5 
        """
        if n < 1: return False
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //=5
            else: return False
        return True