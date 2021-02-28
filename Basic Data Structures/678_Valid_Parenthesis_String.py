def checkValidString_optimal(s):  # O(n) and O(1)
    """
    We track the fewest and most open (left - "(" ) parentheses that we can potentially have
    with low and high counters, and will check if we can reduce that to zero,
    meaning we can close every open parenthesis.
    """
    low, high = 0, 0
    tokens = {"(": (1, 1), ")": (-1, -1), "*": (-1, 1)}
    for c in s:
        l, h = tokens[c]
        low += l
        high += h
    if high < 0:
        return False  # too many closes
    low = max(low, 0)  # "*" and ")" can only close to the left
    return low == 0


def checkValidString_dp(s):  # O(n^3) b/c N^2 states and O(n) work to do on average, O(N^2)
    if not s: return True
    LEFTY, RIGHTY = '(*', ')*'
    n = len(s)
    dp = [[False] * n for _ in s]
    for i in range(n):
        if s[i] == '*':
            dp[i][i] = True
        if i < n - 1 and s[i] in LEFTY and s[i + 1] in RIGHTY:
            dp[i][i + 1] = True
    for size in range(2, n):
        for i in xrange(n - size):
            if s[i] == '*' and dp[i + 1][i + size]:
                dp[i][i + size] = True
            elif s[i] in LEFTY:
                for k in range(i + 1, i + size + 1):
                    if (s[k] in RIGHTY and
                            (k == i + 1 or dp[i + 1][k - 1]) and
                            (k == i + size or dp[k + 1][i + size])):
                        dp[i][i + size] = True
    return dp[0][-1]