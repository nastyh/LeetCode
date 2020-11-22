def combine(n, k):  # DOESN"T WORK, CREATES DUPLICATES FOR SOME REASON
    res = []
    nums = [num for num in range(1, n + 1)]
    def _helper(curr_res, curr_ix):
        if len(curr_res) == k:
            res.append(curr_res[:])
        for i in range(curr_ix, len(nums)):
            curr_res.append(nums[i])
            _helper(curr_res, curr_ix + 1)
            curr_res.pop()
    _helper([], 0)
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