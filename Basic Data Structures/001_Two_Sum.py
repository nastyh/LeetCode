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


if __name__ == '__main__':
    print(twoSum([2,7,11, 15], 9))
    print(twoSum_dict([2,7,11, 15], 9))

