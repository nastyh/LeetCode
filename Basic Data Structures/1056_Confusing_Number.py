def confusingNumber_string_manipulation(self, n: int) -> bool:
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        if n in (0, 1, 2, 3, 4, 5, 7, 8): return False
        if n in (6, 9): return True
        n_str = str(n)
        l = 0
        while n_str[l] == '0':
            l += 1
        n_str = n_str[l:]
        new_n = ''
        for ch in n_str:
            if ch not in mapping:
                return False 
            else: 
                new_n += mapping[ch]
        if int(new_n[::-1]) == n: return False
        return True

def confusingNumber(N):
    nums = []
    d = {0: 0, 1: 1, 6: 9, 9: 6, 8: 8}
    new_nums = []
    if N < 10:
        nums.append(N)
    nums = [int(x) for x in str(N)]
    if any(i in [2, 3, 4, 5, 7] for i in nums):
        return False
    for n in nums:
        new_nums.append(d[n])
    if N - sum([v * 10**k for k, v in enumerate(new_nums)]) == 0:
        return False
    else:
        return True


def test(n): # number to a list of digits; less Pythonic
    nums = []
    while n > 0:
        nums.append(n % 10)
        n = n // 10
    return nums[::-1]


if __name__ == '__main__':
    print(confusingNumber(89))
    print(confusingNumber(6))
    print(confusingNumber(25))
    print(confusingNumber(0))
    print(confusingNumber(11))
    print(confusingNumber(916))
    print(test(34))      
