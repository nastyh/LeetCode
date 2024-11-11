class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        where it's 0, it either belongs to a 2-bit char along with a 1 in front of it
        or it itself a 1-bit char
        Count the number of 1 before the last 0:
        if it's even, than the last 0 is a 1-bit
        If it's odd, than it's part of the 2-bit char 
        """
        stop = len(bits) - 1
        res = 0
        while stop > 0:
            stop -= 1
            if bits[stop] == 1:
                res += 1
            else:
                break
        return res%2 == 0