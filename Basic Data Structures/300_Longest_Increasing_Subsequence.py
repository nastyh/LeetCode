import bisect
def lengthOfLIS(nums): # O(n^2), DP
    """
    Two pointers: left (i) and right (j). i covers everything up to j.
    Every time, if we see that the number at the j-th index is > number at the i-th index, it means that we can extend our LIS
    We will make a choice between what is already in the dp at the index j vs. taking whatever at index i plus one (because we're extending)
    """
    if len(nums) <= 1: return len(nums)
    i, j, dp, res = 0, 1, [1] * len(nums), 1
    for j in range(1, len(nums)):
        for i in range(j):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], dp[i] + 1)
        # res = max(res, dp[i])
    return max(dp)


def lengthOfLIS_reverse_order(nums):  # O(n^2) and O(n)
    """
    It's a bit easier to do in the reversed order.
    Each number on its own is a subsequence that has a length of 1 (that's why dp is filled w/ ones)
    We start from the second last element and will move to the left.
    For every element we will check if there is a number to the right that is larger than the current number.
    If so, we'll update dp at the respective index by choosing the max between what is already there or adding 1 to dp at the right index
    """
    dp = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)


def lengthOfLIS_log(nums):  # O(nlogn)
    if len(nums) == 0:
        return 0 
    dp = []
    for n in nums:
        pos = bisect.bisect_left(dp, n)
        if pos == len(dp):
            dp.append(n)
        else:
            dp[pos] = n
    return len(dp)


def lengthOfLIS_tail(nums): # O(nlogn)
    """
    tails is an array storing the smallest tail of all increasing subsequences with length i + 1 in tails[i].
    nums = [4,5,6,3], then all the available increasing subsequences are:
    len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
    len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
    len = 3   :      [4, 5, 6]            => tails[2] = 6

    (1) if x is larger than all tails, append it, increase the size by 1
    (2) if tails[i-1] < x <= tails[i], update tails[i]
    """
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size


def lengthOfLIS_log_another(nums):
    if not nums:
        return 0
    def _helper(li, n):
        l = 0
        r = len(li) - 1
        while l < r - 1:
            m = (l + r) // 2
            if li[m] > n:
                r = m
            else:
                l = m
        if li[l] >= n:
            return l
        return r
    dp = [nums[0]]
    for i in range(len(nums)):
        if nums[i] > dp[-1]:
            dp.append(nums[i])
        else:
            ix = _helper(dp, nums[i])
            dp[ix] = nums[i] 
    return len(dp)


if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS([7, 7, 7]))
    print(lengthOfLIS_log([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS_log([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS_log([7, 7, 7]))
    print(lengthOfLIS_log_another([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS_log_another([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS_log_another([7, 7, 7]))