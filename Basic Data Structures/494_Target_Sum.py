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


if __name__ == '__main__':
    print(findTargetSumWays([1, 1, 1, 1, 1], 3))