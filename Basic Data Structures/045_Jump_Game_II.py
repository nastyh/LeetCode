import math
def jump_dp_bottoms_up(nums):  # O(n^2) and O(n), TLA
    dp = [math.inf for _ in range(len(nums))]
    dp[0] = 0
    for l in range(len(nums) - 1):
        r = l + 1
        while r <= l + nums[l] and r < len(nums):
            dp[r] = min(dp[r], dp[l] + 1)
            r += 1
    return dp[-1]

def jump_greeedy(nums):  # O(n) and O(1)
    l, r = 0, 0
    res = 0
    while r < len(nums) - 1:
        newStart = r + 1
        newEnd = r + 1
        """find the new range of jumps"""
        for i in range(l, r  + 1):
            newEnd = max(i + nums[i], newEnd)
        l, r = newStart, newEnd
        res += 1
    return res


if __name__ == '__main__':
    print(jump_dp_bottoms_up([2, 3, 1, 1, 4]))
    print(jump_dp_bottoms_up([2, 3, 0, 1, 4]))
    print(jump_greeedy([2, 3, 1, 1, 4]))
    print(jump_greeedy([2, 3, 0, 1, 4]))