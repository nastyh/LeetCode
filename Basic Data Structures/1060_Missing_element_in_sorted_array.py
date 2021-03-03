def missingElement(nums, k): # works but exceeds the time limit  O(n) both 
	full = [i for i in range(nums[0], nums[-1] + 1)]
	missing = [j for j in full if j not in nums]
	if k <= len(missing):
		return missing[k - 1]
	else:
		return nums[-1] + 1 * (k - len(missing))

def missingElement_binary_search(nums, k):  # O(logn) and O(1)
	def missingNums(i):
	    return nums[i] - nums[0] - i
        
	left, right = 0, len(nums)
	while left < right:
		middle = (left+right) // 2
		if missingNums(middle) < k:
			left = middle + 1
		else:
			right = middle 
	return nums[left -1] + k - missingNums(left -1)   


def missingElement_another(nums, k):
	"""
		i:           0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10
	nums:           10,   11,  14,  15,  20,  21,  23,  27,  33,  35, 36
	k_at_i:          0,   0,   2,   2,   6,   6,   7,   10,  15,  16, 16
	"""
	def first_occurence_of_k():
		left, right, result = 0, len(nums)-1, None
		while left <= right:
			mid = (left + right) // 2
			k_at_mid = (nums[mid] - nums[0] - 1) - (mid - 1)
			if k_at_mid < k:
				left = mid + 1
			elif k_at_mid >= k:
				result = [mid, k_at_mid]
				right = mid - 1
		return result

	result = first_occurence_of_k()
	# kth missing number is outside of nums.
	if not result:
		idx = len(nums)-1
		k_at_mid = nums[idx] - nums[0] - 1 - (idx-1)
		kth = nums[idx] - (k_at_mid - k)
	# kth missing is within array, subtract 1 since nums[idx] is not missing.
	else:
		idx, k_at_mid = result
		kth = (nums[idx] - 1) - (k_at_mid - k)
	return kth



if __name__ == '__main__':
	print(missingElement([4, 7, 9,10], 1))
	print(missingElement([4, 7, 9, 10], 3))
	print(missingElement([1, 2, 4], 3))
	print(missingElement_binary_search([4, 7, 9, 10], 1))
	print(missingElement_binary_search([4, 7, 9, 10], 3))
	print(missingElement_binary_search([1, 2, 4], 3))


        