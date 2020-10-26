def subsetsWithDup(nums):
    result = []
    nums.sort()
    def _helper(nums, start_index, subset):
        result.append(subset[:])
        for i in range(start_index, len(nums)):
            if i != start_index and nums[i] == nums[i - 1]: continue
            subset.append(nums[i])
            _helper(nums, i + 1, subset)
            subset.pop()
    _helper(nums, 0, [])
    return result


if __name__ == '__main__':
    print(subsetsWithDup([1, 2, 2]))