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