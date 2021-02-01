def hammingWeight(n)
    return bin(n).count('1')


def hammingWeight_another(n):
    """
    Check every of the 32 bits of the number. If the bit is 1, increment the answer
    """
    ans = 0
    while n:
        ans += n % 2
        n = n >> 1  # returns n with the bits shifted to the right by 1 place. Same as n // 2^1
    return ans


def hammingWeight_manual(n):  # TLE but works in general
    def _int_to_bin(num):
        res = ''
        while n > 0:
            res += str(num % 2)
            num //= 2
        return s[::-1]
    return sum([1 for i in _int_to_bin(n) if i == '1'])

