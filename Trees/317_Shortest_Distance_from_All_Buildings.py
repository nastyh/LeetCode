from collections import deque
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
     """
     Optimal
     For each building run a BFS that:
     walks only through empty cells (0),
     updates the running total distance dist_sum,
     increments reach for every empty cell reached.
     After processing all buildings, a cell (r,c) is a valid house location iff
     reach[r][c] == num_buildings.
     O(B × m × n), where B is the number of buildings.
     O(m × n) for dist_sum, reach, and the visited matrix used per BFS (re‑initialized each time).
     """
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        dist_sum  = [[0] * n for _ in range(m)]   # cumulative distances
        reach     = [[0] * n for _ in range(m)]   # #buildings that reached this cell
        num_buildings = 0
        
        # Directions: up, down, left, right
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:                       # start BFS from each building
                    num_buildings += 1
                    visited = [[False]*n for _ in range(m)]
                    q = deque([(r, c, 0)])                # (row, col, dist)
                    visited[r][c] = True
                    
                    while q:
                        x, y, d = q.popleft()
                        for dx, dy in DIRS:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n \
                               and not visited[nx][ny] \
                               and grid[nx][ny] == 0:     # only traverse empty land
                                visited[nx][ny] = True
                                dist_sum[nx][ny] += d + 1
                                reach[nx][ny]    += 1
                                q.append((nx, ny, d + 1))
        
        # Search for the empty land reached by **all** buildings
        best = min(
            (dist_sum[r][c]
             for r in range(m)
             for c in range(n)
             if grid[r][c] == 0 and reach[r][c] == num_buildings),
            default=float('inf')
        )
        return -1 if best == float('inf') else best


def shortestDistance(grid):
    ## RC ##
    ## APPROACH : BFS ##
    ## BRUTE FORCE: From each building, we do bfs and to every empty land and mark the distance in distances hashmap, after that we loop through all the empty lands and find the land which is least distant to all the buildings ##
    ## TIME COMPLEXITY : O(number of buildings * matrix) + O(marix * number of buildings) ~ O(2*N*N)
    
    if not grid : return 0
    n = len(grid)
    m = len(grid[0])
    builds = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                builds.append((i, j, 0))
    distances = collections.defaultdict(list)
    for build in builds:
        queue = [build]
        visited = set()
        while( queue ):
            i, j, d = queue.pop(0)
            for x, y in [ (0,1), (0,-1), (-1,0), (1,0) ]:
                if 0 <= i + x < n and 0 <= j + y < m and not (grid[ i+x ][ j+y ] >= 1 ) and (i+x, j+y) not in visited:
                    visited.add((i+x, j+y))
                    distances[(i+x,j+y)].append(d+1)
                    queue.append( (i+x, j+y, d+1) )
    ans = float('inf')
    for d in distances.values():
        if( len(d) == len(builds) ):
            ans = min( ans, sum(d) )
    return -1 if(ans == float('inf')) else ans
