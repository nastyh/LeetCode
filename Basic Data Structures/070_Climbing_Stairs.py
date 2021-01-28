def stairs_optimal(n):  # O(n) and O(1)
	"""
	Don't need the whole dp list. 2 variables are enough
	l and r keep the initial edge cases
	Then we need to update them at the same time: turn l into r and for r it's l + r (l)
	Interesting and not obvious while loop: going to n = 1, not to n = 0
	"""
	if n <= 2: return n
	l, r = 1, 2
	while n != 1:
		l, r = r, l + r
		n -= 1
	return l


def stairs(n):  # O(n) both
	"""
	DP approach
	Base cases are 0, 1, 2 steps. Don't have to have zero, though but for the sake of readability
	"""
	if n == 1:
		return 1
	dp = [0] * (n + 1)
	dp[1] = 1
	dp[2] = 2
	for i in range(3, len(dp)):
		dp[i] = dp[i - 2] + dp[i - 1]
	return dp[n]


def stairs_alt(n):
	if n <= 2:
		return n 
	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2
	for i in range(3, n + 1):
		dp[i] = dp[i - 2] + dp[i - 1]
	return dp[-1]
	
	
if __name__ == '__main__':
	print(stairs_optimal(3))
	print(stairs_optimal(4))
	print(stairs_optimal(5))
	print(stairs(3))
	print(stairs(4))
	print(stairs(5))
	print(stairs_alt(3))
	print(stairs_alt(4))
	print(stairs_alt(5))