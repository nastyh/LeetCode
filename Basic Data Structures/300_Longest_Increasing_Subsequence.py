import bisect
def lengthOfLIS(nums): # O(n^2), DP
    if len(nums) <= 1: return len(nums)
    i, j, dp, res = 0, 1, [1] * len(nums), 1
    for j in range(1, len(nums)):
        for i in range(j):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], dp[i] + 1)
        # res = max(res, dp[i])
    return max(dp)


def lengthOfLIS_log(nums):  # O(nlogn)
    if len(nums) == 0:
        return 0 
    dp = []
    for n in nums:
        pos = bisect.bisect_left(dp, n)
        if pos == len(dp):
            dp.append(n)
        else:
            dp[pos] = n
    return len(dp)


def lengthOfLIS_log_another(nums):
    if not nums:
        return 0
    def _helper(li, n):
        l = 0
        r = len(li) - 1
        while l < r - 1:
            m = (l + r) // 2
            if li[m] > n:
                r = m
            else:
                l = m
        if li[l] >= n:
            return l
        return r
    dp = [nums[0]]
    for i in range(len(nums)):
        if nums[i] > dp[-1]:
            dp.append(nums[i])
        else:
            ix = _helper(dp, nums[i])
            dp[ix] = nums[i] 
    return len(dp)


if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS([7, 7, 7]))
    print(lengthOfLIS_log([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS_log([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS_log([7, 7, 7]))
    print(lengthOfLIS_log_another([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS_log_another([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS_log_another([7, 7, 7]))