def rangeBitwiseAnd(m, n):  # O(1) and O(1)
    """
    For a series of bits, e.g. [1, 1, 0, 1, 1], as long as there is one bit of zero value, then the result of AND operation
    on this series of bits would be zero.
    rst we could represent each number in the range in its binary form which we could view as a string of binary numbers (e.g. 9 = 00001001).
    We then align the numbers according to the position of binary string.
    """
    shift = 0   
    # find the common 1-bits
    while m < n:
        m = m >> 1
        n = n >> 1
        shift += 1
    return m << shift


def rangeBitwiseAnd_alt(m, n):
    while m < n:
        # turn off rightmost 1-bit
        n = n & (n - 1)
    return m & n