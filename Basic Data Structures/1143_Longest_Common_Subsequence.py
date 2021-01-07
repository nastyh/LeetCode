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
    

def longestCommonSubsequence_alt(text1, text2):  # both O(mn), where m and n are lengths of strings
    """"
    create a dp matrix where cols are text1 + 1
    and rows are text2 + 1
    everything in the first row and the first col stays the same: 0
    Then start filling with (1, 1)
    It means comparing the first character in text1 to the first character in text2. 
    If they're the same, take the value from the diagonal (left and up) and add 1 to it
    If they're different, take the max of (cell to the left, cell up)
    Return the last element in the matrix
    """
    dp = [[0] * (len(text1) + 1) for _ in range((len(text2) + 1))]  # text1 is along the cols; text2 is along the rows
    for col in range(1, len(text1) + 1):
        for row in range(1, len(text2) + 1):
            if text1[col - 1] == text2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[-1][-1]


def longestCommonSubsequence_bottoms_up_efficient(text1, text2):  # o(mn) and O(2n)
    """
    same as above but keeping only two rows of data
    """
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(2)]
    res = 0
    for row in range(1, len(text1) + 1):
        for col in range(1, len(text2) + 1):
            if text1[row - 1] == text2[col - 1]:
                dp[row % 2][col] = 1 + dp[(row - 1) % 2][col - 1]
            else:
                dp[row % 2][col] = max(dp[(row - 1) % 2][col], dp[row % 2][col - 1])
            res = max(res, dp[row % 2][col])
    return res 


def longestCommonSubsequence_return_string(text1, text2):
    res = ''
    dp = [[0] * (len(text1) + 1) for _ in range((len(text2) + 1))]  # text1 is along the cols; text2 is along the rows
    for col in range(1, len(text1) + 1):
        for row in range(1, len(text2) + 1):
            if text1[col - 1] == text2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
                if len(res) > 0 and res[-1] != text1[col - 1]:
                    res += text1[col - 1]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return res


if __name__ == '__main__':
    print(longestCommonSubsequence('aab', 'azb'))
    print(longestCommonSubsequence('abcde', 'ace'))
    print(longestCommonSubsequence_bottoms_up_efficient('abcde', 'ace'))
    print(longestCommonSubsequence_return_string('aab', 'azb'))