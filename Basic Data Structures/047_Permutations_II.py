from collections import Counter
def permuteUnique(nums):  # O(nPk), n choose k and O(N) from the recursion stack, and a candidate for exploration
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


def permuteUnique_dict(nums):  # O(nPk), n choose k and O(N) from the dict, the recursion stack, and a candidate for exploration
    if len(nums) == 0: return None
    d = Counter(nums)
    res = []
    def _helper(nums, curr_res, d):
        if len(curr_res) == len(nums):
            res.append(curr_res[:])
            return
        for k in d:
            if d[k] > 0:
                curr_res.append(k)
                d[k] -= 1
                _helper(nums, curr_res, d)
                curr_res.pop()
                d[k] += 1
    _helper(nums, [], d)
    return res



if __name__ == '__main__':
    print(permuteUnique([1, 1, 2]))
    print(permuteUnique_dict([1, 1, 2]))