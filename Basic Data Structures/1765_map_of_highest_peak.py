from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
        O(mn), sizes of isWater, to go over
        O(mn), to create height and the BFS queue
        It's a BFS with a twist
        Create height and put -1 everywhere
        Add all water (0) to the queue. These are the starting points 
        for the BFS
        Run the BFS updating the height of each land cell incrementally 
        as the BFS goes wide
        for every cell, the height of its neighbors is set to current_height+1
        if it hasn't been set yet (meaning it's still -1)
        It achieves a state where the difference between adjacent cells is at most 1
        return height
        """
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        d = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    d.append((i, j))

        while d:
            x, y = d.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    d.append((nx, ny))
        return height 