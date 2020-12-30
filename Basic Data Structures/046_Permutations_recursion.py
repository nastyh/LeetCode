def permute(nums):
    def pmt(lst):
        out = []
        if not lst:
            return [lst]
        for i in range(len(lst)):
            a = lst[i:i+1]
            out.extend(a + x for x in pmt(lst[:i] + lst[i + 1:]))
        return out
    return pmt(nums)


def permute_alt(nums):
    # output = []
    # recursively generate all permutations
    def _helper(nums):
        if len(nums) == 1: return [nums]
        # divide
        first, remainder = nums[0], nums[1:]
        permutations = _helper(remainder)
        # conquer
        tmp = []
        for permutation in permutations:
            for i in range(len(permutation) + 1):
                # try to insert 'first' at all possible indexes
                tmp.append(permutation[:i] + [first] + permutation[i:])
        return tmp
    return _helper(nums)


def permute_dfs(nums):
    res = []
    def _helper(res, nums, path):
        if len(nums) <= 1:
            res.append(path + nums)
            return
        for k, v in enumerate(nums):
            _helper(res, nums[:k] + nums[k + 1:], path + [v])
    _helper(res, nums, [])
    return res


def permute_another(nums):  # N! / (N - k)! and O(N!)
    if len(nums) == 0: return None
    if len(nums) == 1: return [nums]
    res = []
    l = len(nums)
    def _helper(nums, curr):
        if len(curr) == l:
            res.append(curr[:])
        # if not nums:
        #     res.append(curr)
        for i in range(len(nums)):
            _helper(nums[:i] + nums[i + 1:], curr + [nums[i]])
    _helper(nums, [])
    return res


if __name__ == '__main__':
    print(permute([1, 2, 3]))
    print(permute_alt([1, 2, 3]))
    print(permute_dfs([1, 2, 3]))
    print(permute_another([1, 2, 3]))
