def subsets(nums): # O(n*2**n), same space complexity
    n = len(nums)
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]
    return output


def subsets_another(nums):  # N * 2**N for both time and space b/c every element can be present or absent 
	result = []
	def helper(nums, start_index, subset):
		result.append(subset[:])        
		for i in range(start_index, len(nums)):
			subset.append(nums[i])         
			helper(nums, i + 1, subset)        
			subset.pop() 
	helper(nums, 0, [])  
	return result


def subsets_alt(nums):
	res = []
	def _helper(nums, ix, curr):
		# if ix >= len(nums): return
		res.append(curr[:])
		for i in range(ix, len(nums)):
			curr.append(nums[i])
			_helper(nums, i + 1, curr)
			curr.pop()
	_helper(nums, 0, [])
	return res


def subsets_iter(nums):
	if len(nums) == 0: return [[]]
	res = [[]]
	for num in nums:
		n = len(res)
		for i in range(n):
			r = res[i] + [num]
			res.append(r)
	return res


def subsets_backtr(nums): # O(n*2**n), same space complexity
	def backtrack(first, curr):
	# if the combination is done
		if len(curr) == k:  
			output.append(curr[:])
		for i in range(first, n):
			# add nums[i] into the current combination
			curr.append(nums[i])
			# use next integers to complete the combination
			backtrack(i + 1, curr)
			# backtrack
			curr.pop()
	output = []
	n = len(nums)
	for k in range(n + 1):
	    backtrack(0, [])
	return output


if __name__ == '__main__':
	print(subsets([1, 2, 3]))
	print(subsets_alt([1, 2, 3]))
	print(subsets_another([1, 2, 3]))
	print(subsets_backtr([1, 2, 3]))