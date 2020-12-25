def max_sum_increasing_subsequence(nums):  # O(n^2) and O(n)
    """
    Returns the sum of the largest subsequence
    """
    dp = nums[:]  # this is important, need a deep copy
    for r in range(1, len(nums)):
        for l in range(r):
            if nums[r] > nums[l]:
                if dp[r] < dp[l] + nums[r]:
                    dp[r] = dp[l] + nums[r]
    return max(dp)


def return_max_increasing_subsequence(nums):  # O(n^2) and O(n)
    """
    Return the subsequence with the largest sum 
    Indices keep track of where we came from to a given cell given that it is an increasing subsequence
    It's required to rebuild the longest subsequence
    Go to the cell with the index of the largest dp
    Then go to the cell with an index that the cell above has 
    """
    dp = nums[:]  # this is important, need a deep copy
    res = []
    indices = [-1] * len(nums)
    for r in range(1, len(nums)):
        for l in range(r):
            if nums[r] > nums[l]:
                if dp[r] < dp[l] + nums[r]:
                    dp[r] = dp[l] + nums[r]
                    indices[r] = l
    max_ix = dp.index(max(dp))
    res.append(nums[max_ix])
    ix = indices[max_ix]
    while ix >= 0:
        res.append(nums[ix])
        ix = indices[ix]
    return res[::-1]


if __name__ == '__main__':
    # print(max_sum_increasing_subsequence([1, 101, 2, 3, 100, 4, 5]))
    # print(max_sum_increasing_subsequence([3, 4, 5, 10]))
    print(return_max_increasing_subsequence([1, 101, 2, 3, 100, 4, 5]))
    print(return_max_increasing_subsequence([3, 4, 5, 10]))