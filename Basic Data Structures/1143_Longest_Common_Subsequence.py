def longestCommonSubsequence(text1, text2):  # O(n^2) and O(len(text1) * len(text2)) 
    """
    create dp that is one col and row larger than lengths of text1 and text2
    First col and row are zeros
    Start filling out from 1, 1
    Start comparing letters from text1 and text2
    If they're the same, take the value from the diagonal (left, up) cell and add 1 to it
    If they're not the same, take the max of the value to the left and value above
    Return the last element
    """
    dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
    for i in range(1, len(text1) + 1):  # i means cols
        for j in range(1, len(text2) + 1):  # j means rows
            if text1[i - 1] == text2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
    return dp[-1][-1]


if __name__ == '__main__':
    # print(longestCommonSubsequence('aab', 'azb'))
    print(longestCommonSubsequence('abcde', 'ace'))
