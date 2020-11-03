 def maxPower(s):  # O(n) and O(1)
     """
     Linear scan: if the elements are equal, add 1 to curr, update the global variable
     """
    if len(s) == 1: return 1
    res = 1
    curr = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            curr += 1
            res = max(res, curr)
        else:
            curr = 1
    return res 


def maxPower_dp(s):  # O(n) and O(n)
    """
    dp approach:
    have a list of ones. If you see two elements that are the same, update the respective element in the dp list 
    """
    if len(s) == 1: return 1
    if len(s) == len(set(s)): return 1
    dp = [1] * len(s)
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            dp[i] = max(dp[i], dp[i - 1] + 1)
    return max(dp)