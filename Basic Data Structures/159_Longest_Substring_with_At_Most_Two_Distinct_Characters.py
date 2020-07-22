import math
from collections import defaultdict
def lengthOfLongestSubstringTwoDistinct(s):
    if len(s) == 0: return 0
    l, r, d, res = 0, 0, defaultdict(int), -math.inf
    while r < len(s):
        d[s[r]] += 1
        r += 1
        while len(d) > 2:
            d[s[l]] -= 1
            if d[s[l]] == 0:
                del d[s[l]]
            l += 1
        res = max(res, r - l)
    return res


if __name__ == '__main__':
    print(lengthOfLongestSubstringTwoDistinct('eceba'))
    print(lengthOfLongestSubstringTwoDistinct('ccaabbb'))
