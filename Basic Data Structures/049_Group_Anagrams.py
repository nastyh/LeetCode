<<<<<<< HEAD
from collections import Counter
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


if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


=======
from collections import defaultdict
def groupAnagrams(strs):
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
>>>>>>> 6f7dbec22dbf499e2507ba1e2d19b19aaad28fbd
