def smallerNumbersThanCurrent(nums):  # O(n^2)
	res = []
	for k, v in enumerate(nums):
		curr = 0
		for el in nums[:k] + nums[k + 1:]:
			if el < v:
				curr += 1
		res.append(curr)
	return res

def smallerNumbersThanCurrent_sort(nums):  # O(n*logn)
	nums_sorted = sorted(nums)
	res = []
	for num in nums:
		res.append(nums_sorted.index(num))
	return res


def smallerNumbersThanCurrent_zip(nums):
	nums_sorted = sorted(nums)
	res = [0] * len(nums)
	for i in range(1, len(nums_sorted)):
		if nums_sorted[i] > nums_sorted[i - 1]:
			res[i] = i
		else:
			res[i] = res[i - 1]
	combo = zip(nums, nums_sorted, res)
	return [x for _,_,x in sorted(combo, key = lambda x: x[1])]


if __name__ == '__main__':
	print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
	# print(smallerNumbersThanCurrent([6, 5, 4, 8]))
	# print(smallerNumbersThanCurrent([7, 7, 7, 7]))
	# print(smallerNumbersThanCurrent_sort([8, 1, 2, 2, 3]))
	# print(smallerNumbersThanCurrent_sort([6, 5, 4, 8]))
	# print(smallerNumbersThanCurrent_sort([7, 7, 7, 7]))
	print(smallerNumbersThanCurrent_zip([8, 1, 2, 2, 3]))

    