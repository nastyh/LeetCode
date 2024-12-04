from collections import Counter
def mincostTickets(days, cost):
    last = days[-1]
    dp = [0 for i in range(last + 1)]
    traveldays = Counter(days)   
    for i in range(last + 1):
        if i not in traveldays:
            dp[i] = dp[i-1]
        else:
            one = dp[max(0, i - 1)] + cost[0]
            seven = dp[max(0, i - 7)] + cost[1]
            thirty = dp[max(0, i - 30)] + cost[2]
            dp[i] = min(one, seven, thirty)
    return dp[-1]


def mincostTickets_optimal(days, costs):
    """
    O(n) both
    dp is the length of all the days we need to travel (last value in days) plus one
    each cell shows the smallest cost it takes to travel up to this day 
    for each day we make a decision whether it's better 
    1. pick what we've incurred yesterday and buy a pass for a day
    2. go back seven days and buy a 7-day pass
    3. go back 30 days and buy a 30-day pass
    Max handles cases when we're at index 5 and cannot look 7 or 30 days back 
    Also on the days we don't travel, we don't update anything, thus, we do this None thing
    """
    dp = [None] * (days[-1] + 1)
    dp[0] = 0
    for day in days:
        dp[day] = 0
        for i in range(1, len(dp)):
            if dp[i] == None:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
    return dp[-1]


if __name__ == '__main__':
    print(mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
    print(mincostTickets_alt([1, 4, 6, 7, 8, 20], [2, 7, 15]))
        
