from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        O(mn), sizes
        both 
        normal BFS
        deque has the coordinates and the original cost of 0 
        directions look slightly more complicated than usual
        """
        m, n = len(grid), len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        visited = [[False] * n for _ in range(m)]
        d = deque([(0, 0, 0)])

        while d: 
            x, y, cost = d.popleft()
            if visited[x][y]: # seen this cell 
                continue
            visited[x][y] = True 
            if x == m - 1 and y == n - 1:  # answer 
                return cost 
            for _d, (dx, dy) in directions.items(): # take out key: (value)
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[nx][ny]:
                        if grid[x][y] == _d:  # Current direction matches
                            d.appendleft((nx, ny, cost))
                        else:  # Change direction
                            d.append((nx, ny, cost + 1))
    
    def minCost_set(self, grid: List[List[int]]) -> int:
        """
        Exactly same but using set for visited (as normally)
        """
        m, n = len(grid), len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        visited = set()
        d = deque([(0, 0, 0)])

        while d: 
            x, y, cost = d.popleft()
            if (x,y) in visited:
                continue
            visited.add((x, y))
            if x == m - 1 and y == n - 1:
                return cost 
            for _d, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited:
                        if grid[x][y] == _d:  # Current direction matches
                            d.appendleft((nx, ny, cost))
                        else:  # Change direction
                            d.append((nx, ny, cost + 1))