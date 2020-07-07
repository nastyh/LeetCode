def minCostClimbingStairs(cost):
    dp = [0] * (len(cost))
    dp[0] = cost[0]
    dp[1] = cost[1]
    for s in range(2, len(cost)):
        dp[s] = cost[s] + min(dp[s-2], dp[s-1])
    return min(dp[-1], dp[-2])

if __name__ == '__main__':
    print(minCostClimbingStairs([10, 15, 20]))
    print(minCostClimbingStairs([0,0, 1, 1]))
    print(minCostClimbingStairs([0,0, 0, 1]))
