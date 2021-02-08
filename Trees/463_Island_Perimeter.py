from collections import deque
def islandPerimeter(grid):  # O(mn) and O(1)
    """
    BFS 
    For every land cell we count the cells around that are either out of bounds or water
    Mark visited with -1
    """
    res, d = 0, deque()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                d.append((row, col))
                grid[row][col] = -1
                res = 0
                while d:
                    r, c = d.popleft()
                    anti_counter = 0
                    for r_offset, c_offset in [(r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c)]:
                        if 0 <= r_offset < len(grid) and 0 <= c_offset < len(grid[0]) and grid[r_offset][c_offset] == 1:
                            d.append((r_offset, c_offset))
                            grid[r_offset][c_offset] = -1
                        if 0 > r_offset or r_offset >= len(grid) or 0 > c_offset or c_offset >= len(grid[0]) or grid[r_offset][c_offset] == 0:
                            res += 1
    return res


def islandPerimeter_alt(grid):  # O(mn) and O(1)
    """
    Linear approach b/c there is only one island 
    """
    m = len(grid)
    if m == 0:  # if empty grid
        return 0
    n = len(grid[0])
    res = 0    # initial value
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:  # if found "1"
                res += 4
            if i > 0 and grid[i - 1][j] == 1and grid[i][j] == 1:  # if found an top element
                res -= 2
            if j > 0 and grid[i][j - 1] == 1 and grid[i][j] == 1: # if found a left element
                res -= 2
    return res


if __name__ == '__main__':
    # print(islandPerimeter([[0, 1, 0, 0],[1, 1, 1, 0],[0, 1, 0, 0],[1, 1, 0, 0]]))
    # print(islandPerimeter([[1]]))
    # print(islandPerimeter([[1, 0]]))
    print(islandPerimeter_alt([[0, 1, 0, 0],[1, 1, 1, 0],[0, 1, 0, 0],[1, 1, 0, 0]]))
