def longestValidParentheses(s):  # O(n) and O(1)
    m = l = r = 0
    for e in s:
        if e == '(':
            l += 1
        else:
            r += 1
        if l==r:
            m = max(m,r + l)
        elif r > l:
            l = r = 0
    l = r = 0
    for e in s[::-1]:
        if e == ')':
            r += 1
        else: 
            l += 1
        if l == r: 
            m = max(m,r + l)
        elif l > r:
            l = r = 0
    return m


def longestValidParentheses_dp(s):  # O(n) both 
    """
    dp keeps the length of the longest substring that ends at a current ix
    Obviously, a good substring is the one that ends with an ')'
    So dp at indices where the symbol is '(' will always have 0
    Then start filling out
    """
    n = len(s)
    if n < 2:
        return 0
    # dp[i] = the length of the longest valid substring ending at s[i]
    dp = [0 for _ in range(n)]
    dp[1] = 2 if s[0:2] == '()' else 0
    for i in range(2, n):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            else:
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    prefix = dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0
                    dp[i] = prefix + dp[i-1] + 2
    return max(dp)