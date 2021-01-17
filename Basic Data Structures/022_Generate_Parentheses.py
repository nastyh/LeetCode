def generateParenthesis(n):
	"""
	only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.
	We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
	"""
	ans = []
	def backtrack(S = '', left = 0, right = 0):
		if len(S) == 2 * n:
			ans.append(S)
			return
		if left < n:
			backtrack(S+'(', left + 1, right)
		if right < left:
			backtrack(S+')', left, right + 1)
	backtrack()
	return ans



def generateParenthesis_easier(n):  # O(4^n / sqrt(n)) both; coming from the N-th Catalan number 
	"""
	Helper takes n, number of opening, number of closing, final list, and the current string we're building
	Once the current string is done (has 2n elements), append to res
	When we build the string, we need to take care of
	- opening should always be <=n. In this case we can always add another opening
	- closing should always be <=n. In this case we can always add another closing
	Time complexity is the n-th Catalan number (1/(n + 1)) * (2n choose n); Assymptotically it's 4^n/(n * sqrt(n))
	Space complexity: same 
	"""
	res = []
	def _helper(n, op, cl, curr):
		if len(curr) == 2 * n:
			res.append(curr)
			return
		if op != cl:
			_helper(n, op, cl + 1, curr + ')')
		if op < n:
			_helper(n, op + 1, cl, curr + '(')
	_helper(n, 0, 0, '')
	return res


if __name__ == '__main__':
	print(generateParenthesis(3))
	print(generateParenthesis_easier(3))