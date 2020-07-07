def smallerNumbersThanCurrent(nums):
	res = []
	for k, v in enumerate(nums):
		curr = 0
		for el in nums[:k] + nums[k + 1:]:
			if el < v:
				curr += 1
		res.append(curr)
	return res

if __name__ == '__main__':
	print(smallerNumbersThanCurrent([8,1,2,2,3]))
	print(smallerNumbersThanCurrent([6, 5, 4, 8]))
	print(smallerNumbersThanCurrent([7, 7, 7, 7]))

    