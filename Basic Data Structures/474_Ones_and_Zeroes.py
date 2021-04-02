def findMaxForm(strs, m, n):  # O(mn) both
    """
    We have a limitation on maximum weight of the items that we can carry in a bag, so what is the maximum profit that can be achieved within the weight limit of the bag.
    m, n are the similar to limitations of the bag in the knapsack problem, strings being with items with weight w
    Each cell in DP indicates the number of strings that can be achieved with i zeros and j ones. We iterate with all strings and fill the matrix
    """
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        zeros, ones = s.count("0"), s.count("1")
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(1 + dp[i - zeros][j- ones], dp[i][j])
    return dp[-1][-1]