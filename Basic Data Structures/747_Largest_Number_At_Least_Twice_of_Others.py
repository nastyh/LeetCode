import math
def dominantIndex(nums):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0
    largest_ix = nums.index(max(nums))
    for n in nums[:largest_ix] + nums[largest_ix + 1:]:
        if nums[largest_ix] < 2 * n:
            return -1
    return largest_ix


def dominantIndex_1pass(nums): # doesn't work well with zeroes based on Leetcode's test cases but is right conceptually
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0
    m_ix, glob_max = -1, -math.inf
    for i in range(len(nums)):
        if nums[i] > glob_max:
            if nums[i] >= 2 * glob_max:
                m_ix = i
                glob_max = nums[i]
            else:
                m_ix = -1
                glob_max = nums[i]
    return m_ix

if __name__ == '__main__':
    print(dominantIndex([3, 6, 1, 0]))
    print(dominantIndex([1, 2, 3, 4]))
    print(dominantIndex_1pass([3, 6, 1, 0]))
    print(dominantIndex_1pass([1, 2, 3, 4]))
