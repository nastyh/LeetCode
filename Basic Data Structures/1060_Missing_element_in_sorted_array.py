def missingElement(nums, k): # works but exceeds the time limit
        full = [i for i in range(nums[0], nums[-1] + 1)]
        missing = [j for j in full if j not in nums]
        if k <= len(missing):
            return missing[k - 1]
        else:
            return nums[-1] + 1 * (k - len(missing))

def missingElement_binary_search(nums, k):
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


if __name__ == '__main__':
	print(missingElement([4,7,9,10], 1))
	print(missingElement([4,7,9,10], 3))
	print(missingElement([1,2,4], 3))
	print(missingElement_binary_search([4,7,9,10], 1))
	print(missingElement_binary_search([4,7,9,10], 3))
	print(missingElement_binary_search([1,2,4], 3))


        