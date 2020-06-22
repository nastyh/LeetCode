def numWays(self, n: int, k: int) -> int:
    """
    If we don't have posts, then nothing to paint, return 0
    If we have only one post, we can paint in k ways (by using any color)
    If we have two posts, we can either paint in the same color (C1/C1 or C2/C2) or in different colors: (C1/C2 or C2/C1). Overall it's four ways. 
    In a formula, it's same + diff. Same = k * 1 (any color for the first, exactly one color for the second). Diff is k * (k - 1)
    If we have three posts: if two previous posts have the same color, then the third can be colored in (k - 1) ways.
    If two previous are of different colors, then the third can be colored in k ways.
    Starting with the third, we need to keep "old" values. Third can be painted in the same color if the previous was different
    Third can be painted in a different color, if previous was same.
    And we move in this manner till the end of the list.
    It can be solved without a list by just updating same and diff but I decided to keep the list b/c it's closer to traditional DP exercises and feels
    more natural

    """
    if n == 0: return 0
    if n == 1: return k
    same = k
    diff = k * (k - 1)
    if n == 2: same + diff
    dp = [None] * (n + 1)
    dp[0] = 0
    dp[1] = k
    dp[2] = k + (k - 1) * k
    for i in range(3, n + 1):
        another_same = diff
        another_diff = (same + diff) * (k-1)
        same = another_same
        diff = another_diff
        dp[i] = same + diff
    return dp[-1]
        
