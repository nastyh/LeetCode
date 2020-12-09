def combinationSum3(k, n):
    nums = [i for i in range(1, 10)]
    res = []
    def _helper(nums, k, n, curr, ix):
        if n < 0 or len(curr) > k: return
        if n == 0 and len(curr) == k:  # need this: sum is equal to the target and curr is of the required length
            res.append(curr)
        for i in range(ix, len(nums)):
            _helper(nums, k, n - nums[i], curr + [nums[i]], i + 1)
    _helper(nums, k, n, [], 0)
    return res


def combinationSum3_backtrack(k, n):
    res = []
    def _helper(i, curr, k, n):
        if len(curr) == k and n == 0:
            res.append(curr[:])
        for i in range(i, 10):
            n -= i
            curr.append(i)
            _helper(i + 1, curr, k, n)
            curr.pop()
            n += i
    _helper(1, [], k, n)
    return res


if __name__ == '__main__': 
    print(combinationSum3(3, 7))
    print(combinationSum3_backtrack(3, 7))