def maxVacationDays(flights, days):
    """
    O(n^2*k) where n -- num of cities, k is num of weeks
    O(nk) for the dp
    a 2-D dp, in which dp[i][k] represents the maximum number of vacations,
    that can be taken starting from the i-th city in the k-th week.
    This dp is filled in from the  back(in terms of the week number).
    We start from the i-th city in the k-th week and stay in the same city for the (k+1) th week.
    Thus, the factor to be considered for updating the dp[i][k] entry will be given by: days[i][k]+dp[i,k+1].
    We start from the i-th city in the k-th week and move to the j-th city in the (k+1) thweek. But, for changing the city in this manner,
    we need to be able to move from the i-th city to the j-th
    city i.e. flights[i][j] should be 1 for such i and j.
    At the end, we need to find the maximum out of these two factors to update the dp[i][k] value.
    In order to fill the dp values, we start by filling the entries for the last week and proceed backwards.
    At last, the value of dp[0][0] gives the required result.
    
    """
    # build adjacency graph
    g = {row: set([row] + [col for col in range(len(flights[0])) if flights[row][col]]) for row in range(len(flights))}

    dp = [[0] * len(days[0]) for _ in range(len(days))] #dp[i,j] = max vacay days if we're starting at city i, and currently on week j
    rows, cols = len(dp), len(dp[0])
    for col in range(cols-1, -1, -1):
        for row in range(rows):
            curMax = dp[row][col]
            for nbr in g[row]:
                potentialMax = days[nbr][col] # base case is for the last column (i.e. last week). dp[i, -1] = max(days[nbr, -1] for nbr of i)
                if col < cols - 1:
                    potentialMax += dp[nbr][col+1] # inductive case, dp[i,j] = max(dp[nbr, j+1] + days[nbr, j] for nbr of i)
                curMax = max(curMax, potentialMax)
            dp[row][col] = curMax
    return dp[0][0]


if __name__ == '__main__':
    print(maxVacationDays([[0, 1, 1], [1, 0, 1], [1, 1, 0]], [[1, 3, 1], [6, 0, 3], [3, 3, 3]]))
    print(maxVacationDays([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [7, 7, 7], [7, 7, 7]]))
