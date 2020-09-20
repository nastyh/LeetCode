def sequentialDigits(low, high):
    all_digits = ''.join([str(i) for i in range(1, 10)])
    n = 10
    res = []
    for ix in range(len(str(low)), len(str(high)) + 1):
        for start in range(n - ix):
            num = int(all_digits[start:start + ix])
            if num >= low and num <= high:
                res.append(num)
    return res

def sequentialDigits_naive(low, high):
    res = []
    all_digits = ''.join([str(i) for i in range(1, 10)])
    for i in range(len(all_digits)):
        for j in range(i + 1, len(all_digits)):
            curr = int(all_digits[i:j + 1])
            if low <= curr <= high:
                res.append(curr)
    return res


if __name__ == '__main__':
    print(sequentialDigits(100, 300))   
    print(sequentialDigits_naive(100, 300))  