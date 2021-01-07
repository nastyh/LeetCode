import math
def lengthOfLongestSubstring_optimal(s):  # O(n) both
    if len(s) <= 1: return len(s)
    if len(set(s)) == 1: return 1
    l, r, storage, res = 0, 0, set(), -math.inf
    while r < len(s):
        if s[r] not in storage:
            storage.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        else:
            storage.remove(s[l])
            l += 1
    return res


def lengthOfLongestSubstring(s):
    m = set()
    res, l, i = 0, 0, 0

    while i < len(s):
        if s[i] not in m:
            m.add(s[i])
            res = max(res, len(m))
            i += 1
        else:
            m.remove(s[l])
            l += 1
    return res


def lengthOfLongestSubstring_dict(s):
    dic = {}
    res = 0
    left = -1
    for i, ch in enumerate(s):
        if ch in dic:
            left = max(left, dic[ch])
        dic[ch] = i
        res = max(res, i - left)
    return res


def lengthOfLongestSubstring_dict_alt(s):
    d, l, res = {}, 0, 0
    for k, v in enumerate(s):
        if v in d and d[v] >= l:
            l = d[v] + 1
        else:
            res = max(res, k - l + 1)
        d[v] = k
    return res


def lengthOfLongestSubstring_set(s):
    storage, curr, glob, l = set(), 0, 0, 0
    for char in s:
        if char not in storage:
            storage.add(char)
            curr = len(storage)
            glob = max(glob, curr)

        else:

            storage.remove(s[l])
            l += 1
    return glob


def lengthOfLongestSubstring_stack(s):
        stack = []
        res = 0
        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
                res=max(res, len(stack))
            elif s[i] in stack:
                stack=stack[stack.index(s[i]) + 1:] + [s[i]]
        return res


def lengthOfLongestSubstring_any(s):   # works but slow
    l, r, res, d = 0, 0, 0, {}
    if len(s) <= 1: return len(s)
    if len(set(s)) == 1: return len(set(s))
    while r < len(s):
        if s[r] not in d:
            d[s[r]] = 1
        else:
            d[s[r]] += 1
        while any(v > 1 for v in d.values()):
            d[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
        r += 1
    return res


if __name__ == '__main__':
    print(lengthOfLongestSubstring_optimal('abcabcbb'))
    print(lengthOfLongestSubstring_optimal('abcbbcbb'))
    print(lengthOfLongestSubstring_optimal('au'))
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring_dict('abcabcbb'))
    print(lengthOfLongestSubstring_dict_alt('au')) #pwwkew
    print(lengthOfLongestSubstring_set('pwwkew'))
    print(lengthOfLongestSubstring_any('pwwkew'))
    print(lengthOfLongestSubstring_dict('abcabcbb'))
