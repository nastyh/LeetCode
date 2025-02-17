class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """
        O(l1 + l2), lengths of both
        O(1)
        A key observation is that when we swap characters between the two strings,
        the best we can do is to "fix" two mismatches at once if they are of the same type.
        For example, two mismatches of type 'x'-'y' can be fixed with one swap. So we can perform:

        countXY // 2 swaps to fix mismatches in pairs for the first type.
        countYX // 2 swaps to fix mismatches in pairs for the second type.
        However, if countXY and countYX are both odd, then after pairing as many as possible,
        you'll have one mismatch of each type left. In this case, you can fix them with two additional swaps.

        """
        countXY = countYX = 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                countXY += 1
            elif a == 'y' and b == 'x':
                countYX += 1
        # If the total number of mismatches is odd, it is impossible to fix
        if (countXY + countYX) % 2 != 0:
            return -1
        # Calculate swaps for pairs of mismatches
        swaps = (countXY // 2) + (countYX // 2)
        # Add two swaps if both are odd
        if countXY % 2 == 1:
            swaps += 2
        
        return swaps