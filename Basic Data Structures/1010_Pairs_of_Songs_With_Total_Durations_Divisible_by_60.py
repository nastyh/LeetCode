from collections import defaultdict
def numPairsDivisibleBy60_brute_force(time):  # O(n^2)
    res = 0
    for r in range(1, len(time)):
        for l in range(r):
            if (time[l] + time[r]) % 60 == 0:
                res += 1
    return res


def numPairsDivisibleBy60_alt(time):
    d = defaultdict(int)
    res = 0
    for t in time:
        if (60 - t) % 60 in d:
            res += d[(60 - t) % 60]
        d[t % 60] += 1
    return res


def numPairsDivisibleBy60_efficient(time):  # doesn't pass edge cases
    if all(i % 60 == 0 for i in time): return len(time)
    mods = [i % 60 for i in time]
    def _helper(nums, target):
        res = 0
        d = defaultdict(int)
        for k, num in enumerate(nums):
            if num not in d:
                d[target - num] = 1
            else:
                d[target - num] += 1
            # if num not in d:
            #     d[target - num] = k
            # else:
            #     res += 1
        # return res
        return sum([v for k, v in d.items() if v % 2 == 0]) - 1
    return _helper(mods, 60)


if __name__ == '__main__':
    # print(numPairsDivisibleBy60_brute_force([30, 20, 150, 100, 40]))
    # print(numPairsDivisibleBy60_brute_force([60, 60, 60]))
    print(numPairsDivisibleBy60_alt([30, 20, 150, 100, 40]))
    print(numPairsDivisibleBy60_alt([60, 60, 60]))
    print(numPairsDivisibleBy60_alt([174, 188, 377, 437, 54, 498, 455, 239, 183, 347, 59, 199, 52, 488, 147, 82]))


    