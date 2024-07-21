import math
def maxSubArray_1(nums):
    if all(x >= 0 for x in nums):
        return sum(nums)
    if all(x < 0 for x in nums):
        return max(nums)
    current, glob = nums[0], nums[0]
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        glob = max(current, glob)
    return glob


def maxSubArray_2(nums):
    dp = 0
    maxSum = None
    for n in nums:
        dp = max(dp + n, n)
        if maxSum is None or dp > maxSum:
            maxSum = dp
    return maxSum

def maxSubArray_kadane(nums):
    if len(nums) == 1: return nums[0]
        res = -math.inf
        max_at_ix = 0 # best result of a subarray ending at this index
        for num in nums:
            max_at_ix = max(num, max_at_ix + num) # consider or not consider the current element num
            res = max(res, max_at_ix)  # update the global result every time
        return res

def maxSubArray_another_dp(nums):
    if len(nums) <= 1: return sum(nums)
    if all(i < 0 for i in nums): return max(nums)
    if all(i >= 0 for i in nums): return sum(nums)
    dp = [None] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    return max(dp)


def maxSubarray_decision(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    res, curr = -math.inf, -math.inf
    for i in nums:
        if curr + i < i:
            curr = i
        else:
            curr += i
        res = max(res, curr)
    return res


if __name__ == '__main__':
    # print(maxSubArray_1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(maxSubArray_2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(maxSubarray_decision([-2, 1, -3, 4, -1, 2, 1,-5 ,4]))
    # print(maxSubarray_decision([-2, 1]))
    print(maxSubArray_another_dp([-2, 1]))
    print(maxSubArray_another_dp([-1, 0, -2, 2]))
