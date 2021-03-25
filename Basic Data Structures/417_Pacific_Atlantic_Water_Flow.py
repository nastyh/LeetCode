from collections import deque
def pacific_cells_dfs(matrix):  # O(rc) both
    """
    Start from the respective oceans and collect cells that are reachable from this ocean.
    Result is the overlap of both lists
    """

    def isValid(i, j, rows, cols):
        return 0 <= i < rows and 0 <= j < cols   

    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    pacific, atlantic, ans = set(), set(), []
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    def dfs(matrix, i, j, ocean, prev):
        if not isValid(i, j, rows, cols) or ((i, j) in ocean):
            return
        if prev > matrix[i][j]:
            return
        ocean.add((i, j))
        for x, y in directions:
            dfs(matrix, i + x, j + y, ocean, matrix[i][j])
        
    for k in range(rows):
        dfs(matrix, k, 0, pacific, matrix[k][0])
        dfs(matrix, k, cols - 1, atlantic, matrix[k][cols - 1])
    for k in range(cols):
        dfs(matrix, 0, k, pacific, matrix[0][k])
        dfs(matrix, rows - 1, k, atlantic, matrix[rows - 1][k])
    return list(pacific.intersection(atlantic))


def pacific_cells_bfs(matrix):
    if not matrix:
        return matrix
    m, n = len(matrix), len(matrix[0])
    queue_p = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
    queue_a = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m-1)]
    def helper(queue): 
        queue = deque(queue)
        seen = set(queue)
        while queue: 
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]: 
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and ((nr, nc) not in seen) and (matrix[nr][nc] >= matrix[r][c]): 
                    queue.append((nr, nc))
                    seen.add((nr, nc))
        return seen
    sp = helper(queue_p)
    sa = helper(queue_a)
    res = sp & sa
    res = [list(item) for item in res]
    return res


def pacific_cells_bfs_another(matrix):
    """
    Need to do 2 BFS searches from the cells that are adjacent to both oceans.
    Adjacent to Pacific: first row and first col
    Adjacent to Atlantic: last col and last col
    Helper function tries to collect cells that are reachable from the provided cells.
    Reachability means that the new cell's value >= original cell's value
    Answer is the intersection of both lists (i.e. cells can be reached from both oceans)
    """
    if not matrix: return matrix
    if len(matrix) == 0 and len(matrix[0]) == 0: return [[0, 0]]
    pacific_candidates = [[0, col] for col in range(len(matrix[0]))] + [[row, 0] for row in range(1, len(matrix))]  # first row and first col
    atlantic_candidates = [[len(matrix) - 1, col] for col in range(len(matrix[0]))] + [[row, len(matrix[0]) - 1] for row in range(len(matrix) - 1)]  # last row and last col
    def _helper(matrix, candidate):
        res = []
        d = deque()
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        for element in candidate:
            d.append(element)
            visited[element[0]][element[1]] = True
        while d:
            row, col = d.popleft()
            for r_offset, c_offset in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                if 0 <= row + r_offset < len(matrix) and 0 <= col + c_offset < len(matrix[0]) and not visited[row + r_offset][col + c_offset] and\
                    matrix[row + r_offset][col + c_offset] >= matrix[row][col]:
                    visited[row + r_offset][col + c_offset] = True
                    res.append([row + r_offset, col + c_offset])
                    d.append([row + r_offset, col + c_offset])
        return res
    
    pac = _helper(matrix, pacific_candidates) + pacific_candidates
    atl = _helper(matrix, atlantic_candidates) + atlantic_candidates
    res = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if [row, col] in pac and [row, col] in atl:
                res.append([row, col])
    return res


if __name__ == '__main__':   
    print(pacific_cells_bfs_another([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
    print(pacific_cells_bfs_another([[1, 2],[4, 3]]))
    print(pacific_cells_bfs_another([[]]))
    print(pacific_cells_bfs_another([[8, 12, 0, 17, 8, 7, 7, 1, 12, 19, 12, 19, 14, 1, 16, 0, 14, 7, 4, 14, 14, 8, 17, 18, 9, 14, 19, 16, 19, 17, 7, 14, 13, 17, 2, 11, 16, 8, 8, 8]]))
    