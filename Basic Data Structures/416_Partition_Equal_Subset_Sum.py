def canPartition(nums):
    if sum(nums) % 2 == 1:
        return False
    cache = set()
    def _helper(target, nums):
        nonlocal cache
        if target < 0:
            return False
        if target == 0:
            return True
        if target in cache:
            return False
        cache.add(target)
        for k, v in enumerate(nums):
            if _helper(target - v, nums[k + 1:]) or _helper(target, nums[k + 1:]):
                return True
        return False
    return _helper(sum(nums) // 2, nums)


def canPartition_brute_force(nums):  # O(2^n)
    if sum(nums) % 2 == 1:
        return False
    def _helper(nums, target, ix):
        if target == 0: return True
        if ix >= len(nums) or target < 0:
            return False
        if nums[ix] <= target:
            if _helper(nums, target - nums[ix], ix + 1):
                return True
        _helper(nums, target, ix + 1)
        return True
    return _helper(nums, sum(nums) // 2, 0)


def canPartition_dp(nums):  # O(NS) where N is the total numbers and S is the sum
    s = sum(nums) // 2
    if sum(nums) % 2 == 1: return False
    # dp = [[-1] * range(s + 1) for _ in range(len(nums))]
    dp = [[None for x in range(s + 1)] for y in range(len(nums))]
    for row in range(0, len(nums)):  # first column
        dp[row][0] = True
    for col in range(1, s + 1):  # another way to say: if nums[0] != col: dp[0][col] = False 
        dp[0][col] = nums[0] == col
    for i in range(1, len(nums)):
        for j in range(1, s + 1):
            # if we can get the sum 'j' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:  # else if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - nums[i]]
    return dp[-1][-1]


def canPartition_dp_alt(nums):
    """
    same as above with slight variations to how we fill out the dp
    """
    if sum(nums) % 2 == 1: return False 
    s = sum(nums) // 2
    dp = [[True] * (s + 1) for _ in range(len(nums))]  # cols are from 0 to the sum, rows are just numbers from nums
    for col in range(1, s + 1):  # first row from (1, 0) is False if the first number isn't equal to the sum we're looking at right now (which is col)
        if nums[0] != col:
            dp[0][col] = False
    for row in range(1, len(nums)):  # fill out from (1, 1)
        for col in range(1, s + 1):
            if nums[row] > col:  # if the current number is larger than the sum we're working with
                dp[row][col] = dp[row - 1][col]  # take the result from the row above
            else: # otherwise make a choice between taking the current number and the complement or not taking the current number (and going with the upper row)
                dp[row][col] = dp[row - 1][col - nums[row]] or dp[row - 1][col]
    # print(dp)
    return dp[-1][-1]


def canPartition_optimized_dp(nums): # O(NS) and O(N) N is the total numbers and S is the sum
     """
    O(NS) N is the total number of numbers and S is the sum, subset_sum
    O(N)
    For any element i, we need the results of the prev (i-1) iteration. 
    If total_sum is odd, we cannot cut it into two equal subsets
    Construct a dp list 
    dp[j] is True if a subset with sum j can be formed from the elements in nums 
    dp[0] is 0 b/c it's always possible to create a subset with the sum of 0 by
    not taking any elements 

    Iterate through each number
    for each curr, iterate backwards from subset_sum down to curr.
    The backward iteration prevents  reusing the same element within the same pass
    For each possible sum j, we update dp[j]
    if dp[j] is already True, or dp[j-curr] is True, then setrting dp[j] to True
    means that by adding curr we can achieve a subset sum of j
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:  # edge case: cannot be cut into two parts 
        return False
    subset_sum = total_sum // 2  # goal 
    dp = [False] * (subset_sum + 1)
    dp[0] = True
    for curr in nums:
        for j in range(subset_sum, curr - 1, -1):
            dp[j] = dp[j] or dp[j - curr]
    return dp[subset_sum]


if __name__ == '__main__':
    # print(canPartition([1, 5, 11, 5]))
    # print(canPartition([1, 2, 3, 5]))
    # print(canPartition_brute_force([1, 5, 11, 5]))
    # print(canPartition_brute_force([1, 2, 3, 5]))
    # print(canPartition_dp([1, 5, 11, 5]))
    # print(canPartition_dp([1, 2, 3, 5]))
    # print(canPartition_dp([2, 2, 3, 5]))
    print(canPartition_dp_alt([1, 5, 11, 5]))
    print(canPartition_dp_alt([1, 2, 3, 5]))
    # print(canPartition_optimized_dp([2, 2, 3, 5]))
