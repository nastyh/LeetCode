from collections import defaultdict
def groupStrings(strings):  # O(N) both
    """
    ## 1. Intuition is: there will be some relative thing in common for all those strings. Ahhh yes, difference in ascii values
    ## 2. Store ascii value pairs in hashmap and group together.
    ## 3. If the diff in ascii become -ve then add 26
    ## Watchout : case : acz (2, 23), dfc (2, -3) ==> (2, -3+26 = 23) => can be clubbed together.
    """
    groups = defaultdict(list)
    for s in strings:
        pattern = ()
        for i in range(1,len(s)):
            pattern = pattern + ((ord(s[i]) - ord(s[i-1]) + 26 ) % 26,)
        groups[pattern].append(s)
    return groups.values()


def groupStrings_another(strings):
    hashmap = {}
	for s in strings:
		key = ()
		for i in range(len(s) - 1):
			circular_difference = 26 + ord(s[i+1]) - ord(s[i])
			key += (circular_difference % 26,)
		hashmap[key] = hashmap.get(key, []) + [s]
	return list(hashmap.values())