# helper solves a normal problem but we run helper twice: on nums starting with the second element to the end of the list
# and on nums starting from the first element but without the last. Between the two, we choose the max value
def rob(self, nums: List[int]) -> int:
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

