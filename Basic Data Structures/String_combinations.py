def stringcombinations(s):
    res = []
    l = len(s)
    def _helper(s, curr_res):
        if len(curr_res) == l:
            res.append(curr_res[:])
            return
        # if curr_ix >= len(s):
        #     return
        for i in range(len(s)):
            _helper(s[:i] + s[i + 1:], curr_res + s[i])
    _helper(s, '')
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
            _helper(nums[:i] + nums[i + 1:], curr + nums[i])
    _helper(nums, '')
    return res


if __name__ == '__main__':
    print(stringcombinations('abc'))
    print(permute_another('abc'))