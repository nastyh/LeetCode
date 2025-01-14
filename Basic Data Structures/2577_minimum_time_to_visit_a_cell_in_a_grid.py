import heapq
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        """
        O(m*n*log(mn)): mn cells, log(mn) to add to the heap
        O(mn) for the heap and the visited set 
        when we find ourselves stuck in a cell, unable to move forward because all
        neighboring cells are inaccessible, with higher minimum times.
        In such situations, we must "waste" time to move forward. We can move back and forth between
        the current cell and any previously accessible cells until a neighboring cell becomes accessible.
        It’s important to note that each unit of time wasted takes 2 seconds since we travel
        to a previous cell and return to the current cell. Therefore, if the difference between the current
        time and the target cell's time is odd, we can step into the target cell exactly when it becomes accessible.
        """
        # edge: both initial moves need more than a second
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        # Possible movements: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        # Priority queue stores (time, row, col)
        # Ordered by minimum time to reach each cell
        d = [(grid[0][0], 0, 0)]
        while d:
            time, row, col = heapq.heappop(d)
            if row == rows - 1 and col == cols - 1: # arrived at the end
                return time 
            if (row, col) in visited: 
                continue 
            visited.add((row, col))
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                    """
                    If the difference between the grid value and the current time is even, the additional wait time is 1.
                    Otherwise, the wait time is 0.
                    """
                    wait_time = (
                        1 if (grid[new_row][new_col] - time) % 2 == 0 else 0
                    )
                    """
                    Calculate the next possible time based on the grid value and the wait time,
                    """
                    next_time = max(grid[new_row][new_col] + wait_time, time + 1)
                    heapq.heappush(d, (next_time, new_row, new_col))
        return -1
