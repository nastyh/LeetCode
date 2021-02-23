from collections import deque
def numIslands(grid):
    ## RC ##
    ## APPROACH : DFS ##
    # 1. find the land, go to surroundings and convert to water
    # 2. increment island count, get back and search for next islands.
    
	## TIME COMPLEXITY : O(N^2) ##
	## SPACE COMPLEXITY : O(1) ##

    def convertLandToWater(grid, i, j):
        if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1'):
            return
        grid[i][j] = '0'
        for x,y in directions:
            convertLandToWater(grid, i + x, j + y)
    if len(grid) == 0 : return 0
    isLandCount = 0
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                isLandCount += 1
                convertLandToWater(grid, i, j)
    return isLandCount

def numIslands_optimal_bfs(grid):  # O(MN) and O(1)
    """
    Explore in a DFS manner as always. The key here is to increment res
    when the deque becomes empty. Means no more land within the reach.
    Then the main double for loop continues by finding the next land (if any)
    """
    res, d = 0, deque()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                d.append((row, col))
                grid[row][col] = '-1'
                while d:
                    r, c = d.popleft()
                    for row_offset, col_offset in [(r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c)]:
                        if 0 <= row_offset < len(grid) and 0 <= col_offset < len(grid[0]) and grid[row_offset][col_offset] == '1':
                            d.append((row_offset, col_offset))
                            grid[row_offset][col_offset] = '-1'
                res += 1
    return res
        


def numIslands_easy(grid):   # O(MN) both; DFS
    if len(grid) == 0: return 0
    res = 0
    def _helper(grid, i, j):
        if i < 0 or j < 0 or i  >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':  # edge case: to avoid falling out of the index range + don't consider zeroes
            return
        grid[i][j] = '3'  # mark visited. Can mark anyting but 1 
        _helper(grid, i - 1, j)
        _helper(grid, i + 1, j)
        _helper(grid, i, j - 1)
        _helper(grid, i, j + 1)
    for rows in range(len(grid)):
        for cols in range(len(grid[0])):
            if grid[rows][cols] == '1':
                _helper(grid, rows, cols)
                res += 1
    return res


def numIslands_bfs_alt(grid):  # O(MN) and O(min(M,N))
    if not grid: return 0
    q = deque()
    m, n = len(grid), len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                q.append((i, j))
                grid[i][j] = '2'
                while q:
                    x, y = q.popleft()
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        xx, yy = x + dx, y + dy
                        if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                            q.append((xx, yy))
                            grid[xx][yy] = '2'
                ans += 1            
    return ans


if __name__ == '__main__':
    # print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    # print(numIslands_easy([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  
    print(numIslands_bfs_alt([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))      
    print(numIslands_bfs_alt([["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]))