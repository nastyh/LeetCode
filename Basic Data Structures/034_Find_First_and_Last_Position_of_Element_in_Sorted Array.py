def searchRange(nums, target):  # O(n) run time
	res = []
	for l in range(len(nums)):
		if nums[l] == target:
			res.append(l)
	if len(res) == 0:
		return [-1, -1]
	else:
		return [res[0], res[-1]]


def searchRange_binary(nums, target): # log(n) time; binary search
	def _helper(nums, target, isLeft):
		l, r = 0, len(nums)
		while l < r:
			mid = l + (r - l) // 2
			if nums[mid] > target or (isLeft and target == nums[mid]):
				r = mid
			else:
				l = mid + 1
		return l
	l_ix = _helper(nums, target, True)
	if l_ix == len(nums) or nums[l_ix] != target:
		return [-1, -1]
	return [l_ix, _helper(nums, target, False) - 1]


def searchRange_2_bin_searches(nums, target):
	"""
	make two binary searches.
	First, look for the most right element.
	Once we found nums[m] == target, don't return anything, but save most_right = m and move the left pointer to the right half,
	to keep searching for the most right element
	When we look for the most left element, the idea is similar:
	once we found nums[m] == target, don't return anything yet, but move r to m - 1 (to the left half) and keep searching for the most left element
	"""
	l, r, most_right = 0, len(nums) - 1, -1
	while l <= r:
		m = l + (r - l) // 2
		if nums[m] == target:
			most_right = m
			l = m + 1
		elif nums[m] < target:
			l = m + 1 
		else:
			r = m - 1
	l, r, most_left = 0, len(nums) - 1, -1
	while l <= r:
		m = l + (r - l) // 2
		if nums[m] == target:
			most_left = m
			r = m - 1
		elif nums[m] < target:
			l = m + 1
		else:
			r = m - 1
	return [most_left, most_right]



def searchRange_another_binary(nums, target):  # the longest but easiest to comprehend
	if not nums: return [-1, -1]
	def _left_helper(nums, l, r, target):
		while l < r:
			m_ix = l + (r - l) // 2
			if nums[m_ix] < target:
				l = m_ix + 1
			elif nums[m_ix - 1] < target:
				return m_ix
			else:
				r = m_ix - 1
		return l
	def _right_helper(nums, l, r, target):
		while l < r:
			m_ix = l + (r - l) // 2
			if nums[m_ix] > target:
				r = m_ix - 1
			elif nums[m_ix + 1] > target:
				return m_ix
			else:
				l = m_ix + 1
		return r
		
	l, r = 0, len(nums) - 1
	while l <= r:
		m = l + (r - l) // 2
		if nums[m] < target:
			l = m + 1
		elif nums[m] > target:
			r = m - 1
		else:
			return [_left_helper(nums, 0, m, target), _right_helper(nums, m, len(nums) - 1, target)]
	return [-1, -1]


if __name__ == '__main__':
	print(searchRange([5, 7, 7, 8, 8, 10], 8))
	print(searchRange([5, 7, 7, 8, 8, 10], 6))
	print(searchRange_binary([5, 7, 7, 8, 8, 10], 8))
	print(searchRange_binary([5, 7, 7, 8, 8, 10], 6))
	print(searchRange_another_binary([5, 7, 7, 8, 8, 10], 8))
	print(searchRange_another_binary([5, 7, 7, 8, 8, 10], 6))