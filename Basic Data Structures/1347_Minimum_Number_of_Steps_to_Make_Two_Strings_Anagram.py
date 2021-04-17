from collections import Counter
def minSteps(s, t):  # O(n) both 
    """
    If t has a character that is not in s, then we should account for it
    But we also need to account for a situation when characters exist in both strings and the respective count in s > that in t. That balances out the previous
    """
    d_s, d_t = Counter(s), Counter(t)
    res = 0
    for ch in d_s:
        temp =  d_s[ch] - d_t.get(ch, 0)
        if temp > 0:
            res += temp
    return res