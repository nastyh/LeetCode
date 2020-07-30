def longestCommonSubsequence(text1, text2):
    dp = [[None for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
    for i in range(len(text1) + 1):
        dp[0][i] = 0
    for j in range(len(text2) + 1):
        dp[j][0] = 0
    for i in range(1, len(text2)):
        for j in range(1, len(text1)):
            if text2[i] == text1[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


if __name__ == '__main__':
    print(longestCommonSubsequence('aab', 'azb'))