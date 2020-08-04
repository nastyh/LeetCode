def uniquePathsWithObstacles(obstacleGrid):
    obstacleGrid[0][0] ^= 1 # binary XOR
    col, row = len(obstacleGrid[0]), len(obstacleGrid)
    for r in range(1, row):
        if obstacleGrid[r][0] == 1:
            obstacleGrid[r][0] = 0
        else:
            obstacleGrid[r][0] = obstacleGrid[r - 1][0]
    for c in range(1, col):
        if obstacleGrid[0][c] == 1:
            obstacleGrid[0][c] = 0
        else:
            obstacleGrid[0][c] = obstacleGrid[0][c - 1]
    for r in range(1, row):
        for c in range(1, col):
            if obstacleGrid[r][c] == 1:
                obstacleGrid[r][c] = 0
            else:
                obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
    return obstacleGrid[-1][-1]

def uniquePathsWithObstacles_another(obstacleGrid): # with filling out the corner rows/cols first:
	col, row = len(obstacleGrid[0]), len(obstacleGrid)
	if obstacleGrid[0][0] == 1: return 0
	obstacleGrid[0][0] = 1
	for i in range(1, col):
		obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
	for j in range(1, row):
		obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
	for i in range(1, row):
		for j in range(1, col):
			if obstacleGrid[i][j] == 0:
			    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
			else:
			    obstacleGrid[i][j] = 0
	return obstacleGrid[-1][-1]


def uniquePathsWithObstacles_easy(obstacleGrid): # doesn't work with some edge cases
    if obstacleGrid[0][0] == 1: return 0
    dp = [[None for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(1, len(dp[0])):
        if (obstacleGrid[0][i] == 0 and obstacleGrid[0][i - 1] == 0):
            dp[0][i] = 1
        else:
             dp[0][i] = 0
    for j in range(1, len(dp)):
        if (obstacleGrid[j][0] == 0 and obstacleGrid[j - 1][0] == 0):
            dp[j][0] = 1
        else:
            dp[j][0] = 0
        # if obstacleGrid[j - 1][0] == 0:
        #     dp[j][0] = 1
        # else:
        #     dp[j][0] = 0
    for p in range(1, len(obstacleGrid)):
        for q in range(1, len(obstacleGrid[0])):
            dp[p][q] = dp[p - 1][q] + dp[p][q - 1] if obstacleGrid[p][q] == 0 else 0
    return dp[-1][-1]

def test(grid):
    col, row = len(grid[0]), len(grid)
    dp = [[None] * col for i in range(row)]
    for i in range(col):
        if grid[0][i] == 0:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    for j in range(row):
        if grid[j][0] == 0:
            dp[j][0] = 1
        else:
            dp[j][0] = 0
    return dp

if __name__ == '__main__':
    # print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePathsWithObstacles_another([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePathsWithObstacles_easy([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePathsWithObstacles_easy([[1, 0]]))
    print(uniquePathsWithObstacles_easy([[0, 1]]))
    print(uniquePathsWithObstacles_easy([[1]]))
    print(uniquePathsWithObstacles_easy([[0, 0]]))
    # print(test([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
