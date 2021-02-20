def countBits(num):  # O(nk) and O(n) where k is the number of bits in a given number 
    """
    Brute force: convert each number to binary and count 1s
    """
    ones = []
    def _helper(n):
        res = []
        while n > 0:
            res.append(n % 2)
            n = n // 2
        return sum([1 for i in res[::-1] if i == 1])
    for n in range(num + 1):
        ones.append(_helper(n))
    return ones


def countBits_last_sert(num):  # O(n) both
    result = [0]*(num+1)
    for i in range(1, num + 1):
        result[i] = result[i & (i - 1)] + 1
    return result

if __name__ == '__main__':
    print(countBits(5))
