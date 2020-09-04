def isPowerOfTwo_recur(n):
    if n <= 0: return False
    if n == 1: return True
    if n % 2 == 1: return False
    return isPowerOfTwo_recur(n // 2)


def isPowerOfTwo_binary(n):  # count the number of ones in a binary form of the number. All numbers that are power of 2 have only one 1 and it stands in the beginning
    return n > 0 and bin(n).count('1') == 1


def isPowerOfTwo_bit(n):
    """
    binary representation is only one 1 followed by zeroes. 2 to the power minus 1 must be zero followed by ones. Thus, bitwise AND will return 1 if 
    the corresponding bit of X and Y is 1, otherwise 0. 
    """
    return n > 0 and not (n & n - 1)


if __name__ == '__main__':
    print(isPowerOfTwo_recur(-3))
    print(isPowerOfTwo_recur(0))
    print(isPowerOfTwo_recur(1))
    print(isPowerOfTwo_recur(64))
    print(isPowerOfTwo_binary(-3))
    print(isPowerOfTwo_binary(0))
    print(isPowerOfTwo_binary(1))
    print(isPowerOfTwo_binary(64))
    print(isPowerOfTwo_bit(-3))
    print(isPowerOfTwo_bit(0))
    print(isPowerOfTwo_bit(1))
    print(isPowerOfTwo_bit(64))
