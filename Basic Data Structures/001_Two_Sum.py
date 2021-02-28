def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, n in enumerate(nums):
        r = target - n
        if r in nums[i + 1:]:
            j = nums.index(r, i + 1)
            return [i, j]


def twoSum_dict(nums, target):  # O(n) both
    """
    Maintain dictionary: complement: index of the number to which the key is a complement
    """
    d = {}
    for k, v in enumerate(nums):
        if v not in d:
            d[target - v] = k
        else:
            return [d[v], k]
    return []


def twoSum_recur(nums, target):
    def _helper(nums, target, d={}, i=0):
        if i < len(nums):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i
            i += 1
        return _helper(nums, target, d, i)
    return _helper(nums, target, {}, 0)


def twoSum_several(nums, target): # list of lists if more than one combination is available
    d, res = {}, []
    if len(nums) == 0:
        return []
    for i in range(len(nums)):
        curr = []
        if target - nums[i] not in d:
            d[nums[i]] = i
        else:
            curr.append(nums[i])
            curr.append(target - nums[i])
            res.append(curr)
    return res


if __name__ == '__main__':
    # print(twoSum([2,7,11, 15], 9))
    # print(twoSum_dict([2,7,11, 15], 9))
    # print(twoSum_recur([2, 7, 11, 15], 9))
    print(twoSum_several([3, 5, 2, -4, 8, 11], 7))
    print(_helper([0, 1, 2, -1, -4], 1))