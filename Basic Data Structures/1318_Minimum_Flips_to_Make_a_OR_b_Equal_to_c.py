class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:  #O(n) and O(1)
        """
        Given 3 positives numbers a, b and c. Return the minimum flips required
        in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
        Flip operation consists of change any single bit 1 to 0 or change the bit
        0 to 1 in their binary representation.
        Bitwise or (x | y) is 
        Result bit 1, if any of the operand bit is 1; otherwise results bit 0.
        Operator takes two equivalent length bit designs as boundaries;
        if the two bits in the looked-at position are 0, the next bit is zero. If not, it is 1.
        example
        111 and 100 (start from the right)
        1 and 0: gives 1 since there is at least one 1 present
        1 and 0: the same
        1 and 1: two ones, more than enough, so we get 1
        Result is 1, 1, 1 (and it's actually 7)

        Here we need to find the min number of flips in a OR b so one of these numbers
        becomes c 
        """
        res = 0
        while a or b or c:
            # going from right to left
            b_a, b_b, b_c = a & 1, b & 1, c & 1 # the least significant bits
            if b_c == 0:
                res += (b_a & b_b) # if both and b are ones, we need to turn both into zeroes 
                res += (b_a | b_b) # if only one is one and another is zero, we turn only one of them
            else:
                res += ((b_a | b_b) == 0) # if both are zero, we need only one extra flip
            # move to the next bit
            a >>= 1 
            b >>= 1 
            c >>= 1
        return res