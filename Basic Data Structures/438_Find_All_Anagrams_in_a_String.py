from collections import Counter
def findAnagrams(s, p):
    l, r, res = 0, 0, []
    if len(s) == 0: return res
    if len(p) > len(s): return None

    d_p = Counter(p)
    # d_s = Counter(s)
    p_len = len(p)

    for i in range(len(s)):
        if i > p_len:
            d_p[]




if __name__ == '__main__':
    print(findAnagrams('cbaebabacd', 'abc'))
