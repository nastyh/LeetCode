def concatenatedBinary_optimal(n):
    """
    Avoids string concatenation
    Convert the number into binary form.
    Iterate the binary string.
    For each element (0 or 1), update result to 2*result + element.
    """
    MOD = 10**9 + 7
    concatenation = "".join(bin(i)[2:] for i in range(n + 1))
    return int(concatenation, 2) % MOD


def concatenatedBinary_bit_shifting(n):  # O(nlogn) iterate over n and check whether it's a power of 2 (takes logn) and O(1)
    """
    Step 1: Initialize an integer result to store the final result.
    Step 2: Iterate from 1 to n. For each number i:
    Find the length of the binary representation of the number. Denote by length.
    Update result to result * 2**length + 1
    """
    MOD = 10**9 + 7
    length = 0  # bit length of addends
    result = 0   # long accumulator
    for i in range(1, n + 1):
        # when meets power of 2, increase the bit length
        if math.log(i, 2).is_integer():
            length += 1
        result = ((result * (2 ** length)) + i) % MOD
    return result


def concatenatedBinary_math(n):  # O(n) and O(1)
    """
    With bitwise operation, we can check whether a number is the power of 22 in O(1)
    If (x & (x - 1)) == 0, then x is the power of 22.
    """
    MOD = 10**9 + 7
    length = 0  # bit length of addends
    result = 0   # long accumulator
    for i in range(1, n + 1):
        # when meets power of 2, increase the bit length
        if i & (i - 1) == 0:
            length += 1
        result = ((result << length) | i) % MOD
    return result



def concatenatedBinary(n):  # works but TLE
    """
    Brute force: turn to a binary, then turn back 
    """
    nums = list(range(1, n + 1))
    number = ''
    def _dec_to_bin(num):
        res = ''
        while num != 0:
            res += str(num % 2)
            num //= 2
        return res[::-1]
    def _bin_to_dec(num):
        return sum([2**k if v == '1' else 0 for k, v in enumerate(list(reversed(num)))])
    for num in nums:
        number += _dec_to_bin(num)
    return _bin_to_dec(number) % (10**9 + 7)


if __name__ == '__main__':
    print(concatenatedBinary(1))
    print(concatenatedBinary(3))
    print(concatenatedBinary(12))