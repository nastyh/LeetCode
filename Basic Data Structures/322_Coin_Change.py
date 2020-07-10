def coinchange(nums, target):
	if len(nums) == 0: return -1
	i, res = len(nums) - 1, 0
	nums.sort()
	while i != 0 or target != 0:
		if nums[i] > target:
			i -= 1
		elif nums[i] == target:
			return res
		else:
			continue
		res += target // nums[i]
		target = target % nums[i]
		i -= 1
	return res


def coinchange_naive(nums, target):
	if len(nums) == 0: return -1
	res = 0
	for coin in nums:
		while target >= coin:
			target -= coin
			res += 1
	return res


if __name__ == '__main__':
	# print(coinchange([1,2,5], 11))
	print(coinchange_naive([1,2,5], 11))