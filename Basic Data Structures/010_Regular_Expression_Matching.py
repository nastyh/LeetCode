def isMatch_dp_top_down(s, p):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i + 1, j)
                else:
                    ans = first_match and dp(i + 1, j + 1)
            memo[i, j] = ans
        return memo[i, j]
    return dp(0, 0)


def isMatch_dp_bottom_up(s, p):  # O(sp) both where s and p are lengths respectively 
    """
    Save string-building ops 
    """
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    dp[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]

    return dp[0][0]


def isMatch_dp_bottom_up_another(s, p):
    n = len(s)
    m = len(p)
    # create a DP lookup table
    T = [[False for x in range(m + 1)] for y in range(n + 1)]
    # if both pattern and string are empty: match
    T[0][0] = True
    # handle empty string case (i == 0)
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            T[0][j] = T[0][j - 1]
    # build a matrix in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                T[i][j] = T[i - 1][j] or T[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                T[i][j] = T[i - 1][j - 1]
    # last cell stores the answer
    return T[n][m]