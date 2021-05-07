def minimumDeleteSum(s1, s2):  # O(mn) both, where m and n are lengths 
    """
    Idea is a combination of the longest common subsequence (1143) and Delete Operation for two strings (583)
    Need to find the longest common subsequence, calculate its ord value and subtract the double of it
    from the sum of ord values of strings s1 and s2
    """
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for r in range(1, len(s1) + 1):
        for c in range(1, len(s2) + 1):
            if s2[c - 1] == s1[r - 1]:
                dp[r][c] = dp[r - 1][c - 1] + ord(s1[r - 1])
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
    # return sum(map(ord, s1 + s2)) - dp[-1][-1] * 2
    return sum(ord(ch) for ch in s1) + sum(ord(ch) for ch in s2) - 2 * dp[-1][-1]


def minimumDeleteSum_space_efficient(s1, s2):  # O(mn) and O(2n)
    """
    Space optimization b/c we need only two rows 
    """
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(2)]
    res = 0
    for row in range(1, len(s1) + 1):
        for col in range(1, len(s2) + 1):
            if s1[row - 1] == s2[col - 1]:
                dp[row % 2][col] = ord(s1[row - 1]) + dp[(row - 1) % 2][col - 1]
            else:
                dp[row % 2][col] = max(dp[(row - 1) % 2][col], dp[row % 2][col - 1])
            res = max(res, dp[row % 2][col])
    return sum(ord(ch) for ch in s1) + sum(ord(ch) for ch in s2) - 2 * res


if __name__ == '__main__':
    print(minimumDeleteSum('sea', 'eat')) 
    print(minimumDeleteSum('delete', 'leet')) 
    print(minimumDeleteSum_space_efficient('sea', 'eat')) 
    print(minimumDeleteSum_space_efficient('delete', 'leet')) 
 