def lengthOfLIS(nums): # O(n^2), DP
    if len(nums) <= 1: return len(nums)
    i, j, dp, res = 0, 1, [1] * len(nums), 1
    for j in range(1, len(nums)):
        for i in range(0, j):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], dp[i] + 1)
        res = max(res, dp[i])
    return max(dp)


def lengthOfLIS_alt(nums):
    if len(nums) <= 1: return len(nums)
    i, j, dp, res = 0, 1, [1] * len(nums), 1
    while j < len(nums):
        if nums[j] >= nums[i]:
            dp[j] = max(dp[j], dp[i] + 1)
            j += 1
        else:
            i += 1
        if j - 1 == i:
            j += 1
            i = 0
    return max(dp)

if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS_alt([10, 9, 2, 5, 3, 7, 101, 18]))