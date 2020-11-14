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


def uniquePathsWithObstacles_recursion(obstacleGrid):
    """
    brute force, bottom-up recursively with memorization
    - intuitively go through all the path with i+1 OR j+1
    - count the path which reaches to the destination coordinate (m, n)
    - cache the count of the coordinates which we have calculated before
    - if the current grid, grid[i][j], is blocked, tell its parent that this way is blocked by return 0
    - sum up all the coordinates' count

    Time    O(row*col) since we cache the intermediate coordinates, we wont go through the visited coordinates again
    Space   O(row*col) depth of recursions
    """
    def dfs(grid, i, j, m, n, seen):
        key = str(i)+","+str(j)
        if key in seen:
            return seen[key]
        if i == m and j == n:
            if grid[i][j] == 1:
                return 0
            return 1
        elif i > m or j > n:
            return 0
        if grid[i][j] == 1:
            seen[key] = 0
            return 0
        left = dfs(grid, i + 1, j, m, n, seen)
        right = dfs(grid, i, j + 1, m, n, seen)
        seen[key] = left + right
        return left + right
    if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
        return 0
    seen = {}
    return dfs(obstacleGrid, 0, 0, len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1, seen)
    

if __name__ == '__main__':
    # print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePathsWithObstacles_another([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePathsWithObstacles_recursion([[1, 0]]))
    print(uniquePathsWithObstacles_recursion([[0, 1]]))
    print(uniquePathsWithObstacles_recursion([[1]]))
    print(uniquePathsWithObstacles_recursion([[0, 0]]))
    print(uniquePathsWithObstacles_recursion([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    # print(test([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
