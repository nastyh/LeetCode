from collections import deque, defaultdict
def longestIncreasingPath_optimal(matrix):  # O(mn) both
    """
    DFS approach with memoization
    For each cell, we need to calculate the largest path that can be built from THIS cell. The number is saved in dp
    _helper() does DFS. Need to pass old and new coordinates 
    """
    if not matrix or not matrix[0]: return 0
    res = 0
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    def _helper(matrix, row, col, i, j):
        if dp[i][j] > 0:  # allows to avoid recalculations 
            return dp[i][j]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        max_res = 0
        for direction in directions:
            row_offset = i + direction[0]
            col_offset = j + direction[1]
            if 0 <= row_offset < len(matrix) and 0 <= col_offset < len(matrix[0]) and matrix[row_offset][col_offset] > matrix[i][j]:
                max_res = max(max_res, _helper(matrix, len(matrix), len(matrix[0]), row_offset, col_offset)) 
        dp[i][j] = max_res + 1
        return max_res + 1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            curr_res = _helper(matrix, len(matrix), len(matrix[0]), row, col)
            res = max(res, curr_res)
    return res


def longestIncreasingPath(matrix):  # O(nlogn)
    if not matrix or not matrix[0]: return 0
    rows = len(matrix)
    cols = len(matrix[0])
    elms = sorted([(matrix[i][j], i, j) for i in range(rows) for j in range(cols)])
    poslen = defaultdict(int)
    neighbors = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    maxlen = 0
    
    for val, i, j in elms:
        clen = max([1] + [poslen[(i + ich, j + jch)] + 1 for ich, jch in neighbors if (i + ich, j + jch) in poslen and matrix[i + ich][j + jch] < val])
        poslen[(i, j)] = clen
        maxlen = max(clen, maxlen)
    return maxlen
    

def longestIncreasingPath_alt(matrix):
    if not matrix or not matrix[0]: return 0
    rows = len(matrix)
    cols = len(matrix[0])
    dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    @lru_cache(None)
    def get_maxlen(i, j):
        return max([1] + [get_maxlen(i + x, j + y)+1 for x, y in dirs \
                            if rows > i+x >= 0 <= j + y < cols and matrix[i + x][j + y] < matrix[i][j]])
    return max([get_maxlen(i, j) for i in range(rows) for j in range(cols)])


def longestIncreasingPath_topological(matrix):  # O(MN) both 
    if not matrix or not matrix[0]:
        return 0
    DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
    row, col = len(matrix), len(matrix[0])
    indegree = [[0 for _ in range(col)] for _ in range(row)]

    def neighbors(r, c):
        for d in DIRECTIONS:
            nr, nc = r + d[0], c + d[1]           
            if not (0 <= nr < row and 0 <= nc < col):
                continue
            yield nr, nc
    
    for r in range(row):
        for c in range(col):
            for nr, nc in neighbors(r, c):
                if matrix[nr][nc] > matrix[r][c]:
                    indegree[nr][nc] += 1
    q = deque()
    for r in range(row):
        for c in range(col):
            if indegree[r][c] == 0:
                q.append((r, c))      
    lip = 0
    while q:
        q_len = len(q)
        lip += 1
        for _ in range(q_len):
            r, c = q.popleft()
            for nr, nc in neighbors(r, c):
                if matrix[nr][nc] > matrix[r][c]:
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        q.append((nr, nc))        
    return lip
    

if __name__ == '__main__':
    print(longestIncreasingPath_optimal([[9, 9, 4],[6, 6, 8],[2, 1, 1]]))