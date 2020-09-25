from collections import Counter
def singleNumber(nums):  # optimal
    res = 0
    for num in nums:
        res ^= num
    return res


def singleNumber_dict(nums):  # uses extra space
    d = Counter(nums)
    return [k for (k, v) in d.items() if v == 1][0]


def singleNumber_naive(nums):
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
        else:
            res.remove(num)
    return res[0]


def singleNumber_math(nums):
    return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    print(singleNumber([2, 2, 1]))
    print(singleNumber([4, 1, 2, 1, 2]))
    print(singleNumber_dict([2, 2, 1]))
    print(singleNumber_dict([4, 1, 2, 1, 2]))
    print(singleNumber_naive([2, 2, 1]))
    print(singleNumber_naive([4, 1, 2, 1, 2]))
    print(singleNumber_math([2, 2, 1]))
    print(singleNumber_math([4, 1, 2, 1, 2]))