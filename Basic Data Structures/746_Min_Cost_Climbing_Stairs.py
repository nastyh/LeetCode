def minCostClimbingStairs(cost):
    dp = [0] * (len(cost))
    dp[0] = cost[0]
    dp[1] = cost[1]
    for s in range(2, len(cost)):
        dp[s] = cost[s] + min(dp[s-2], dp[s-1])
    return min(dp[-1], dp[-2])


def minCostClimbingStairs_path(prices):
    res = []
    p = [None] * (len(prices) + 1)
    dp = [0] * (len(prices) + 1)
    dp[0] = 0
    dp[1] = prices[0]
    for i in range(2, len(prices) + 1):
        dp[i] = min(dp[i - 2], dp[i - 1]) + prices[i - 1]
        if dp[i - 1] < dp[i - 2]:
            p[i] = i - 1
        else:
            p[i] = i - 2
    curr = len(prices)
    while curr > 0:
 	    curr = p[curr]
 	    if curr == 0:
 	    	break
 	    res.append(curr)
    return res[::-1]


if __name__ == '__main__':
    # print(minCostClimbingStairs([10, 15, 20]))
    # print(minCostClimbingStairs([0,0, 1, 1]))
    # print(minCostClimbingStairs([0,0, 0, 1]))
    print(minCostClimbingStairs_path([3, 2, 4, 6, 1, 1, 5, 3]))
