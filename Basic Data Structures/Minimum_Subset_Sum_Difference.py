"""
Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.
[1, 2, 3, 9]
Output: 3
[1, 2, 3] and [9]. Sum of the first is 6, second is 9. Diff is 3

[1, 2, 7, 1, 5]
Output: 0
[1, 2, 5] & [7, 1]. 8 and 8

[1, 3, 100, 4]
Output: 92
"""

def can_partition(nums):  # O(NS) both, where N is len(nums) and S is sum(nums)
    if len(nums) == 0: return 0
    dp = [[False] * (sum(nums) // 2 + 1) for _ in range(len(nums))]
    for row in range(len(nums)):  # first col
        dp[row][0] = True
    for col in range(1, sum(nums) // 2 + 1):  # first row is True if there is an exact match
        if col == nums[0]:
            dp[0][col] = True
    for row in range(1, len(nums)):
        for col in range(1, sum(nums) // 2 + 1):
            if nums[row] > col:
                dp[row][col] = dp[row - 1][col]
            else:
                dp[row][col] = dp[row - 1][col] or dp[row - 1][col - nums[row]]
    for col in range(sum(nums) // 2, -1, -1):  # finding the most right True cell in the last row
        if dp[-1][col]:
            complement = col  # taking the sum from this cell. The largest sum we can achieve
            break
    other_sum = sum(nums) - complement # that is then the other portion
    return abs(other_sum - complement)  # need the abs difference between the two portions 


if __name__ == '__main__':
    print(can_partition([1, 2, 3, 9]))
    print(can_partition([1, 2, 7, 1, 5]))
    print(can_partition([1, 3, 100, 4]))
