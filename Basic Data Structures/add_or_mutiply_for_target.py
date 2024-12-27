def can_reach(nums, target): 
    """
    Given a list and a target number, return true if any combination of addition and/or multiplication of the list numbers hits the target
    ignore order of operations
    Numbers must be used left to right and cannot reorder numbers in the list
    O(2**n) and O(n) due to the recursive stack
    """
    def _helper(nums, target, curr_ix, curr_res):
        if target == curr_res: return True 
        if curr_ix >= len(nums) or curr_res > target:
            return False 
        return (_helper(nums, target, curr_ix + 1, curr_res + nums[curr_ix]) or _helper(nums, target, curr_ix + 1, curr_res * nums[curr_ix]))

    return _helper(nums, target, 0, 0)

def can_reach_dp(nums, target): 
    """
    O(nT), where n = len(nums), T = target + 1
    O(nT) for dp 
    """
    max_possible = target + 1
    # len(nums) + 1 the possible indices in nums
    # max_possible is set to target + 1 to limit the size of intermediate results.
    dp = [[None] * max_possible for _ in range(len(nums) + 1)]
    # Each state (curr_ix, curr_res) is stored in the dp table. If a state has been computed before,
    # it is reused instead of recalculating.

    def _helper(curr_ix, curr_res):
        if curr_res == target:
            return True
        if curr_ix >= len(nums) or curr_res > target:
            return False
        if dp[curr_ix][curr_res] is not None:
            return dp[curr_ix][curr_res]

        # Explore both addition and multiplication paths
        result = (
            _helper(curr_ix + 1, curr_res + nums[curr_ix]) or
            _helper(curr_ix + 1, curr_res * nums[curr_ix])
        )
        dp[curr_ix][curr_res] = result
        return result
    return _helper(0, 0)