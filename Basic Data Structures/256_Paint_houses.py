def minCost(self, costs):
    a, b, c = 0, 0, 0 # red, blue, green
    for i in range(len(costs) - 1, -1, -1):
        # need update a, b and c simultaneously
        a, b, c = costs[i][0] + min(b, c), costs[i][1] + min(a, c), costs[i][2] + min(a, b)

    return  min(a, b, c)
