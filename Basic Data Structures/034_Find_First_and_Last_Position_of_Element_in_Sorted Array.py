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