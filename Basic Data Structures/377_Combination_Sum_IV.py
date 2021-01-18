def combinationSum4(nums, target):  # O(TN) and O(T) where T is the target value and N is the length of nums
    # minor optimization
    # nums.sort()
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    for comb_sum in range(target+1):
        for num in nums:
            if comb_sum - num >= 0:
                dp[comb_sum] += dp[comb_sum - num]
            # minor optimization, early stopping.
            # else:
            #    break
    return dp[target]