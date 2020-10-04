import math 
def findAverages(nums, k):
    if len(nums) == 0: return []
    if len(nums) < k: return []
    res = []
    l = 0
    curr_sum = 0.0
    for r in range(len(nums)):
        curr_sum += nums[r]
        if r - l == k - 1:
            res.append(curr_sum)
            curr_sum -= nums[l]
            l += 1
    return [v / 5 for v in res]


def findAverages_alt(nums, k):
    if len(nums) == 0: return []
    if len(nums) < k: return []
    res = []
    l = 0
    r = l + k - 1
    curr_sum = sum(nums[l: r + 1])
    res.append(curr_sum)
    while r != len(nums) - 1:
        curr_sum -= nums[l]
        l += 1
        r += 1
        curr_sum += nums[r]
        res.append(curr_sum)
    return [v / 5 for v in res]


def maxSubarraySizeK(nums, k):
    if len(nums) == 0:
        return 0
    if len(nums) < k:
        return 0
    glob_res, curr_res = -math.inf, 0
    l = 0
    r = l + k - 1
    curr_res = sum(nums[l:r + 1])
    glob_res = max(glob_res, curr_res)
    while r != len(nums) - 1:
        curr_res -= nums[l]
        l += 1
        r += 1
        curr_res += nums[r]
        glob_res = max(glob_res, curr_res)
    return glob_res

def smallestSubarraySum(nums, s):
    if any(i == s for i in nums): return 1
    glob_l, curr_sum = math.inf, 0 
    l = 0
    for r in range(len(nums)):
        curr_sum += nums[r]
        while curr_sum >= s:
            glob_l = min(glob_l, r - l + 1)
            curr_sum -= nums[l]
            l += 1 
    return glob_l if glob_l != math.inf else 0 
    


if __name__ == '__main__':
    # print(findAverages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
    # print(findAverages_alt([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
    # print(maxSubarraySizeK([2, 1, 5, 1, 3, 2], 3))
    print(smallestSubarraySum([2, 1, 5, 2, 3, 2], 7))
    print(smallestSubarraySum([2, 1, 5, 2, 8], 7))
    print(smallestSubarraySum([3, 4, 1, 1, 6], 8))
 