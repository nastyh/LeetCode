"""
Given a sequence of positive integers nums and an integer k, return whether there is a continuous sequence of nums that sums up to exactly t.
"""
def subarray_sum(nums, t):
    s = set()
    running_sum = 0
    for i in range(len(nums)):
        running_sum += nums[i]
        if running_sum == t:
            return True
        if running_sum - t in s:
            return True
        else:
            s.add(running_sum)
    return False


if __name__ == '__main__':
    print(subarray_sum([23, 5, 4, 7, 2, 11], 20))
    print(subarray_sum([1, 3, 5, 23, 2], 7))
    print(subarray_sum([1, 3, 5, 23, 2], 8))