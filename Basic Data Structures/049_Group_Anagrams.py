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