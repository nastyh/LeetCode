# helper solves a normal problem but we run helper twice: on nums starting with the second element to the end of the list
# and on nums starting from the first element but without the last. Between the two, we choose the max value
def rob(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums)
    def _helper(nums):
        dp = [None] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return max(dp[-1], dp[-2])
    return max(_helper(nums[1:]), _helper(nums[:-1]))


def rob_linear(nums):
    """
    helper solves in the linear time by keeping track of the values two houses ago and updating the value one house ago
    """
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums)
    def _helper(nums):
        max_2_left, max_1_left = 0, 0
        for num in nums:
            max_2_left, max_1_left = max_1_left, max(max_2_left + num, max_1_left)
        return max_1_left
    first_pass = _helper(nums[1:])
    second_pass = _helper(nums[:-1])
    return max(first_pass, second_pass)



if __name__ == '__main__':
    print(rob([2, 3, 2]))
    print(rob_linear([2, 3, 2]))
    print(rob([1, 2, 3, 1]))
    print(rob_linear([1, 2, 3, 1]))
