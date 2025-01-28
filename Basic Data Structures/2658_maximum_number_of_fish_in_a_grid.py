from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        O(mn) to traverse from every cell
        O(mn) due to visited and the recursion stack

        """
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def _helper(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c>= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            curr_val = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                curr_val += _helper(nr, nc)
            return curr_val 
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0: # fish 
                    visited = set()
                    res = max(res, _helper(r, c))
        return res

    def findMaxFish_no_visited(self, grid: List[List[int]]) -> int:
        """
        O(mn) time is still the same
        O(mn) due to the recursion stack, but otherwise it'd be O(1)
        Slight space improvement: instead of keeping visited,
        we set the visited cell to 0
        """
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def _helper(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c>= len(grid[0]) or grid[r][c] == 0:
                return 0
            curr_val = grid[r][c]
            grid[r][c] = 0 # new line 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                curr_val += _helper(nr, nc)
            return curr_val 
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0: # fish 
                    res = max(res, _helper(r, c))
        return res