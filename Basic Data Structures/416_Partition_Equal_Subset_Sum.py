def canPartition(nums):
    if sum(nums) % 2 == 1:
        return False
    cache = set()
    def _helper(target, nums):
        nonlocal cache
        if target < 0:
            return False
        if target == 0:
            return True
        if target in cache:
            return False
        cache.add(target)
        for k, v in enumerate(nums):
            if _helper(target - v, nums[k + 1:]) or _helper(target, nums[k + 1:]):
                return True
        return False
    return _helper(sum(nums) // 2, nums)


if __name__ == '__main__':
    print(canPartition([1, 5, 11, 5]))
    print(canPartition([1, 2, 3, 5]))