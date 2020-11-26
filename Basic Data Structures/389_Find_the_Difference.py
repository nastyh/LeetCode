from collections import Counter
def findTheDifference(s, t):  # most optimal solution: O(n) and O(1) 
    res = 0
    for ch in s:
        res ^= ord(ch)
    for ch in t:
        res ^= ord(ch)
    return chr(res)
    

def findTheDifference_dict(s, t):  # straightforward but uses extra space
    s_d, t_d = Counter(s), Counter(t)
    for k, v in t_d.items():
        if s_d[k] != t_d[k]:
            return k


def findTheDifference_dict_optimized(s, t):  # slight modification, uses only one dictionary instead of two
    t_d = Counter(t)
    for ch in s:
        if ch in t_d:
            t_d[ch] -= 1
    return [k for (k, v) in t_d.items() if v == 1][0]


def findTheDifference_traversal(s, t):
    """
    Slow solution uses no extra space
    Go through t. 
    If you find a match, you need to exclude this letter from further consideration in s.
    Otherwise, it will fail for s = 'a' and t = 'aa'
    If there is no match, return it immediately
    """
    for ch in t:
        if ch in s:
            s = s[:s.index(ch)] + s[s.index(ch) + 1:]
        else:
            return ch


def findTheDifference_sort(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    i = 0
    while i < len(s):
        if sorted_s[i] != sorted_t[i]:
            return sorted_t[i]
        i += 1
    return sorted_t[i]


if __name__ == '__main__':
    print(findTheDifference('abcd', 'abcde'))
    print(findTheDifference('a', 'aa'))
    print(findTheDifference_dict('abcd', 'abcde'))
    print(findTheDifference_dict('a', 'aa'))
    print(findTheDifference_dict_optimized('abcd', 'abcde'))
    print(findTheDifference_dict_optimized('a', 'aa'))
