def longestIncreasingPath(matrix):  # O(nlogn)
    if not matrix or not matrix[0]: return 0
    rows = len(matrix)
    cols = len(matrix[0])
    elms = sorted([(matrix[i][j], i, j) for i in range(rows) for j in range(cols)])
    poslen = collections.defaultdict(int)
    neighbors = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    maxlen = 0
    
    for val, i, j in elms:
        clen = max([1] + [poslen[(i+ich, j+jch)]+1 for ich, jch in neighbors if (i+ich, j+jch) in poslen and matrix[i+ich][j+jch] < val])
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