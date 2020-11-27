def canJump(nums):  # optimal
    if len(nums) == 0: return False
    i = 0
    furtherst_ix = nums[0]
    while i < len(nums) and i <= furtherst_ix:
        new_ix = nums[i] + i
        furtherst_ix = max(furtherst_ix, new_ix)
        i += 1
    if i == len(nums):
        return True
    else:
        return False


def canJump_backtracking(nums):  # times out but works 2^n and O(n)
    def _helper(pos, nums):
        if pos == len(nums) - 1:
            return True
        furtherst = min(pos + nums[pos], len(nums) - 1)
        for i in range(pos + 1, furtherst + 1):
            if _helper(i, nums):
                return True
        return False
    return _helper(0, nums)


def canJump_bottoms_up(nums):  # times out but works
    dp = [False] * len(nums)
    dp[-1] = True
    for i in range(len(nums) - 2, -1, -1):
        n = nums[i]
        if n == 0:
            dp[i]=False
            continue
        for j in range(n, 0, -1):
            if i + j < len(dp) and dp[i + j] == True:
                dp[i] = True
                break
    return dp[0]


def canJump_top_down(nums):
    def _helper(nums, dp, ind):
        if nums[0] >= len(nums) or (nums[0] == 0 and len(nums) == 1): return True # [0] case
        if nums[0] == 0: return False
        if dp[ind]!=None:
            return dp[ind]
        status = True
        for i in range(1, nums[0]+1):
            if i==1:
                status = _helper(nums[i:], dp, ind + i)
            else:
                status = status or _helper(nums[i:], dp, ind + i)
        dp[ind] = status
        return dp[ind]
    t = list(set(nums))
    if len(t) == 1 and t[0]>=1: return True
    dp = [None] * len(nums)
    return _helper(nums, dp, 0)




if __name__ == '__main__':
    print(canJump([3, 2, 1, 0, 4]))
    print(canJump_backtracking([3, 2, 1, 0, 4]))
    print(canJump_top_down([3, 2, 1, 0, 4]))
