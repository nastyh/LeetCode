from collections import Counter, defaultdict

def groupAnagrams_alt(strs):
    """
    Idea is that the key is the strings in the sorted order (eat becomes aet).
    And then keys' values are actual words that can be formed from these keys
    """
    if len(strs) == 0:
        return []
    d = defaultdict(list)
    for word in strs:
        t = ''.join(sorted(word))
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return [v for v in d.values()]


def groupAnagrams_another(strs):  # same as above but slightly different implementation
    if len(strs) == 0: return [[""]]
    if len(strs) == 1: return [strs]
    d = defaultdict(list)
    for word in strs:
        temp = sorted([w for w in word])
        d[tuple(temp)].append(word)
    return [v for v in d.values()]


if __name__ == '__main__':
    print(groupAnagrams_alt(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams_another(["eat", "tea", "tan", "ate", "nat", "bat"]))
