from collections import defaultdict
def containsNearbyDuplicate(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = i
        else:
            idx_diff = abs(i - d[nums[i]])
            if idx_diff <=k:
                return True
            d[nums[i]] = i
    return False


def containsNearbyDuplicate_dict(nums, k):
    d = defaultdict(list)
    if len(nums) <= 1: return False
    if len(set(nums)) == len(nums): return False
    for k, v in enumerate(nums):
        d[v].append(k)
    t = [abs(max(l) - min(l)) for l in d.values()]
    # return t
    return all([i <= k for i in t])
    # if all([i <= k for i in t]):
    #     return True
    # else:
    #     return False 
    # return temp
    # if all( (abs(max(l) - min(l)) <= k for l in d.values() ):
    #     return True
    # return False

def test(nums, k):
    # return True if all(i <= k for i in nums) else False
    return all(i <= k for i in nums)

if __name__ == '__main__':
    print(containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
    print(containsNearbyDuplicate_dict([1,2,3,1,2,3], 2))
    # print(test([3, 3, 3], 2))
