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


def groupAnagrams_easy_to_understand(strs):
    """
    anagrams, when sorted, are the same word
    So, this sorted word will be a key in the dictionary
    Iterate over and either create a new key-value pair or append to the existing one
    """
    d = defaultdict(list)
    res = []
    for s in strs:
        temp = ''.join(sorted(s))
        if temp not in d:
            d[temp] = [s]
        else:
            d[temp].append(s)
    for v in d.values():
        res.append(v)
    return res


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
