def isIsomorphic(s, t):
    d = {}
    for ix, ch in enumerate(s):
        if ch not in d:
        	d[ch] = t[ix]
        else:
        	if d[ch] != t[ix]:
        		return False
    return True

def isIsomorphic_2way(s, t):
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

if __name__ == '__main__':
	print(isIsomorphic('egg','add'))
	print(isIsomorphic('foo','bar'))
	print(isIsomorphic('paper','title'))
	print(isIsomorphic('ab','aa'))
	print(isIsomorphic_2way('egg','add'))
	print(isIsomorphic_2way('foo','bar'))
	print(isIsomorphic_2way('paper','title'))
	print(isIsomorphic_2way('ab','aa'))
