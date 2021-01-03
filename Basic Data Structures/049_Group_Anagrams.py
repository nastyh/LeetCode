from collections import Counter, defaultdict

def groupAnagrams_alt(strs):  # O(NKlogK) where N is the length of strs, K is the max length of an element in strs. O(NK)
    """
    Idea is that the key is the strings in the sorted order (eat becomes aet).
    And then keys' values are actual words that can be formed from these keys
    """
    if len(strs) == 1:
        return [strs]
    d = defaultdict(list)
    for candidate in strs:
        t = ''.join(sorted(candidate))  # won't work without this reassignment 
        d[t].append(candidate)
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
