def subsets(nums): # O(n*2**n), same space complexity
    n = len(nums)
    output = [[]]
    
    for num in nums:
        output += [curr + [num] for curr in output]
    return output


def subsets_another(nums):
	def _helper(nums, curr_ix, curr_res, res):
		res.append(curr_res.copy())
		for i in range(curr_ix, len(nums)):
			curr_res.append(nums[i])
			_helper(nums, curr_ix + 1, curr_res, res)
			curr_res.pop()
		return  res
	return _helper(nums, 0, [], [])


def subsets_backtr(nums): # O(n*2**n), same space complexity
	def backtrack(first = 0, curr = []):
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
	    backtrack()
	return output


if __name__ == '__main__':
	# print(subsets([1, 2, 3]))
	print(subsets_another([1, 2, 3]))
	# print(subsets_backtr([1, 2, 3]))