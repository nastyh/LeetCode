def minPathSum(grid):
    dp = grid
    col, row = len(grid[0]), len(grid)
    for i in range(1, col):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
    for j in range(1, row):
        dp[j][0] = dp[j - 1][0] + grid[j][0]
    for y in range(1, row):
        for x in range(1, col):
            dp[y][x] = min(dp[y][x - 1], dp[y - 1][x]) + grid[y][x]
    return dp[-1][-1]


def minPathSum_alt(grid):
    """
    Very similar but just creating a new dp instead of overwriting the existing list of lists
    """
        dp = [[None for i in range(len(grid[0]))] for j in range(len(grid))]  # the only difference is how I build dp
        dp[0][0] = grid[0][0]
        col, row = len(grid[0]), len(grid)
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for j in range(1, row):
            dp[j][0] = dp[j - 1][0] + grid[j][0]
        for y in range(1, row):
            for x in range(1, col):
                dp[y][x] = min(dp[y][x - 1], dp[y - 1][x]) + grid[y][x]
        return dp[-1][-1]


if __name__ == '__main__':
    print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(minPathSum([[1, 2, 5], [3, 2, 1]]))
    print(minPathSum_alt([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(minPathSum_alt([[1, 2, 5], [3, 2, 1]]))
