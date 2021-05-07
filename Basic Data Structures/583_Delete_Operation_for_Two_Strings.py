def minDistance(word1, word2):  # O(mn) both, where m and n are lengths of words
    """
    The idea is to solve the longest common subsequene problem (1143) 
    and substract its double length from the sum of lengths of both words
    Why double the length?
    We need to remove the longest common subsequence from both words. What we're left with is
    letters that aren't common. Thus, these are the letters that need to be removed in order 
    to make two words equal
    """
    dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
    for r in range(1, len(word2) + 1):
        for c in range(1, len(word1) + 1):
            if word1[c - 1] == word2[r - 1]:
                 dp[r][c] = dp[r - 1][c - 1] + 1
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
    return len(word1) + len(word2) - 2 * dp[-1][-1]


def minDistance_space_efficient(word1, word2):  # O(mn) and O(2n) 
    """
    Space optimization: we only need two rows in dp to keep track of the results
    """
    dp = [[0 for _ in range(len(word2) + 1)] for _ in range(2)]
    res = 0
    for row in range(1, len(word1) + 1):
        for col in range(1, len(word2) + 1):
            if word1[row - 1] == word2[col - 1]:
                dp[row % 2][col] = 1 + dp[(row - 1) % 2][col - 1]
            else:
                dp[row % 2][col] = max(dp[(row - 1) % 2][col], dp[row % 2][col - 1])
            res = max(res, dp[row % 2][col])
    return len(word1) + len(word2) - 2 * res


if __name__ == '__main__': 
    print(minDistance('sea', 'eat'))
    print(minDistance('leetcode', 'etco'))
    print(minDistance_space_efficient('sea', 'eat'))
    print(minDistance_space_efficient('leetcode', 'etco'))