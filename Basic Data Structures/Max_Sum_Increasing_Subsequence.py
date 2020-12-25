def max_sum_increasing_subsequence(nums):  # O(n^2) and O(n)
    dp = nums[:]  # this is important, need a deep copy
    for r in range(1, len(nums)):
        for l in range(r):
            if nums[r] > nums[l]:
                if dp[r] < dp[l] + nums[r]:
                    dp[r] = dp[l] + nums[r]
    return max(dp)


if __name__ == '__main__':
    print(max_sum_increasing_subsequence([1, 101, 2, 3, 100, 4, 5]))
    print(max_sum_increasing_subsequence([3, 4, 5, 10]))