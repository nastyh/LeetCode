def addBinary(a, b):  # O(M + N)
    """
    convert to decimal, sum, convert to binary
    """
    def binToDec(n):  # n is a string
        return sum([2**k if v=='1' else 0 for k, v in enumerate(n[::-1])])
    def decToBin_alt(n):  # n is a string
        res = []
        n = int(n)
        if n == 0: return '0'
        while n != 0:
            res.append(n % 2)
            n = n // 2
        return ''.join(str(i) for i in res[::-1])
    def decToBin(n): # n is an integer
        if n == 0:
            return '0'
        result = ''
        while n != 0:
            remainder = n % 2  # gives the exact remainder
            n = n // 2
            result = str(remainder) + result
        return result
    c_dec = binToDec(a) + binToDec(b)
    return decToBin_alt(c_dec)


def addBinary_xor(a, b):  # without using the plus sign. O(M +N) and O(max(M, M)) to store the result
    """
    XOR sums two numbers w/o taking into account carries
    Current carry is an AND between two numbers shifted one bit to the left
    Repeat until there is no carry left
    """
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]


def addBinary_pythonic(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    print(addBinary('11', '1'))
    print(addBinary('1010', '1011'))
