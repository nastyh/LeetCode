import math
def maxAreaOfIsland(grid):
    if len(grid) == 0: return 0
    glob_res = -math.inf
    def _helper(grid, i, j):
        if i < 0 or j < 0 or i  >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:  # edge case: to avoid falling out of the index range + don't consider zeroes
            return 0
        loc_res = 1
        grid[i][j] = 3  # mark visited. Can mark anyting but 1 
        loc_res += _helper(grid, i - 1, j)
        loc_res += _helper(grid, i + 1, j)
        loc_res += _helper(grid, i, j - 1)
        loc_res += _helper(grid, i, j + 1) 
        return loc_res
    for rows in range(len(grid)):
        for cols in range(len(grid[0])):
            if grid[rows][cols] == 1:
                glob_res = max(glob_res, _helper(grid, rows, cols))
    return glob_res if glob_res != -math.inf else 0
    # return grid

if __name__ == '__main__':
    print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
    print(maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
        