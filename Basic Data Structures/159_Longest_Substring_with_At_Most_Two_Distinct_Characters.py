import math
from collections import defaultdict

def lengthOfLongestSubstringTwoDistinct_easy(s):
    """
    keep building a dictionary by moving the right pointer
    if the dictionary has more that two elements, it's time to start moving the left pointer
    Move the left pointer and decrement the count
    Once the count for the left character is zero, remove the whole thing from the dictionary 
    """
    if len(s) < 2: return len(s)
    l, r, res, d = 0, 0, -math.inf, {}
    while r < len(s):
        if s[r] not in d:
            d[s[r]] = 1
        else:
            d[s[r]] += 1
        while len(d) > 2:
            d[s[l]] -= 1             
            if d[s[l]] == 0:
                del d[s[l]]
            l += 1
        res = max(res, r - l + 1)
        r += 1
    return res


def lengthOfLongestSubstringTwoDistinct_no_space(s):
    last_char = ''
    second_last_char = ''
    last_char_count = 0
    maximum = 0
    currentMax = 0
    
    for char in s:
        if char == last_char or char == second_last_char:
            currentMax += 1
        else:
            currentMax = last_char_count + 1
            
        if char == last_char:
            last_char_count += 1
        else:
            last_char_count = 1
            second_last_char = last_char
            last_char = char    
        maximum = max(currentMax, maximum)        
    return maximum


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
