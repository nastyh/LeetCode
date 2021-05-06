def smallerNumbersThanCurrent(nums):  # O(n^2)
	"""
	Just check for every element if there are other elements smaller in the rest of the list
	"""
	res = []
	for k, v in enumerate(nums):
		curr = 0
		for el in nums[:k] + nums[k + 1:]:
			if el < v:
				curr += 1
		res.append(curr)
	return res
	

def smallerNumbersThanCurrent_sort(nums):  # O(n*logn)
	"""
	Sort nums and save in a separate list
	For every num in original nums place the index at which this num lives in the sorted list
	"""
	nums_sorted = sorted(nums)
	res = []
	for num in nums:
		res.append(nums_sorted.index(num))
	return res


def smallerNumbersThanCurrent_bin_search(nums):  # O(nlogn) and O(n) b/c of sorted_nums
	"""
	helper function to find the first occurance of a given number in a sorted list
	Then iterate over nums and pass each num into the helper function
	"""
	res = []
	def _helper(vals, target):
		res = 0
		l, r = 0, len(vals) - 1
		while l <= r:
			m = l + (r - l) // 2
			if vals[m] == target:
				res = m
				r = m - 1
			elif vals[m] < target:
				l = m + 1
			else:
				r = m - 1
		return res
	sorted_nums = sorted(nums)
	for num in nums:
		res.append(_helper(sorted_nums, num))
	return res 


if __name__ == '__main__':
	print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
	print(smallerNumbersThanCurrent([6, 5, 4, 8]))
	print(smallerNumbersThanCurrent([7, 7, 7, 7]))
	print(smallerNumbersThanCurrent_sort([8, 1, 2, 2, 3]))
	print(smallerNumbersThanCurrent_sort([6, 5, 4, 8]))
	print(smallerNumbersThanCurrent_sort([7, 7, 7, 7]))
	print(smallerNumbersThanCurrent_bin_search([8, 1, 2, 2, 3]))


    