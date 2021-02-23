import math
from collections import deque
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


def maxAreaOfIsland_alt(grid):  # O(mn) both
    """
    Usual BFS
    Go element by element, once you see a 1, add to the deque
    Edge case is that we need to immediately update glob_res for situations like [[1]] when we never enter the big if statement w/ offset
    Then do normal stuff and update glob_res every time when there is a good neighbor
    """
    if len(grid) == 0: return 0
    d = deque()
    glob_res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                res = 1
                glob_res = max(glob_res, res)
                d.append((row, col))
                grid[row][col] = 2
                while d:
                    r, c = d.popleft()
                    for row_offset, col_offset in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= row_offset < len(grid) and 0 <= col_offset < len(grid[0]) and grid[row_offset][col_offset] == 1:
                            res += 1
                            grid[row_offset][col_offset] = 2
                            glob_res = max(glob_res, res)
                            d.append((row_offset, col_offset))
    return glob_res
              


if __name__ == '__main__':
    print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],\
        [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],\
            [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0],\
                [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
    print(maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
    print(maxAreaOfIsland_alt([[0, 0, 0, 0, 0, 0, 0, 0]]))
    print(maxAreaOfIsland_alt([[1,1,0,0,0],[1, 1, 0, 0, 0],[0, 0, 0, 1, 1],[0, 0, 0, 1, 1]]))
    print(maxAreaOfIsland_alt([[0,0,1,0,0,0,0,1,0,0,0,0,0],\
        [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],\
            [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0],\
                [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(maxAreaOfIsland_alt([[1]]))
        