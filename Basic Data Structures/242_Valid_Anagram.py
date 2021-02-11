from collections import Counter
def isAnagram(s, t):
    s_d, t_d = {}, {}
    for i in s:
        if i in s_d:
            s_d[i] += 1
        else:
            s_d[i] = 1
    for j in t:
        if j in t_d:
            t_d[j] += 1
        else:
            t_d[j] = 1
    return s_d == t_d


def isAnagram_short(s, t):  # O(n) both
    return Counter(s) == Counter(t)


def isAnagram_sort(s, t):  # O(nlogn) and O(1)
    return sorted(s) == sorted(t)


def isAnagram_one_dict(s, t):  # O(n) both
    """
    Checking if the sum of all values == 0 won't work for a case 'aacc' 'ccac' b/c
    the dictionary will be {a: 1, c: -1}
    Sum is 0 but it's not an anagram 
    """
    s_d = Counter(s)
    for ch in t:
        if ch not in s_d:
            return False
        else:
            s_d[ch] -= 1
    return all(v == 0 for v in s_d.values())
