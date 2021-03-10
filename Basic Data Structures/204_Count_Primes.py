def countPrimes_brute_force(n):  # TLE
    candidates = [i for i in range(2, n)]
    res = [True] * len(candidates)
    for i in range(len(candidates) - 1):
        for j in range(i + 1, len(candidates)):
            if res[i] and  candidates[j] % candidates[i] == 0:
                # res[i] = False
                res[j] = False
    # print(candidates)
    # print(res)
    return sum(res)


def countPrimes_efficient(n):  # O(n) both 
    """
    Marking all multiples as True, then counting the remaining False
    """
    nums = [False] * (n + 1)
    i = 2
    while i * i <= n:
        if not nums[i]:
            st = i * i
            while st <= n:
                nums[st] = True
                st += i
        i += 1
    res = 0
    for i in range(2, len(nums) - 1):
        if not nums[i]:
            res += 1
    return res


if __name__ == '__main__':
    print(countPrimes_brute_force(10))
    print(countPrimes_brute_force(0))
    print(countPrimes_brute_force(1))
    print(countPrimes_brute_force(2))