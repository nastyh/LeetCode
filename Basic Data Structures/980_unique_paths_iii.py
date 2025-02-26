from collections import deque
from typing import List


class Solution:
    def uniquePathsIII_dfs(self, grid: List[List[int]]) -> int:
        """
        O(3^(mn)) worst
        O(mn) due to the recursion stack
        iterate over the grid to count the number of non-obstacle cells (including the start and end) and to locate the starting cell (marked as 1).
        helper function dfs takes the current position (x, y) and the count of cells visited so far. If we reach the ending square (2)
        and the count matches the total number of non-obstacle cells, we increment our valid path count.
        To avoid revisiting cells, we temporarily mark the current cell as an obstacle (i.e. set it to -1)
        before exploring further and then restore it (backtracking) after exploring all directions.
        self.paths holds the total number of unique paths that meet the conditions.
        """
        m, n = len(grid), len(grid[0])
        non_obstacles = 0
        start_x = start_y = 0
        
        # Count all non-obstacle cells and locate the starting square.
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    non_obstacles += 1
                if grid[i][j] == 1:
                    start_x, start_y = i, j

        self.paths = 0
        
        def dfs(x, y, count):
            # If we reach the ending square and have covered all non-obstacle cells
            if grid[x][y] == 2 and count == non_obstacles:
                self.paths += 1
                return
            
            # Mark the current cell as visited by setting it to -1 (obstacle)
            temp = grid[x][y]
            grid[x][y] = -1
            
            # Explore all 4 directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    dfs(nx, ny, count + 1)
            
            # Backtrack: unmark the current cell
            grid[x][y] = temp
        
        dfs(start_x, start_y, 1)
        return self.paths

    def uniquePathsIII_bfs(self, grid: List[List[int]]) -> int:
        """
        O(mn*2^(mn)) check for each state at most 4 directions 
         O(mn*2^(mn)) due to the queue
        We iterate through the grid to count the total number of non-obstacle cells and to identify the starting square (value 1).
        Each cell is encoded as a unique bit (using the function idx(i, j)) so that we can use a bitmask to track which cells have been visited.
        The initial bitmask is set for the starting cell.

        We initialize a BFS queue where each state is a tuple containing the current coordinates, the visited bitmask, and the number of steps
        (cells visited so far).

        For each state, if the current cell is the ending square (value 2) and the number of steps equals the total number
        of non-obstacle cells, we count it as a valid path.
        Otherwise, we check each of the 4 neighbors. If a neighbor is within bounds, not an obstacle,
        and not yet visited (as per the bitmask), we add the new state to the queue.

        The variable count_paths accumulates the number of valid paths that cover all non-obstacle cells exactly once.
        """
        m, n = len(grid), len(grid[0])
        non_obstacles = 0
        start_x = start_y = 0
        
        # Preprocess the grid: count non-obstacle cells and locate the start.
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    non_obstacles += 1
                if grid[i][j] == 1:
                    start_x, start_y = i, j
        
        # A helper to encode cell coordinates into a unique bit position.
        def idx(i, j):
            """
            computes a unique index for each cell in the grid (i*n+j)
            converts the 2D coordinates into a single integer position.
            """
            return i * n + j
        
        # Set up the initial state.
        start_mask = 1 << idx(start_x, start_y) # operator shifts the number 1 to the left by the number of positions equal to the index of the starting cell.
        queue = deque()
        # Each state: (x, y, visited_mask, steps_taken)
        queue.append((start_x, start_y, start_mask, 1))
        count_paths = 0
        
        while queue:
            x, y, mask, steps = queue.popleft()
            
            # If we reach the ending square and have visited all non-obstacle cells
            if grid[x][y] == 2 and steps == non_obstacles:
                count_paths += 1
                continue
            
            # Explore the 4 directional neighbors.
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    bit = 1 << idx(nx, ny)
                    # Skip if this cell is already visited in the current path.
                    if mask & bit:
                        continue
                    new_mask = mask | bit
                    queue.append((nx, ny, new_mask, steps + 1))
                    
        return count_paths