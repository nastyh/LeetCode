from collections import deque
def shortestPathBinaryMatrix_inplace(grid):
    """
    O(MN)
    O(1) since we update in place
    visited become -1
    """
    if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
    d = deque()
    d.append((0,0))
    res = 1
    grid[0][0] = - 1
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, 1), (1, 1), (1, 0),
                  (1, -1), (0, -1)]
    while d:
        for _ in range(len(d)):
            r, c = d.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return res
            for r_offset, c_offset in directions:
                if 0 <= r + r_offset < len(grid) and 0 <= c + c_offset < len(grid[0])\
                    and grid[r+r_offset][c+c_offset] ==0:
                        grid[r+r_offset][c+c_offset] = -1  # mark cell as visited
                        d.append((r+r_offset, c+c_offset))
        res += 1
    return -1
def shortestPathBinaryMatrix(grid):  # O(MN) and O(MN)
    """
    Check edge cases
    Start adding zero cells to the deque
    If we arrive to the last cell, return res immediately
    Otherwise, do normal BFS
    increment res outside the for _ in range... loop so that we don't count every good neighbor, but only one
    Check at the end that we arrived to the last cell 
    """
    if grid[0][0] == 1 or grid[-1][-1] == 1:  return -1
    res = 1
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    d = deque()
    d.append((0, 0))
    visited[0][0] = True
    while d:
        for _ in range(len(d)):
            r, c = d.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return res
            for r_offset, c_offset in [(r - 1, c - 1), (r - 1, c),\
                (r - 1, c + 1), (r, c + 1), (r + 1, c + 1), (r + 1, c),\
                    (r + 1, c - 1), (r, c - 1)]:
                    if 0 <= r_offset < len(grid) and 0 <= c_offset < len(grid[0])\
                        and visited[r_offset][c_offset] == False:
                        if grid[r_offset][c_offset] == 0:
                            visited[r_offset][c_offset] = True
                            d.append((r_offset, c_offset))
        res += 1
    if visited[-1][-1] == False:
        return -1
    else:
        return res


def shortestPathBinaryMatrix_optimized(grid): ## O(MN) and O(1)
    if grid[0][0] == 1: return -1
    if grid[-1][-1] == 1: return -1
    d = deque()
    d.append((0, 0, 1))
    grid[0][0] = 2  # marking as visited 
    while d:
        r, c, st = d.popleft()
        if r == len(grid) - 1 and c == len(grid[0]) - 1:  # return condition
            return st
        for row_offset, col_offset in [(r - 1, c - 1), (r + 1, c + 1), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1), (r - 1, c + 1), (r + 1, c - 1)]:
            if 0 <= row_offset < len(grid) and 0 <= col_offset < len(grid[0]) and grid[row_offset][col_offset] == 0:
                grid[row_offset][col_offset] = 2
                d.append((row_offset, col_offset, st + 1))  # add to st here not above: st += 1
    return -1


if __name__ == '__main__':
    # print(shortestPathBinaryMatrix([[0, 1],[1, 0]]))
    # print(shortestPathBinaryMatrix([[0, 0, 0],[1, 1, 0],[1, 1, 0]]))
    # print(shortestPathBinaryMatrix([[0, 0],[0, 0]]))
    # print(shortestPathBinaryMatrix([[0, 0, 1, 0],[1, 0, 1, 0],[1, 1, 0, 1], [0, 0, 0, 0]]))
    print(shortestPathBinaryMatrix([[0,0,0,0,1,1],[0,1,0,0,1,0],[1,1,0,1,0,0],[0,1,0,0,1,1],[0,1,0,0,0,1],[0,0,1,0,0,0]]))
    # print(shortestPathBinaryMatrix_optimized([[0, 1],[1, 0]]))
    # print(shortestPathBinaryMatrix_optimized([[0, 0, 0],[1, 1, 0],[1, 1, 0]]))
    # print(shortestPathBinaryMatrix_optimized([[0, 0],[0, 0]]))
    # print(shortestPathBinaryMatrix_optimized([[0, 0, 1, 0],[1, 0, 1, 0],[1, 1, 0, 1], [0, 0, 0, 0]]))
    # print(shortestPathBinaryMatrix_optimized([[0, 0, 0, 0, 1],[1, 0, 0, 0, 0],[0, 1, 0, 1, 0],[0, 0, 0, 1, 1],[0, 0, 0, 1, 0]]))
    print(shortestPathBinaryMatrix_optimized([[0, 0, 0, 0, 1, 1],[0, 1, 0, 0, 1, 0],[1, 1, 0, 1, 0, 0],[0, 1, 0, 0, 1, 1],[0, 1, 0, 0, 0, 1],[0, 0, 1, 0, 0, 0]]))
