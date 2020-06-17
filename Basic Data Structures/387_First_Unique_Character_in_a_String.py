from collections import OrderedDict 
def firstUniqChar(s):   # loveleetcode
    if len(s) == 0:
        return -1
    if len(s) == 1:
        return 0
    d = {}

    for el in s:
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1

    # return d
    if all(v % 2 == 0 for v in d.values()) or all(v % 2 == 1 for v in d.values()):
        return -1

    nonrep = [k for k, v in d.items() if v == 1] # v, t
                   # min([2, 7])
    indices = []
    for num in nonrep:
        indices.append(s.index(num))

    return min(indices)

def firstUniqChar_alt(s):
    d = OrderedDict()
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    for k, v in enumerate(s):
        if d[v] == 1:
            return k
    return -1


if __name__ == '__main__':
    print(firstUniqChar('loveleetcode'))
    print(firstUniqChar_alt('loveleetcode'))
    # leetcode loveleetcode aadadaad
