import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        O(mn*log(mn)) -- all cells to the heap
        O(mn) for visited 
        min-heap to keep track of the boundary cells while processin the inner
        cells that can potentially trap water
        boundary of the matrix is a wall
        visited so don't go in circles
        pop the smallest height from the heap, check its neighbors,
        and calculate trapped water if the neighbor's height is less than the current boundary height
        Add the neighbor to the heap and update the new boundary height for the neighbor if needed
        """
        if not heightMap or not heightMap[0]:  # edge case 
            return 0
    
        m, n = len(heightMap), len(heightMap[0])
        visited = set()
        res = 0
        h = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1: 
                    # start with the  first and last cells 
                    # guarantees we process the smallest boundary first 
                    heapq.heappush(h, (heightMap[i][j], i, j)) # height, coordinates
                    visited.add((i, j))
        while h:
            height, x, y = heapq.heappop(h)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    res += max(0, height - heightMap[nx][ny])
                    heapq.heappush(h, (max(height, heightMap[nx][ny]), nx, ny))
                    visited.add((nx, ny))
        return res

