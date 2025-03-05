class Solution:
    def coloredCells(self, n: int) -> int:
        """
        O(1) both
        start w/ a blue cell, add multiples of 4: 4x1, 4x2, etc
        total count is: 1 + (4*1) + (4*2) + ... + (4*(n-1))
        rewrite to 1+2(n-1)n b/c the sum in the parenthesis above is
        the arithmetic seriies 
        """
        return 2 * n * n - 2 * n + 1
    
    def coloredCells_longer(self, n: int) -> int:
        """
        Same idea as above
        """
        res = 1 
        for i in range(n):
            res += 4 * i 
        return res