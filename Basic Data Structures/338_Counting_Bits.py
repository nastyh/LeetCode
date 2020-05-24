def countBits(num):
    ones = []

    def _helper(n):
        res = []
        while n > 0:
            res.append(n % 2)
            n = n // 2
        return sum([1 for i in res[::-1] if i == 1])

    for n in range(num+1):
        ones.append(_helper(n))

    return ones

if __name__ == '__main__':
    print(countBits(5))
