from collections import Counter
def customSortString(S, T):  # O(n) both 
    """
    Dictionary: letter: index
    the_rest is the list with all other letters in T that aren't in S
    Iterate over T and put characters from the dictionary at the right spots
    At the end include leftovers 
    """
    d = {v : k for k, v in enumerate(S)}
    the_rest = [i for i in T if i not in S]
    res = [""] * len(S)  # important to have a list of stringgs
    for ch in T:
        if ch in d:
            res[d[ch]] += ch  # important not to overwrite but to add chars for edge cases when there are two same letters next to each other
    return ''.join(i for i in res + the_rest)


def customSortString_sorting_counter(S, T):  # O(n) both
    """
    Counter for T
    go through the letters in S.
    If this letter exists in d, append it to res whatever many times it's in d
    Make these counts = 0
    After that you're left with non-zero keys in d that are letters that are leftovers
    """
    d = Counter(T)
    res = ''
    for i in range(len(S)):
        if S[i] in d:
            res += S[i] * d[S[i]]
            d[S[i]] = 0
    for k, v in d.items():
        if v != 0:
            res += k * v 
    return res


def customSortString_sorting(S, T):  # O(nlogn) an O(n) 
    """
    Brute force solution

    """
    d = {}
    for k, v in enumerate(S):  # {c: 0, b: 1, a: 2}
        d[v] = k
    d_opposite = {}
    for k, v in d.items():  # {0: c, 1: b, 2: a}
        d_opposite[v] = k
    T_nums = []
    for ch in T:
        if ch in d:
            T_nums.append(d[ch])
    T_nums.sort()
    res = []
    for num in T_nums:
        res.append(d_opposite[num])
    if len(res) != len(T):
        for ch in T:
            if ch not in d:
                res.append(ch)
    return ''.join(res)


def customSortString_sorting_another(S, T): # slight more Pythonic, but slowish
    d = {}
    d_opposite = {}
    res = ''
    t_list = []
    for k, v in enumerate(S):  # letter to index
        d[v] = k
    for k, v in enumerate(S):  # index to letter
        d_opposite[k] = v
    for ch in T:
        if ch in d:
            t_list.append(d[ch])
    t_list.sort()
    letters_left = ''
    letters_left += ''.join(ch for ch in T if ch not in d)  # all letters that are in T but not in S. Will append them at the end
    for ix in t_list:  # building the main portion
        if ix in d_opposite:
            res += d_opposite[ix]
    return res + letters_left  # adding leftovers 


if __name__ == '__main__':
    print(customSortString('cba', 'abcd'))
    print(customSortString_sorting('cba', 'abcd'))
    print(customSortString_sorting('exv', 'xwvee'))
