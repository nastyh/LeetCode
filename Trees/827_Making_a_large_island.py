from collections import defaultdict
def largestIsland(grid):  # O(n^2) both.
# inside dfs, update the area of the current island and
# update the boundary cell to include this island as adjacent
    def _dfs(i, j):
        visited.add((i,j))
        areas[id] += 1
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n:
                if not grid[x][y]:
                    boundaries[(x,y)].add(id)
                elif (x, y) not in visited:
                    _dfs(x, y)

    m, n = len(grid), len(grid[0])
    visited = set()
    boundaries = defaultdict(set)
    id, areas = 0, [0] * (m * n)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in visited:
                _dfs(i, j)
                id += 1

    if max(areas) == m * n:
        return m * n
    res = 0
    for p in boundaries:
        res = max(res, sum(areas[_] for _ in boundaries[p]))
    return res + 1


def largestIsland_another(grid):  # O(n^2) and O(1)
    mark = 2
    islands = []
    n = len(grid)
    
    def mark_it(x, y):  # marks island and returns square of that island
        grid[x][y] = mark
        s = 1
        for xn in (x - 1, x + 1):
            if 0 <= xn < n and grid[xn][y] == 1:
                s += mark_it(xn, y)
        for yn in (y - 1, y + 1):
            if 0 <= yn < n and grid[x][yn] == 1:
                s += mark_it(x, yn)
        return s
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                islands.append(mark_it(i, j))
                mark += 1
    if not islands: return 1
    ret = max(islands)
    
    def check_it(x, y):  # returns sum of adjacent islands to zero cell
        adj = []
        for xn in (x - 1, x + 1):
            if 0 <= xn < n and grid[xn][y] != 0:
                adj.append(grid[xn][y] - 2)
        for yn in (y - 1, y + 1):
            if 0 <= yn < n and grid[x][yn] != 0:
                adj.append(grid[x][yn] - 2)
        if not adj: return 0
        return sum([islands[a] for a in set(adj)])
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                ret = max(ret, 1 + check_it(i, j))
    return ret