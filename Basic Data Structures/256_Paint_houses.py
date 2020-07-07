def minCost(costs):
    a, b, c = 0, 0, 0 # red, blue, green
    for i in range(len(costs) - 1, -1, -1):
        # need update a, b and c simultaneously
        a, b, c = costs[i][0] + min(b, c), costs[i][1] + min(a, c), costs[i][2] + min(a, b)

    return  min(a, b, c)

def minCost_dp(costs): # doesn't pass some edge cases

    def _helper(l): # returns the value of the second largest element in the list
        return sorted(l)[-2]

    if len(costs) == 0: return 0
    if len(costs) == 1: return min(costs[0])
    dp = []
    for i in range(len(costs)):
        dp.append([])
    dp[0].append(min(costs[0]))
    dp[0].append(costs[0].index(min(costs[0])))

    for ix in range(1, len(costs)):
        if costs[ix].index(min(costs[ix])) != dp[ix - 1][1]:
            dp[ix].append(min(costs[ix]))
            dp[ix].append(costs[ix].index(min(costs[ix])))
        else:
            dp[ix].append(_helper(costs[ix]))
            dp[ix].append(costs[ix].index(_helper(costs[ix])))
    return dp
    # return sum([i[0] for i in dp])

def minCost_dp_working(costs):
    if len(costs) == 0: return 0
    if len(costs) == 1: return min(costs[0])
    for ix in range(1, len(costs)):
        costs[ix][0] += min(costs[ix - 1][1], costs[ix - 1][2])
        costs[ix][1] += min(costs[ix - 1][0], costs[ix - 1][2])
        costs[ix][2] += min(costs[ix - 1][0], costs[ix - 1][1])

    return min(costs[len(costs) - 1])

def test(nums):
    return sorted(nums)[-2]



if __name__ == '__main__':
    # print(minCost_dp([[17,2,17],[16,16,5],[14,3,19]]))
    # print(minCost_dp([[7, 6, 2]]))
    print(minCost_dp([[3,5,3],[6,17,6],[7,13,18],[9,10,18]]))
    # print(minCost_dp_working([[3,5,3],[6,17,6],[7,13,18],[9,10,18]]))
    print(test([6, 17, 6]))
