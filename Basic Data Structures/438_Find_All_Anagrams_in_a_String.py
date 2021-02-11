from collections import Counter
# def findAnagrams(s, p): # s -- long, p -- short
#     l, r, res = 0, 0, []
#     if len(s) == 0: return res
#     if len(p) > len(s): return None

#     d_p = Counter(p)
#     p_len = len(d_p)

#     for r in range(len(s)):
#         if s[r] in d_p:
#             d_p[s[r]] -= 1
#         if d_p[s[r]] == 0: # if a given value in the dictionary == 0:
#             p_len -= 1 # subtract 1 from p_len
#         if p_len == 0: # when p_len is all zero, it means we've met all characters from p in s
#             res.append(r - len(p) + 1) # we need to append the index from which we started seeing our characters. It's where we are at now minus the length of p plus 1.
#             # res.append(l)
#             # for the first instance, we're done once we hit 'a' at index 2. So we do 2 minus len(p) + 1. It gives us zero, or the index of 'c,' the first characted that contributed to the anagram we're looking for
#         for i in range(len(p), len(s)): # but now we need to somehow move forward
#             if s[i-len(p)] in d_p:
#                 d_p[s[i-len(p)]] += 1
#                 if d_p[s[i-len(p)]] > 0 and d_p[s[i-len(p)]] < 2:
#                     p_len += 1

#             if s[i] in d_p:
#                 d_p[s[i]] -= 1
#                 if d_p[s[i]] == 0:
#                     p_len -= 1
#             if p_len == 0:
#                 res.append(i - len(p) + 1)
#         # if r - l == len(p) - 1:
#         #     d_p[s[l]] += 1
#         #     if d_p[s[l]] > 0:
#         #         p_len += 1
#         #     l += 1

#     return res

def findAnagrams_one_more(s, p):  # O(len(s) + len(p)) both. Pass through both strings and maintain dicts
    """
    Build original dictionaries: one for string p (it won't change)
    another for string p (this will be updated)
    Two pointers: start moving
    If dictionaries are the same, it means palindromes, save the left index
    Then need to move the left border one step right. Decrement the respective value in the dictionary,
    if it becomes 0, delete the whole record
    Now we also need to move the right pointer.
    Be accurate with indices here. Check the letter at the index r + 1 but first check that r + 1 isn't out of bounds
    Make an update to the dictionary and then actually move the right index.
    """
    res = []
    p_d = Counter(p)
    s_d = Counter(s[0: len(p)])
    l = 0
    r = l + len(p) - 1
    while r < len(s):
        if p_d == s_d:
            res.append(l)
        s_d[s[l]] -= 1
        if s_d[s[l]] == 0:
            del s_d[s[l]]
        l += 1
        if r + 1 < len(s):
            if s[r + 1] not in s_d:
                s_d[s[r + 1]] = 1
            else:
                s_d[s[r + 1]] += 1
        r += 1
    return res 


def findAnagrams_sorted(s, p):
    len_p = len(p)
    target = Counter(p)
    res = []

    for i in range(len_p, len(s) + 1):
        if Counter(s[i - len_p:i]) == target:
            res.append(i - len_p)
    return res


def findAnagrams_another_sorting(s, p):  #  O(nlogn) and O(n); very slow but works
    """
    Start the loop from the index equal to the length of p
    slice the s by subtracting the length of p and adding 1, all the way to the current index
    if sorted lines are equal, append the left border
    """
    p = sorted(p)
    res = []
    for i in range(len(p) - 1, len(s)):
        if sorted(s[i - len(p) + 1:i + 1]) == p:
            res.append(i - len(p) + 1)
    return res


def findAnagrams_dicts(s, p):
    len_s, len_p = len(s), len(p)
    if len_s < len_p:
        return []
    p_count = Counter(p)
    s_count = Counter()
    res = []
    for i in range(len_s):  # going element by element through the long string s
        s_count[s[i]] += 1
        if i >= len_p: # if we past three elements:
            if s_count[s[i - len_p]] == 1:  # if it's the last element, remove
                del s_count[s[i - len_p]]
            else:
                s_count[s[i - len_p]] -= 1  # otherwise, decrement
        if p_count == s_count:
            res.append(i - len_p + 1)
    return res


def findAnagrams_another(s, p):
    l, r, res, d, l_p = 0, 0, [], Counter(p), len(p)
    while r < len(s):
        if d[s[r]] == 1:
            d[s[r]] -= 1
            if d[s[r]] == 0:
                l_p -= 1
            r += 1
        while l_p == 0:
            if r - l == len(p):
                res.append(l)
            if d[s[l]] == 1:
                d[s[l]] += 1
                if d[s[l]] > 0:
                    l_p += 1
                l += 1
            # r += 1
    return res


def findAnagrams_counter(s, p): # times out but works
    res = []
    def _isAn(s1, s2):
        return Counter(s1) == Counter(s2)
    l, r = 0, len(p) - 1
    while r < len(s):
        if _isAn(s[l:r + 1], p):
            res.append(l)
            l += 1
            r += 1
        else:
            l += 1
            r += 1
    return res


def findAnagrams_counter_another(s, p):  # times out but works
    res = []
    def _helper(a, b):
        return Counter(a) == Counter(b)
    i = len(p)
    while i <= len(s):
        candidate = s[i - len(p): i]
        if _helper(candidate, p):
            res.append(i - len(p))
        i += 1
    return res 


def findAnagrams_one_more(s, p):  # times out but works
    res = []
    p_d = Counter(p)
    s_d = Counter(s[0: len(p)])
    l = 0
    r = l + len(p) - 1
    while r < len(s):
        if p_d == s_d:
            res.append(l)
        s_d[s[l]] -= 1
        if s_d[s[l]] == 0:
            del s_d[s[l]]
        l += 1
        if r + 1 < len(s):
            if s[r + 1] not in s_d:
                s_d[s[r + 1]] = 1
            else:
                s_d[s[r + 1]] += 1
        r += 1
    return res 


if __name__ == '__main__':
    # print(findAnagrams('cbaebabacd', 'abc'))
    print(findAnagrams_dicts('cbaebabacd', 'abc'))
    print(findAnagrams_sorted('cbaebabacd', 'abc'))
    # print(findAnagrams_another('cbaebabacd', 'abc'))
    print(findAnagrams_counter('cbaebabacd', 'abc'))
    print(findAnagrams_counter('abab', 'ab'))
    print(findAnagrams_counter_another('cbaebabacd', 'abc'))
    print(findAnagrams_counter_another('abab', 'ab'))
    print(findAnagrams_one_more('cbaebabacd', 'abc'))
    print(findAnagrams_one_more('abab', 'ab'))