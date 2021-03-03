from collections import defaultdict

NEIGHBOURS = [[-1, 0], [1, 0], [0,-1], [0, 1]]

def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
    def merge(grid_map, grid_height, node1, node2):
        p1 = get_parent(grid_map, node1)
        p2 = get_parent(grid_map, node2)
        if p1 == p2:
            return 0
        
        if grid_height[p1] > grid_height[p2]:
            grid_map[p2] = p1
        else:
            grid_map[p1] = p2
            grid_height[p2] = max(grid_height[p2], grid_height[p1] + 1)
        return -1

    def get_parent(grid_map, key):
        while key != grid_map[key]:
            key = grid_map[key]
        return key

    grid = []
    for i in range(m):
        grid.append([0] * n)
    
    result = []
    grid_map = defaultdict(int)
    grid_height = defaultdict(int)
    island_num = 1
    total = 0

    for r, c in positions:
        if grid[r][c] == 0:
            parent = None
            for i, j in NEIGHBOURS:
                x, y = r + i, c + j
                if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                    if parent is None:
                        parent = grid[x][y]
                        grid[r][c] = parent
                    else:
                        total += merge(grid_map, grid_height, grid[x][y], parent)
            if parent is None:
                grid[r][c] = island_num
                grid_map[island_num] = island_num
                grid_height[island_num] = 0
                island_num += 1
                total += 1
        result.append(total)
    return result


def numIslands2_alt(, m, n, positions):
    dic, res, count = {}, [], 0
    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    def find(self, dic, i):
        if dic[i] >= 0:
            return find(dic, dic[i])
        else:
            return i

    def union(self, dic, a, b):
        rootA, rootB = find(dic, a), find(dic, b)
        if rootA != rootB:
            if dic[rootA] > dic[rootB]:
                rootA, rootB = rootB, rootA
                # union by rank
            dic[rootA] += dic[rootB]
            dic[rootB] = rootA
            count -= 1

    if m == 0 or n == 0 or not positions:
        return []
    for pos in positions:
        x, y = pos[0], pos[1]
        if x * n + y in dic:
            # deal with duplicate operations
            res.append(res[-1])
            continue
        count += 1
        dic[x * n + y] = -1
        for dirc in directions:
            nx, ny = x + dirc[0], y + dirc[1]
            if 0 <= nx < m and 0 <= ny < n and (nx * n + ny) in dic:
                union(dic, x * n + y, nx * n + ny)
        res.append(count)
    return res


