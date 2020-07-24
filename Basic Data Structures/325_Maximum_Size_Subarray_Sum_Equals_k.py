def maxSubArrayLen(nums, k):
    if not nums:
        return 0
    curr_max = 0   # current record of max length
    cum_sum = 0    # cumulative sum so far
    idx_dict = {0:-1} # initialize the dictionary

    for i,num in enumerate(nums):
        cum_sum += num
        diff = cum_sum - k
        if diff in idx_dict:
            curr_max = max(curr_max, i - idx_dict[diff])
        if cum_sum not in idx_dict:
            idx_dict[cum_sum] = i       # only keep the oldest index to have the longest subarray
    return curr_max
    

def test(nums):
    res = [None] * len(nums)
    res[0] = nums[0]
    for ix in range(1, len(nums)):
        res[ix] = res[ix - 1] + nums[ix]
    return res


def test_same(nums):
    for ix in range(1, len(nums)):
        nums[ix] += nums[ix - 1]
    return nums


if __name__ == '__main__':
    print(maxSubArrayLen([-1], -1))
    print(test([6, 3, -2, 4, -1, 0, -5]))
    print(test_same([6, 3, -2, 4, -1, 0, -5]))
