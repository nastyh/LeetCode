from collections import defaultdict
import math
def containsNearbyDuplicate(nums, k):  # update a dictionary once you see a dup and make a decision
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


def containsNearbyDuplicate_default(nums, k):
    """
    create a defaultdict with keys as numbers and values as list of indices
    Indices is a list of lists with values from defaultdict for repeating elements
    Then we check whether the differences in all elements are <= k
    """
    if len(nums) <= 1: return False 
    if len(set(nums)) == len(nums): return False  # no dups
    d = defaultdict(list)
    for ix, v in enumerate(nums):
        d[v].append(ix)
    indices = [v for v in d.values() if len(v) > 1]
    for ind in indices:
        return True if any(abs(ind[i] - ind[i + 1]) <= k for i in range(len(ind) - 1)) else False


def containsNearbyDuplicate_set(nums, k):
    """
    Exotic solution.
    Add elements to the set
    If you see a duplicate, check whether the difference between the current index and nums.index(nums[i]), which is always the first occurance of the element, is
    <= k. If it's so, return True. Otherwise, substitute that element that occured first with -math.inf, so that you don't consider this element in the future
    """
    s = set()
    for i in range(len(nums)):
        if nums[i] not in s:
            s.add(nums[i])
        else:
            if abs(i - nums.index(nums[i])) <= k:
                return True
            nums[nums.index(nums[i])] = -math.inf
    return False


if __name__ == '__main__':
    print(containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
    print(containsNearbyDuplicate_dict([1, 2, 3, 1, 2, 3], 2))
    print(containsNearbyDuplicate_default([1, 2, 3, 1], 3))
