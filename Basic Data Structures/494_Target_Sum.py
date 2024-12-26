def findTargetSumWays_dp(self, nums: List[int], target: int) -> int:
    """
    O(n * total_sum) both
    2D dp array with dimensions [nums.length][2 * totalSum + 1]
    to represent possible sums shifted by totalSum (to handle negative indices).
    Add 1 to dp[0][nums[0] + totalSum] to account for adding the first number.
    Add 1 to dp[0][-nums[0] + totalSum] to account for subtracting the first number (handle duplicate cases).
    For each possible sum sum in the range -totalSum to totalSum:
    If dp[index - 1][sum + totalSum] > 0 (i.e., the sum is achievable from previous numbers):
    Add its value to dp[index][sum + nums[index] + totalSum] (sum achieved by adding the current number).
    Add its value to dp[index][sum - nums[index] + totalSum] (sum achieved by subtracting the current number).
    Check if the absolute value of the target exceeds totalSum:
    If yes, return 0 (the target is unachievable).
    Otherwise, return dp[nums.length - 1][target + totalSum], which contains the number of ways to achieve the target.
    """
    total_sum = sum(nums)
    dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]
    dp[0][nums[0] + total_sum] = 1
    dp[0][-nums[0] + total_sum] += 1

    for index in range(1, len(nums)):
        for sum_val in range(-total_sum, total_sum + 1):
            if dp[index - 1][sum_val + total_sum] > 0:
                dp[index][sum_val + nums[index] + total_sum] += dp[
                    index - 1
                ][sum_val + total_sum]
                dp[index][sum_val - nums[index] + total_sum] += dp[
                    index - 1
                ][sum_val + total_sum]

    # Return the result if the target is within the valid range
    return (
        0
        if abs(target) > total_sum
        else dp[len(nums) - 1][target + total_sum]
    )
def findTargetSumWays_dp_space_optimized(self, nums: List[int], target: int) -> int:
    """
    like dp but using the dictionary instead
    """
    d = defaultdict(int)
    d[0] = 1
    for num in nums:
        dp = defaultdict(int)
        for k, v in d.items():
            dp[k + num] += v
            dp[k - num] += v
        d = dp
    return d[target]

def findTargetSumWays(nums, S):
    memo = {}
    def findSum(nums, s):
        if (len(nums), s) in memo:
            return memo[(len(nums), s)]
        if not nums:
            return 1 if not s else 0
        result = findSum(nums[1:], s + nums[0]) + findSum(nums[1 : ], s - nums[0])
        memo[(len(nums), s)] = result
        return result
    return findSum(nums, S)


def findTargetSumWays_alt(nums, s):  # O(NS), N total numbers, S sum. Space is O(S)
    totalSum = sum(nums)
    # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s + totalSum) / 2'
    if totalSum < s or (s + totalSum) % 2 == 1:
        return 0

    def count_subsets(nums, s):
        n = len(nums)
        dp = [[0 for x in range(s + 1)] for y in range(n)]

        # populate the sum = 0 columns, as we will always have an empty set for zero sum
        for i in range(0, n):
            dp[i][0] = 1
        # with only one number, we can form a subset only when the required sum is
        # equal to the number
        for s in range(1, s + 1):
            dp[0][s] = 1 if nums[0] == s else 0
        # process all subsets for all sums
        for i in range(1, n):
            for s in range(1, s + 1):
                dp[i][s] = dp[i - 1][s]
                if s >= nums[i]:
                    dp[i][s] += dp[i - 1][s - nums[i]]
        return dp[-1][-1]

    return count_subsets(nums, (s + totalSum) // 2)


def findTargetSumWays_optimized(nums, s):  # O(NS) and O(S)
    totalSum = sum(nums)
    if totalSum < s or (s + totalSum) % 2 == 1:
        return 0
    def count_subsets(nums, s):
        n = len(nums)
        dp = [0 for x in range(s + 1)]
        dp[0] = 1
        # with only one number, we can form a subset only when the required sum is equal to the number
        for j in range(1, s + 1):
            dp[j] = 1 if nums[0] == j else 0
        # process all subsets for all sums
        for i in range(1, n):
            for j in range(s, -1, -1):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]
        return dp[s]
    return count_subsets(nums, (s + totalSum) // 2)


if __name__ == '__main__':
    print(findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(findTargetSumWays_alt([1, 1, 1, 1, 1], 3))
    print(findTargetSumWays_optimized([1, 1, 1, 1, 1], 3))
