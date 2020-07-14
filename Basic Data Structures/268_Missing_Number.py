def missingNumber(nums): # brute force
    d = dict.fromkeys(range(min(nums), len(nums) + 1))
    for n in nums:
        if n in d:
            d[n] = 1
    return [k for k, v in d.items() if v is None][0]


def missingNumber_alt(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


def missingNumber_Gauss(nums):
    target_sum = len(nums) * (len(nums) + 1) / 2
    real_sum = sum(nums)
    return int(target_sum - real_sum)


def missingNumber_naive(nums):
    full = range(0, len(nums) + 1)
    for n in full:
        if n not in nums:
            return n


if __name__ == '__main__':
    print(missingNumber([3, 0, 1]))
    print(missingNumber([0]))
    print(missingNumber_Gauss([3, 0, 1]))
    print(missingNumber_Gauss([0]))
    print(missingNumber_naive([0]))
