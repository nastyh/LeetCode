def minCost(costs):
    a, b, c = 0, 0, 0 # red, blue, green
    for i in range(len(costs) - 1, -1, -1):
        # need update a, b and c simultaneously
        a, b, c = costs[i][0] + min(b, c), costs[i][1] + min(a, c), costs[i][2] + min(a, b)
    return  min(a, b, c)


def minCost_dp_working(costs):  # O(n) both 
    """
    for every cell, take the min of two other cells and add to the current cell.
    The result is the min value in hte last row
    """
    if len(costs) == 0: return 0
    if len(costs) == 1: return min(costs[0])
    for ix in range(1, len(costs)):
        costs[ix][0] += min(costs[ix - 1][1], costs[ix - 1][2])
        costs[ix][1] += min(costs[ix - 1][0], costs[ix - 1][2])
        costs[ix][2] += min(costs[ix - 1][0], costs[ix - 1][1])
    return min(costs[len(costs) - 1])


def minCost_no_space(costs): # O(n) and O(1)
    if len(costs) == 0: return 0
    previous_row = costs[-1]
    for n in reversed(range(len(costs) - 1)):
        current_row = copy.deepcopy(costs[n])
        # Total cost of painting nth house red?
        current_row[0] += min(previous_row[1], previous_row[2])
        # Total cost of painting nth house green?
        current_row[1] += min(previous_row[0], previous_row[2])
        # Total cost of painting nth house blue?
        current_row[2] += min(previous_row[0], previous_row[1])
        previous_row = current_row
    return min(previous_row)


if __name__ == '__main__':
    # print(minCost([[17,2,17],[16,16,5],[14,3,19]]))
    # print(minCost([[7, 6, 2]]))

    # print(minCost_dp_working([[3,5,3],[6,17,6],[7,13,18],[9,10,18]]))
