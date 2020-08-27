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

def mincostTickets_alt(days, costs):
    dp_cost = [None] * 366
    dp_cost[0] = 0
    for day in days:
        dp_cost[day] = 0
    for day_i in range(1, 366):
        if dp_cost[day_i] == None:
            dp_cost[day_i] = dp_cost[day_i - 1]      
        else:  
            dp_cost[day_i] = min(dp_cost[day_i - 1]  + costs[0],\
                                 dp_cost[max(day_i - 7, 0)]  + costs[1],\
                                 dp_cost[max(day_i - 30, 0)] + costs[2])
    return dp_cost[-1]
    

if __name__ == '__main__':
    print(mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
    print(mincostTickets_alt([1, 4, 6, 7, 8, 20], [2, 7, 15]))
        