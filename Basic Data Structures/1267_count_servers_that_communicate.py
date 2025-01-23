from collections import deque
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        O(mn) to go over the grid, its sizes
        O(m+n) to save two lists 
        count the number of servers in each row and column of the grid.
        Traverse the grid and check if the server at a specific cell can communicate.
        A server can communicate if either its row count or column count is greater than 1.
        count connected_servers and return 
        """
        rows, cols = len(grid), len(grid[0])
        row_servers = [0] * rows
        col_servers = [0] * cols
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_servers[r] += 1
                    col_servers[c] += 1
        
        connected_servers = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_servers[r] > 1 or col_servers[c] > 1):
                    connected_servers += 1
        return connected_servers
    
    def countServers_bfs(self, grid: List[List[int]]) -> int:
        """
        O(m*n*(m+n)) since for each server, we do a BFS
        O(mn) for visited and the queue
        start BFS from any unvisited server
        traverse servers in the same row and col 
        mark visited servers
        count the num of servers in the connected portion
        if the size of the connected portion > 1, all servers in this portion
        can communicate w/ each other
        sum up all the connected pprtions w/ more than one server 
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def _helper(start_r, start_c):
            d = deque((start_r, start_c))
            visited.add((start_r, start_c))
            count = 0 
            while d:
                r, c = d.popleft()
                d = deque([(start_r, start_c)]) # accurate with the parentheses
                visited.add((start_r, start_c))
                count = 0 
                while d:
                    r, c = d.popleft()
                    count += 1 
                    for next_col in range(cols):
                        if grid[r][next_col] == 1 and (r, next_col) not in visited:
                            visited.add((r, next_col))
                            d.append((r, next_col)) # don't need the [] anymore

                    for next_row in range(rows):
                        if grid[next_row][c] == 1 and (next_row, c) not in visited:
                            visited.add((next_row, c))
                            d.append((next_row, c))
                return count
        connected_servers = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    connected_count = _helper(r, c)
                    if connected_count > 1:
                        connected_servers += connected_count
        return connected_servers
    
    def countServers_bfs_better(self, grid: List[List[int]]) -> int:
        """
         O(mn) to go over the grid, its sizes
         O(num of servers) for the deque 
         It's like the first solution but using the deque 
        """
        rows, cols = len(grid), len(grid[0])
        d = deque()
        row_servers = [0] * rows
        col_servers = [0] * cols
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    d.append((i,j))
                    row_servers[i] += 1
                    col_servers[j] += 1
        while d:
            r, c = d.popleft()
            if row_servers[r] > 1 or col_servers[c] > 1:
                res += 1
        return res