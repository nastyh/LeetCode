from collections import Counter
import string

def sortString_sorting(s):
    d = Counter(s)
    result = []
    smallest = True
    while d:
        keys = [key for key in d]
        keys = sorted(keys) if smallest else sorted(keys, reverse = True)
        smallest = not smallest
        for key in keys:
            result.append(key)
            if d[key] == 1:
                del d[key]
            else:
                d[key] -= 1
    return ''.join(result)
    

def sortString(s):  # times out and doesn't work for ggggggg
    if len(s) == 1: return s
    res = ''
    alphabet = list(string.ascii_lowercase)
    d = Counter(s)
    d_len = sum(v for v in d.values())
    s_set = set()
    for ch in s:
        if ch not in s_set:
            s_set.add(ch)
    while d_len != 0:
        # for _ in range(len(set(s))):
        for ch in alphabet:
            if ch in s:
                res += ch
                d[ch] -= 1
                if d[ch] == 0:
                    d_len -= 1
        for ch in alphabet[::-1]:
            # for _ in range(len(set(s))):
            if ch in s:
                res += ch
                d[ch] -= 1
                if d[ch] == 0:
                    d_len -= 1
    return res[:len(s)]

"""
Dry run with rat
d = {r: 1 a: 1 t: 1}; d_len = 3
res = a, d = {r: 1 a: 0 t: 1}; d_len = 2
res = ar, d = {r: 0 a: 0 t: 1}; d_len = 1
res = art, d = {r: 0 a: 0 t: 0}; d_len = 0

Dry run with aaaabbbbcccc
d = {a: 4, b: 4, c: 4, d: 4}, d_len = 16
res = 

"""

if __name__ == '__main__':
    print(sortString('rat'))
    print(sortString('spo'))
    # print(sortString('gggggg'))
