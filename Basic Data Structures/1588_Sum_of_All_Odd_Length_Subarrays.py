def sumOddLengthSubarrays(arr):
    res = 0
    if len(arr) <= 2: return sum(arr)
    l = 0
    # r = l + 1
    while l < len(arr) - 1:
        for r in range(l + 1, len(arr)):
            if (r - l) % 2 == 0:
                res += sum(arr[l: r + 1])
        l += 1
    return res + sum(arr)


if __name__ == '__main__':
    print(sumOddLengthSubarrays([1, 4, 2, 5, 3]))
    print(sumOddLengthSubarrays([1, 2]))
    print(sumOddLengthSubarrays([10, 11, 12]))