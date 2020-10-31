def maxVacationDays(flights, days):
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