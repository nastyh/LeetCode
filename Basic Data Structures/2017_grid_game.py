from collections import deque
import copy
import math
from typing import List


class Solution:
    def gridGame_prefix_sum(self, grid: List[List[int]]) -> int:
        """
        O(n) to iterate through each col once
        O(1) don't store anything extra
        
        For any col i, robot1 can do
        right portion (top row): points left in cols i+1 to n-1 (top_sum - grid[0][i])
        left portion (bottom row): points collecte from col 0 to i-1 (bottom_sum)
        Robot 1 tries to minimize Robot 2’s score by choosing the column i 
        where the maximum of these two portions is smallest.
        track the minimum score Robot 2 can achieve across all splits.
        """
        n = len(grid[0])
        top_sum = sum(grid[0])  # Total points in the top row (from the curr col)
        bottom_sum = 0  # nothing is collected from the second row (keeps track of already collected in the bottom row)
        res = math.inf
        for i in range(n):
            """
            robot2 potentially can
            top row: points to the right of col i (inclusive)
            bottom row: points to the left of col i (exclusive)
            """
            points_top = top_sum - grid[0][i]
            points_bottom = bottom_sum
            # switching from one row to another at col i: maximize what Robot2 can collect
            max_points_robot2 = max(points_top, points_bottom)
            # minimize the max num of points robot2 can collect per question
            res = min(res, max_points_robot2)
            # update the cumulative sums
            top_sum -= grid[0][i]
            bottom_sum += grid[1][i]
        return res


    def gridGame_bfs(self, grid: List[List[int]]) -> int:
        """
        O(2^n*m*n), since 2^n to explore all possible paths 
        and then O(mn), where m = 2 for robot2 to explore via bfs
        O(mn) for deques and copies 
        not very efficient since it explores all the cells 
        times out for some cases
        """
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0)]
        d = deque([(0, 0, set([(0, 0)]), 0)]) # x, y, path, collected points
        min_points_robot2 = math.inf

        def _helper(grid, start):
            """
            helper to look around and choice the optimal cell
            to go to next
            """
            rows, cols = len(grid), len(grid[0])
            directions = [(0, 1), (1, 0)]
            q = deque([(start[0], start[1], 0)])  # (row, col, points_collected)
            max_points = 0

            while q:
                r, c, points = q.popleft()
                max_points = max(max_points, points)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        q.append((nr, nc, points + grid[nr][nc]))
            return max_points
        
        while d:
            r, c, path, points = d.popleft()
            if (r,c) == (1, m - 1):
                new_grid = copy.deepcopy(grid)
                for pr, pc in path:
                    new_grid[pr][pc] = 0

                points_robot2 = _helper(new_grid, (0, 0))
                min_points_robot2 = min(min_points_robot2, points_robot2)
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in path:
                    """
                    path | {(nr, nc)} 
                    creates a new set that includes all the previous cells in path plus the new cell (nr, nc)
                    | is a union operator
                    """
                    d.append((nr, nc, path | {(nr, nc)}, points + grid[nr][nc]))
        return min_points_robot2
        

