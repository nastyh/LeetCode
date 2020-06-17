def searchRange(nums, target):
	res = []
	for l in range(len(nums)):
		if nums[l] == target:
			res.append(l)
	if len(res) == 0:
		return [-1, -1]
	else:
		return [res[0], res[-1]]

def searchRange_binary(nums, target):
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

if __name__ == '__main__':
	print(searchRange([5,7,7,8,8,10], 8))
	print(searchRange([5,7,7,8,8,10], 6))
	print(searchRange_binary([5,7,7,8,8,10], 8))
	print(searchRange_binary([5,7,7,8,8,10], 6))