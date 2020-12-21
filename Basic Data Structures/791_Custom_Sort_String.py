def customSortString(S, T):
    d = {v:k for k, v in enumerate(S)}
    the_rest = [i for i in T if i not in S]
    res = [""] * len(S)

    for ch in T:
        if ch in d:
            res[d[ch]] += ch
    return ''.join(i for i in res + the_rest)


def customSortString_sorting(S, T):  # O(nlogn) an O(n) 
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


if __name__ == '__main__':
    print(customSortString('cba', 'abcd'))
    print(customSortString_sorting('cba', 'abcd'))
    print(customSortString_sorting('exv', 'xwvee'))
