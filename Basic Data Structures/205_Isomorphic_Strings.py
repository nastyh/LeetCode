def isIsomorphic(s, t):  # O(n) both 
    d = {}
    for ix, ch in enumerate(s):
        if ch not in d:
        	d[ch] = t[ix]
        else:
        	if d[ch] != t[ix]:
        		return False
    return True
	

def isIsomorphic_2way(s, t):  # O(n) both 
	d = {}
	for ix, ch in enumerate(s):
		if ch not in d:
			if t[ix] in d.values():
				return False
			d[ch] = t[ix]
		else:
			if d[ch] != t[ix]:
				return False
	return True


def isIsomorphic_2passes(s, t);
	"""
	Two dictionaries for respective strings.
	Maps word from the first string to the word from the second string 
	Another is the opposite.
	Need to compare first to second and then second to first
	If mapping is wrong, return False. If it's ok, keep going 
	"""
	d_s, d_t = {}, {}
	if len(s) != len(t):  # edge case
		return False 

	for i in range(len(s)):
		if s[i] not in d_s:
			d_s[s[i]] = t[i]
		else:
			if d_s[s[i]] != t[i]:
				return False
			else:
				continue

	for j in range(len(t)):
		if t[j] not in d_t:
			d_t[t[j]] = s[j]
		else:
			if d_t[t[j]] != s[j]:
				return False
			else:
				continue
	return True

if __name__ == '__main__':
	print(isIsomorphic('egg','add'))
	print(isIsomorphic('foo','bar'))
	print(isIsomorphic('paper','title'))
	print(isIsomorphic('ab','aa'))
	print(isIsomorphic_2way('egg','add'))
	print(isIsomorphic_2way('foo','bar'))
	print(isIsomorphic_2way('paper','title'))
	print(isIsomorphic_2way('ab','aa'))
