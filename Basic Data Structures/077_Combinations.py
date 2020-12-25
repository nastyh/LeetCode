def combine(n, k):  # O(k*CkchooseN) and O(CkchooseN)
    nums = [i for i in range(1, n + 1)]
    res = []
    def _helper(nums, curr_ix, curr_res):
        if len(curr_res) == k:
            res.append(curr_res)
        for i in range(curr_ix, len(nums)):
            # curr_res.append(nums[i])
            _helper(nums, i + 1, curr_res + [nums[i]])
    _helper(nums, 0, [])
    return res


def combine_alt(n, k):
    result = []
    nums = [i for i in range(1,n + 1)]
    def backtrack(start, end, tmp):
        if len(tmp) == k:
            result.append(tmp[:])
        else:
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i + 1, end, tmp)
                tmp.pop()
    backtrack(0, n, [])
    return result


if __name__ == '__main__':
    print(combine(4, 2))
    print(combine_alt(4, 2))