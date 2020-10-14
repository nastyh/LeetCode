def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for _ in range(k % len(nums)):
        p = nums.pop()
        nums.insert(0, p)
    return nums

def rotate_alt(nums, k):
	if len(nums) == 0: return 
	if len(nums) == 1: return nums
	if len(set(nums)) == 1: return nums

	for _ in range(k % len(nums)):
		l = nums.pop()
		nums = [l] + nums[:]
	return nums


def rotate_reversal(nums, k):
	r = nums[-(k % len(nums)):]
	rr = list(reversed(r))
	rest = nums[:(k % len(nums)) + 1]
	# return r + rest
	return nums[-(k % len(nums)):] + nums[:(k % len(nums)) + 1]


def rotate_short(nums, k):
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]


def rotate_another(nums, k):
    """
    Step 1: rotate the whole thing
    Step 2: rotate the first k elements
    Step 3: rotate the last len(nums) - k elements
    """
    def _helper(nums, l, r):
        return nums[l: r + 1][::-1] 
    nums = _helper(nums, 0, len(nums))
    nums[:k] = _helper(nums, 0, k - 1)
    nums[len(nums) - k - 1:] = _helper(nums, len(nums) - k - 1, len(nums))
    return nums


if __name__ == '__main__':
    print(rotate([1,2,3,4,5,6,7], 3))
    print(rotate([-1,-100,3,99], 2))
    print(rotate_alt([1,2,3,4,5,6,7], 3))
	print(rotate_reversal([1,2,3,4,5,6,7], 3))
    print(rotate_alt([1,2,3,4,5,6,7], 3))
    print(rotate_another([1,2,3,4,5,6,7], 3))

