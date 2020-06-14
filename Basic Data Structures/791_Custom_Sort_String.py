def customSortString(S, T):
    d = {v:k for k, v in enumerate(S)}
    # in_both = [i for i in T if i in S]
    the_rest = [i for i in T if i not in S]
    res = [""] * len(S)

    for ch in T:
        if ch in d:
            res[d[ch]] += ch
    return ''.join(i for i in res + the_rest)

if __name__ == '__main__':
    print(customSortString('cba', 'abcd'))
