def subset_sum_brute_force(nums, target):  # O(2^n)
    def _helper(nums, target, ix):
        if ix >= len(nums) or target < 0:
            return False
        if target == 0:
            return True
        return _helper(nums, target - nums[ix], ix + 1) or _helper(nums, target, ix + 1)
    return _helper(nums, target, 0)


def subset_sum_dp(nums, target):
    """
    create dp with columns from 0 to target (including)
    rows are how many numbers we have in nums + 1 (for zero)
    First row can be filled out with False b/c there is no way to get to target without having any numbers
    """
    dp = [[False for x in range(target + 1)] for y in range(len(nums))]
    for i in range(0, len(nums)):  # populate the first column with True, as we can always form '0' sum with an empty set
        dp[i][0] = True
    for s in range(1, target + 1):
        dp[0][s] = True if nums[0] == s else False
    # process all subsets for all sums
    for row in range(1, len(nums)):
        for col in range(1, target + 1):
        # if we can get the sum 's' without the number at index 'i'
            if dp[row - 1][col]:
                dp[row][col] = dp[row - 1][col]
            elif col >= nums[row]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[row][col] = dp[row - 1][col - nums[row]]

    # the bottom-right corner will have our answer.
    return dp[-1][-1]


if __name__ == '__main__':
    print(subset_sum_brute_force([1, 2, 3, 7], 6))
    print(subset_sum_brute_force([1, 2, 7, 1, 5], 10))
    print(subset_sum_brute_force([1, 3, 4, 8], 6))
    print(subset_sum_dp([1, 2, 3, 7], 6))
    print(subset_sum_dp([1, 2, 7, 1, 5], 10))
    print(subset_sum_dp([1, 3, 4, 8], 6))
