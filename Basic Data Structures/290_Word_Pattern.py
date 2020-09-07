def wordPattern(pattern, str):
    if len(pattern) != len(str.split()): return False
    if len(set(pattern)) != len(set(str.split())): return False
    p_l, s_l = [ch for ch in pattern], [w for w in str.split()]
    d = {}
    for ix in range(len(p_l)):
        if p_l[ix] not in d:
            d[p_l[ix]] = s_l[ix]
        else:
            if d[p_l[ix]] != s_l[ix]:
                return False
    return True


if __name__ == '__main__':
    print(wordPattern('abba', 'dog cat cat dog'))  
    print(wordPattern('abba', 'dog cat cat fish'))
    print(wordPattern('aaaa', 'dog cat cat dog'))
    print(wordPattern('abba', 'dog dog dog dog'))
