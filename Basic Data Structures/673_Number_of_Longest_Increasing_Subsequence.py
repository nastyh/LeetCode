def findnumberofLIS(nums):
    if len(nums) <= 1: return len(nums)
    if len(set(nums)) == 1: return len(nums)
    m, dp, cnt = 0, [1] * len(nums), [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[i] < dp[j] + 1: dp[i], cnt[i] = dp[j] + 1, cnt[j]
                elif dp[i] == dp[j]+1: cnt[i] += cnt[j]
        m = max(m, dp[i])                        
    return sum(c for l, c in zip(dp, cnt) if l == m)


def findnumberofLIS_alt(nums):  # bottoms-up, O(n^2) and O(n)
    """
    If the number at the current index is bigger than the number at the previous index, we increment the count for LIS up to the current index.
    But if there is a bigger LIS without including the number at the current index, we take that.
    """
    dp = [0] * len(nums)
    dp[0] = 1 
    res = 1 
    for i in range(1, len(nums)):
        dp[i] = 1 
        for j in range(i):
            if nums[i] < nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                res  = max(res, dp[i])
    return res 


if __name__ == '__main__':
    print(findnumberofLIS([1, 3, 5, 4, 7]))
    print(findnumberofLIS([2, 2, 2, 2, 2]))
    print(findnumberofLIS_alt([1, 3, 5, 4, 7]))
    print(findnumberofLIS_alt([2, 2, 2, 2, 2]))