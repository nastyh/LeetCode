class Solution:
    def canJump_greedy(self, nums: List[int]) -> bool:
        """
        O(n) and O(1)
        We’ll define the variable last_reach_ix as the last element's index of the array.
        After each iteration, we’ll update the last_reach_ix variable by checking whether
        the last_reach_ix variable is reachable from that index. If yes, the current index becomes the new last_reach_ix.
        We keep on doing this until we reach the first element of the array.
        Now, we’ll check whether the last_reach_ix variable is equal to zero (index of the first variable),
        which means we could have reached the last element had we started from the first one.
        """
        last_reach_ix = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_reach_ix:
                last_reach_ix = i
        if last_reach_ix == 0:
            return True
        else: return False

     def canJump_back(self, nums: List[int]) -> bool:
        """
        O(n) and O(1)
        greedy approach
        if we go from the left, every time we want to arrive to the end asap
        to do so, we want to take the longest steps 
        But it can bring us to a bad situation. 
        max_reach_ix is the largest index of where we can get from a current cell
        if we are at ix=2 and the nums[ix] = 4, we can go to 2+1, 2+2, 2+3, 2+4
        The max here is 2+4=6
        If max_reach_ix is not less than i, it means we can reach this position,
        and therefore we update max_reach_ix to be the maximum of its current value and i + x, where
        x is the maximum jump length from the current position. 
        """
        max_reach_ix = 0
        for index, jump_length in enumerate(nums):
            if max_reach_ix < index: return False
        # best of where we are vs. where we can get 
            max_reach_ix = max(max_reach_ix, index + jump_length)
        return True


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
