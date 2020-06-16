def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, n in enumerate(nums):
        r = target - n
        if r in nums[i+1:]:
            j = nums.index(r,i+1)
            return [i, j]

def twoSum_dict(nums, target):
    d = {}
    for k, v in enumerate(nums):
        if v not in d:
            d[target - v] = k
        else:
            return [d[v], k]
    return []

def twoSum_recur(nums, target):
    def _helper(nums, target, d = {}, i = 0):
        if i < len(nums):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i
            i += 1
        return _helper(nums, target, d, i)
    return _helper(nums, target, {}, 0)


if __name__ == '__main__':
    # print(twoSum([2,7,11, 15], 9))
    # print(twoSum_dict([2,7,11, 15], 9))
    print(twoSum_recur([2,7,11, 15], 9))

