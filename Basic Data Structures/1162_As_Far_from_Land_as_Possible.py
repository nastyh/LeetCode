import math
from collections import deque
def maxDistance(grid):
    res = -1
    dp = [[-1] * len(grid[0]) for _ in range(len(grid))]  # not visited are -1
    q = deque()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == True:
                q.append([y, x, 0])
                dp[y][x] = 0
    while q:
        i_step, j_step, step = q.popleft()
        for r, c in [(i_step + 1, j_step), (i_step - 1, j_step), (i_step, j_step - 1), (i_step, j_step + 1)]:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and dp[r][c] < 0:  # check we aren't out of bounds and haven't been to this cell
                if grid[r][c] == 0:
                    dp[r][c] = step + 1
                    res = max(res, step + 1)
                    q.append([r, c, step + 1])
    return res



def maxDistance_alt(grid):
    rows = len(grid)
    if rows == 0:
        return -1
    cols = len(grid[0])
    lands = deque()
    maxDistance = 0
    # Cover up all the lands and say there nearest distance to themselves is = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                lands.append([(i,j), 0])
    while lands:
        for _ in range(len(lands)):
            # Get the node and the distance value corresponding to it
            temp = lands.popleft()
            x,y = temp[0] 
            d = temp[1]
            
            # Keep a global maxDistance check
            maxDistance = max(maxDistance, d)
            
            # Explore everything around the given land mass
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                xx, yy = x + dx, y + dy
                
                # Simple edge cases tested
                if xx < 0 or xx == rows or yy < 0 or yy == cols:
                    continue
                
                # If you find a sea around it
                if grid[xx][yy] == 0:
                
                    # Mutate and append
                    grid[xx][yy] = d + 1
                    lands.append([(xx, yy), d + 1])
    return maxDistance or -1


if __name__ == '__main__':
    print(maxDistance([[1, 0, 1],[0, 0, 0],[1, 0, 1]]))
    print(maxDistance([[1, 0, 0],[0, 0, 0],[0, 0, 0]]))
    print(maxDistance_alt([[1, 0, 1],[0, 0, 0],[1, 0, 1]]))
    print(maxDistance_alt([[1, 0, 0],[0, 0, 0],[0, 0, 0]]))