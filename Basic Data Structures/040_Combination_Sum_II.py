def combinationSum2_another(candidates, target):
    res = []
    candidates.sort()
    def _helper(nums, curr_res, curr_ix, left): 
        if left == 0:
            res.append(curr_res)
        if left < 0:
            return
        for i in range(curr_ix, len(nums)):
            if i > curr_ix and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target: return
            _helper(nums, curr_res + [nums[i]], i + 1, left - nums[i])
    _helper(candidates, [], 0, target)
    return res


def combinationSum2_optimal(candidates, target):  # O(2^N)  -- num either included or excluded and O(N)
    """
    Need to sort to handle dups
    Base cases: left is 0. Exact match
    left < 0: took to match, return one level higher
    Then recursion 
    """
    candidates.sort()
    res = []
    def _helper(nums, curr_res, curr_ix, left): 
        if left == 0:
            res.append(curr_res)
        if left < 0:
            return
        for i in range(curr_ix, len(nums)):
            if i > curr_ix and nums[i] == nums[i - 1]:
                continue
            _helper(nums, curr_res + [nums[i]], i + 1, left - nums[i])
    _helper(candidates, [], 0, target)
    return res
    

def combinationSum2_working(candidates, target):
    def backtrack(nums, targetLeft, path):
        if targetLeft == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > targetLeft:
                break
            backtrack(nums[i + 1:], targetLeft - nums[i],path + [nums[i]])    
    res = []
    backtrack(sorted(candidates), target, [])
    return res
    

if __name__ == '__main__':
    print(combinationSum2_another([10, 1, 2, 7, 6, 1, 5], 8))
    print(combinationSum2_optimal([10, 1, 2, 7, 6, 1, 5], 8))
    print(combinationSum2_working([10, 1, 2, 7, 6, 1, 5], 8))
