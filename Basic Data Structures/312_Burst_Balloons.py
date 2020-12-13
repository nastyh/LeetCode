def maxCoins(nums):  # O(n^3) where N^2 b/c of left and right pairs, and takes O(N) to find the value of one of them. Space is O(N^2)
    nums, n = [1] + nums + [1], len(nums) + 2
    dp = [[0] * n for _ in range(n)]
    for right in range(2, n):
        for left in reversed(range(right - 1)):
            dp[left][right] = max(dp[left][i] + nums[left] * nums[i] * nums[right] + dp[i][right] for i in range(left + 1, right))
    return dp[0][-1]

def maxCoins_alt(nums):
    """
    dp[i][j] means the maximum coins we get after we burst all the balloons between i and j in the original array.
    between i and j means not include i and j, which means j-i >= 2 (let gap = j-i >=2)
    DP: dp[i][j] = max(nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])(k in (i,j)]   Note: i<k<j
    """
    nums = [1] + nums + [1]
    dp = [[0]*len(nums) for i in range(len(nums))]
    for gap in range(2, len(nums)):
        for i in range(0,len(nums) - gap):
            j = i + gap
            for k in range(i+1,j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
    return dp[0][-1]
    

def maxCoins_another(nums):
    nums = [1] + nums + [1]
    dp = [[0] * len(nums) for i in range(len(nums))]
    
    for i in range(len(nums) -1, -1, -1):
        for j in range(i + 2,len(nums)):
            for k in range(i + 1,j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
    return dp[0][-1]