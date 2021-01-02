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
    for col in range(1, s + 1):
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
    dp = [[True] * (s + 1) for _ in range(len(nums))]
    for col in range(1, s + 1):
        if nums[0] != col:
            dp[0][col] = False
    for row in range(1, len(nums)):
        for col in range(1, s + 1):
            if nums[row] > col:  # if the current number is larger than the sum we're working with
                dp[row][col] = dp[row - 1][col]  # take the result from the row above
            else: # otherwise make a choice between taking the current number and the complement or not taking the current number (and going with the upper row)
                dp[row][col] = dp[row - 1][col - nums[row]] or dp[row - 1][col]
    return dp[-1][-1]
    

if __name__ == '__main__':
    # print(canPartition([1, 5, 11, 5]))
    # print(canPartition([1, 2, 3, 5]))
    # print(canPartition_brute_force([1, 5, 11, 5]))
    # print(canPartition_brute_force([1, 2, 3, 5]))
    print(canPartition_dp([1, 5, 11, 5]))
    print(canPartition_dp([1, 2, 3, 5]))
    print(canPartition_dp([2, 2, 3, 5]))
    print(canPartition_dp_alt([1, 5, 11, 5]))
    print(canPartition_dp_alt([1, 2, 3, 5]))
    print(canPartition_dp_alt([2, 2, 3, 5]))