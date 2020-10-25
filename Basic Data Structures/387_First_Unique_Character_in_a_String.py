from collections import OrderedDict, defaultdict
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

def firstUniqChar_alt(s):  # the straightforward one
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


def firstUniqChar_ordered(s):
    d = defaultdict(list)
    for k, v in enumerate(s):
        d[v].append(k)
    return [v if len(v) == 1 else -1 for v in d.values() ][0][0]    
    return [v for v in d.values() if len(v) == 1][0][0]
    return d


def firstUniqChar_another(s):
    """
    Pythonic
    edge cases: 0, 1 and all the same elements -- get them out the door immediately
    Build a defaultdict where keys are letters and values are indices of the letters in the string
    We need keys for which values are of the length 1 (means only one index, means it only appeared once)
    non-rep is a list of such keys
    If it's empty, it means there are not characters that repeat only once ('aabbcc'), then return -1
    Otherwise, take the first element of the list (apparently defaultdict() maintains an order in which it was populated)
    Return index of the when this element occured in the string 
    """
    if len(s) == 0: return -1
    if len(s) == 1: return 0
    if len(set(s)) == 1: return -1
    d = defaultdict(list)
    for ix, ch in enumerate(s):
        d[ch].append(ix)
    non_rep = [k for k, v in d.items() if len(v) == 1]
    if len(non_rep) == 0: return - 1
    else: non_rep = non_rep[0]
    return s.index(non_rep)


if __name__ == '__main__':
    # print(firstUniqChar('loveleetcode'))
    # print(firstUniqChar_alt('loveleetcode'))
    # print(firstUniqChar_ordered('loveleetcode'))
    print(firstUniqChar_another('leetcode'))
    print(firstUniqChar_another('loveleetcode'))
    # leetcode loveleetcode aadadaad
