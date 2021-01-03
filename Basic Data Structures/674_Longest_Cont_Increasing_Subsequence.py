import math
def findLengthOfLCIS(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    if len(set(nums)) == 1:
        return 1
    counter, gl_m = 1, 0
    for n_ix in range(len(nums) - 1):
        if nums[n_ix] < nums[n_ix + 1]:
            counter += 1
            gl_m = max(gl_m, counter)
        else:
            counter = 1
            gl_m = max(gl_m, counter)
    return gl_m


def findLengthOfLCIS_another(nums):  # O(n) and O(1)
    if len(nums) <= 1:
        return len(nums)
    l, r = 0, 1 
    gl_res = -math.inf
    while r < len(nums):
        if nums[r] > nums[r - 1]:
            curr_res = r - l + 1
            gl_res = max(gl_res, curr_res)
        else:
            l = r 
        r += 1 
    return gl_res if gl_res != -math.inf else 1


def findLengthOfLCIS_another_cleaner(nums): # O(n) and O(1)
    """
    as above but with fewer extra variables
    """
    if len(nums) <= 1: return len(nums)
    curr_res, glob_res = 1, 1
    i = 1
    while i < len(nums):
        if nums[i] > nums[i - 1]:
            curr_res += 1
            glob_res = max(glob_res, curr_res)
        else:
            curr_res = 1
        i += 1
    return glob_res


def findLengthOfLCIS_dp(nums):  # O(n) and O(n)
    """
    Cover edge cases
    Create dp with 1s
    If the next element is larger than the previous, increment the respective element in dp
    Return max(dp)
    """
    if len(nums) <= 1: return len(nums)
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


if __name__ == '__main__':
    print(findLengthOfLCIS([1, 3, 5, 4, 7]))
    print(findLengthOfLCIS_another([1, 3, 5, 4, 7]))

