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
			backtrack(S+'(', left+1, right)
		if right < left:
			backtrack(S+')', left, right+1)

	backtrack()
	return ans

if __name__ == '__main__':
	print(generateParenthesis(3))