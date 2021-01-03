"""
Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.
"""

def count_subsets(nums, s):
    dp = [[-1] * (s + 1) for _ in range(len(nums))]
    for row in range(len(nums)):  # first column
        dp[row][0] = 1
    for col in range(1, s + 1):
        if nums[0] == col:
            dp[0][col] = 1
        else:
            dp[0][col] = 0
    # print(dp)
    for row in range(1, len(nums)):
        for col in range(1, s + 1):
            dp[row][col] = dp[row - 1][col]
            if col >= nums[row]:
                dp[row][col] += dp[row - 1][col - nums[row]]
    # print(dp)
    return dp[-1][-1]


def count_subsets_bottoms_up(nums, s):
    dp = [[0] * (s + 1) for _ in range(len(nums))]
    for row in range(len(nums)):  # first col
        dp[row][0] = 1
    for col in range(1, s + 1):  # first row 
        if col == nums[0]:
            dp[0][col] = 1 
    # print(dp)
    for row in range(1, len(nums)):
        for col in range(1, s + 1):
            dp[row][col] = dp[row - 1][col]
            if col >= nums[row]:
                dp[row][col] += dp[row - 1][col - nums[row]]
    # print(dp)
    return dp[-1][-1]
    


if __name__ == '__main__':
    print(count_subsets([1, 1, 2, 3], 4))
    print(count_subsets([1, 2, 7, 1, 5], 9))
    print(count_subsets_bottoms_up([1, 1, 2, 3], 4))
    print(count_subsets_bottoms_up([1, 2, 7, 1, 5], 9))