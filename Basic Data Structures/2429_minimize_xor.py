class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        O(32) = O(1)
        O(1)
        Count the number of set bits in num2
        Construct a number x with the same number of set bits as num2
        to minimize x xor num1, x should be as close to num1 as possible in terms
        of the binary representation

        """
        set_bits_num2 = bin(num2).count('1')
        x = 0
        # Use the bits from num1 first
        for i in range(31, -1, -1):  # 31 bits for num1 as it can be up to 10^9
            if set_bits_num2 == 0:
                break
            # & is a bitwise AND operator comparing each bit of two nums
            # if both bits == 1, then returns 1, else 0
            if num1 & (1 << i):  # Check if the bit at position i is set in num1
                # |= combines a bitwise OR with assignment 
                x |= (1 << i)  # Set the bit at position i in x. (1 << i) shifts th number 1 left by i positions
                set_bits_num2 -= 1
        
        # If more set bits are needed, fill from LSB (least significant bit) upwards
        for i in range(32):
            if set_bits_num2 == 0:
                break
            if not (x & (1 << i)):  # Check if the bit at position i is not set in x
                x |= (1 << i)  # Set the bit at position i in x
                set_bits_num2 -= 1
        
        return x