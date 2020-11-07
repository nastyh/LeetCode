def countPairs_bf(nums, k):  # O(n^2)
    res = 0
    for l in range(len(nums) - 1):
        for r in range(l + 1, len(nums)):
            if abs(nums[r] - nums[l]) == k:
                res += 1
    return res


def countPairs_sort(nums, k):
    res = 0
    nums.sort()
    l, r = 0, 0
    while r < len(nums):
        if nums[r] - nums[l] < k:
            r += 1
        elif nums[r] - nums[l] > k:
            l += 1
        else:
            res += 1
            l += 1
            r += 1
    return res

if __name__ == '__main__':
    print(countPairs_bf([8, 12, 16 ,4, 0, 20], 4))
    print(countPairs_sort([8, 12, 16 ,4, 0, 20], 4))