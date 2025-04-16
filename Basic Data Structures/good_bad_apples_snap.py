"""
You have a box of mxn grids.
Each grid can have one apple.
Some apples are bad, and some are good.
Bad apples will make the neighboring apple become bad too every hour
Return the minium hours that all apples become bad
"""

from collections import deque


def good_bad_apples(grid):
    """
    O(mn) to traverse the grid 

    Say, bad apples are 1, good apples are 0
    """
    res = 0
    visited = set()
    d = deque()
    fresh_apples, rotten_apples = 0, 0 
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                rotten_apples += 1
                visited.add((r, c))
                d.append((r, c)) # put rotten locations into the deque
            else:
                fresh_apples += 1 

    if fresh_apples == 0: # no need to wait, everything is already bad
        return 0
    
    # process the bad cells in a bfs manner
    while d: 
        bad_apples = len(d)
        for _ in range(bad_apples):
            row, col = d.popleft()
            for row_offset, col_offset in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= row_offset < len(grid) and 0 <= col_offset < len(grid[0]) and (row_offset, col_offset) not in visited:
                    if grid[row_offset][col_offset] == 0: # good one is a neighbor
                        visited.add((row_offset, col_offset)) # we saw it 
                        d.append((row_offset, col_offset)) # add this cell for processing purposes 
                        grid[row_offset][col_offset] = 1 # make this apple rotten 
        res += 1 
    for row in grid:
        if any(i == 1 for i in row):
            return -1
    return res - 1


    