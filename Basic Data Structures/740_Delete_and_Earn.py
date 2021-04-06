def deleteAndEarn_sorting(nums):  # O(nlogn) and O(n)
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    sort_num = sorted(nums)
    max_num = sort_num[-1]
    value = [0] * (max_num + 1)
    dp = value
    for num in sort_num:
        value[num] += num
    max_points = 0
    dp[0] = 0
    dp[1] = value[1]
    dp[2] = max(value[1], value[2])
    for i in range(3, max_num + 1):
        dp[i] = max(value[i] + dp[i - 2], dp[i - 1])
        max_points = max(max_points, dp[i])
    return max_points


def deleteAndEarn_optimal(nums):  # O(n) and O(n)
    if not nums : return 0
    helper = [0] * (max(nums) + 1)
    for num in nums:
        helper[num] += num
    dp = [0] * (len(helper) + 1)
    for i in range(1,len(helper)):
        dp[i] = max(helper[i] + dp[i - 2], dp[i - 1])
    return max(dp[-1], dp[-2])
     