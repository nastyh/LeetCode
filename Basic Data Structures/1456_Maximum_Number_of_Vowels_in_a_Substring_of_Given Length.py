import math
def maxVowels(s, k): # times out
	vowels = 'aeiou'
	if len(s) == 0: return
	if k > len(s): return
	l, curr, curr_l, glob_l = 0, '', 0, -math.inf
	while l + k - 1 < len(s):
		curr = s[l:l + k]
		curr_l = sum([1 for symbol in curr if symbol in vowels])
		glob_l = max(glob_l, curr_l)
		l += 1
	return glob_l

def maxVowels_alt(s, k): # works 
	vowels = 'aeiou'
	if len(s) == 0: return
	if k > len(s): return
	l_ix, r_ix, length, glob_length = 0, 0, 0, -math.inf 
	for r_ix in range(len(s)):
		r_el = s[r_ix]
		if r_el in vowels:
			length += 1
		while r_ix - l_ix + 1 > k:
			l_el = s[l_ix]
			if l_el in vowels:
				length -= 1
			l_ix += 1
		if r_ix - l_ix + 1 == k:
			glob_length = max(glob_length, length)
	return glob_length

def maxVowels_short(s, k):
	curr_l, glob_l = 0, -math.inf
	vowels = 'aeiou'
	for ix, v in enumerate(s):
		if ix >= k:
			if s[ix - k] in vowels:
				curr_l -= 1
		if v in vowels:
			curr_l += 1
		glob_l = max(glob_l, curr_l)
	return glob_l


if __name__ == '__main__':
	# print(maxVowels('abciiidef', 3))
	# print(maxVowels('aeiou', 2))
	# print(maxVowels('leetcode', 3))
	# print(maxVowels('rhytms', 4))
	# print(maxVowels('tryhard', 4))
	# print(maxVowels_alt('abciiidef', 3))
	# print(maxVowels_alt('aeiou', 2))
	# print(maxVowels_alt('leetcode', 3))
	# print(maxVowels_alt('rhytms', 4))
	# print(maxVowels_alt('tryhard', 4))
	print(maxVowels_short('abciiidef', 3))
	print(maxVowels_short('aeiou', 2))
	print(maxVowels_short('leetcode', 3))
	print(maxVowels_short('rhytms', 4))
	print(maxVowels_short('tryhard', 4))

