def permuteUnique(nums):
    if len(nums) == 0: return None
    if len(nums) == 1: return [nums]
    nums.sort()
    res = []
    l = len(nums)
    def _helper(nums, curr):
        if len(curr) == l:
            res.append(curr[:])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            _helper(nums[:i] + nums[i + 1:], curr + [nums[i]])
    _helper(nums, [])
    return res



if __name__ == '__main__':
    print(permuteUnique([1, 1, 2]))