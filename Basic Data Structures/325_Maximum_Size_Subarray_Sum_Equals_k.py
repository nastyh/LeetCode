def maxSubArrayLen(nums, k):  # O(n) both 
    if not nums:
        return 0
    curr_max = 0   # current record of max length
    cum_sum = 0    # cumulative sum so far
    idx_dict = {0 : -1} # initialize the dictionary

    for i, num in enumerate(nums):
        cum_sum += num
        diff = cum_sum - k
        if diff in idx_dict:
            curr_max = max(curr_max, i - idx_dict[diff])
        if cum_sum not in idx_dict:
            idx_dict[cum_sum] = i       # only keep the oldest index to have the longest subarray
    return curr_max


def maxSubArrayLen_alt(nums, k):
    """
    Dictionary will contain pairs running sum: end_index
    Start building a running sum. If it becomes k, mark in largest_len
    If it's not k, calculate the diff. If we've seen the difference already, choose 
    the max b/w the current length and the length stored in the dictionary
    Keep building the dict
    """
    seen_sum = {0: 0}
    total_sum, largest_len = 0, 0
    for i in range(len(nums)):
        total_sum += nums[i]
        if total_sum == k:
            largest_len = i + 1
        else: 
            required = total_sum - k
            if required in seen_sum:
                largest_len = max(largest_len, i - seen_sum[required])
        if total_sum not in seen_sum:
            seen_sum[total_sum] = i
    return largest_len


if __name__ == '__main__':
    print(maxSubArrayLen([-1], -1))
    print(maxSubArrayLen_alt([-1], -1))
