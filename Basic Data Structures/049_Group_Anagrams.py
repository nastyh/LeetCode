from collections import Counter, defaultdict
def groupAnagrams(strs):
    res = []
    if len(strs) == 0:
        return res

    def _helper(s1, s2):
        return Counter(s1) == Counter(s2)

    for i in range(len(strs) - 1):
        curr = [strs[i]] # eat
        for j in range(i + 1, len(strs)):
            # curr = [strs[i]]
            if _helper(strs[i], strs[j]): # helper(eat, tea)
                if strs[j] not in res:
                    curr.append(strs[j]) # eat, tea, ate
                # del strs[j] # remove tea, ate
        res.append(curr)
    return res

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
	return d.values()


if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams_alt(["eat", "tea", "tan", "ate", "nat", "bat"]))
