from collections import defaultdict, deque
def longestIncreasingPath(matrix):  # O(mn) both
    """
    DFS approach 
    """
    def dfs(visited, matrix, row, col, dp):
        new_row_arr = [1, -1, 0, 0]
        new_col_arr = [0, 0, 1, -1]
        if visited[row][col] == True:
            return dp[row][col]
        visited[row][col] = True
        for i in range(len(new_row_arr)):
            new_row = row + new_row_arr[i]
            new_col = col + new_col_arr[i]
            if new_row >= 0 and new_row < len(matrix) and new_col >= 0 and new_col < len(matrix[0]) and matrix[row][col] < matrix[new_row][new_col]:
                dp[row][col] = max(dfs(visited, matrix, new_row, new_col, dp) + 1, dp[row][col])
        return dp[row][col] 

    row = len(matrix)
    col = len(matrix[0])
    visited = [[False for i in range(col)] for j in range(row)]
    dp = [[1 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            if visited[i][j] != True:
                dfs(visited, matrix, i, j, dp)
    max_value = 1
    for i in range(row):
        for j in range(col):
            if max_value < dp[i][j]:
                max_value = dp[i][j]
    # print(dp)
    return max_value


def longestIncreasingPath_topological(matrix): # O(mn) both
    m,n = len(matrix), len(matrix[0])
    out_degrees = defaultdict(list)
    in_degrees  = defaultdict(int)
    # gets all neighbors that are in bound
    def get_neighbors(i, j):
        for new_i, new_j in [(i + 1,j),(i - 1,j),(i,j + 1),(i,j - 1)]:
            if 0 <= new_i < m and 0 <= new_j < n:
                yield (new_i,new_j)
    # for each neighbor of a specific cell that is greater
    # than the specific cell gets out and in degree modified
    for i in range(m):
        for j in range(n):
            for new_i,new_j in get_neighbors(i, j):
                if matrix[i][j] < matrix[new_i][new_j]:
                    out_degrees[(i, j)] += [(new_i, new_j)]
                    in_degrees[(new_i, new_j)]  += 1
    # A cell with in-degree of 0 is a cell that is greater
    # than all its neighbors.
    queue = deque()
    for i in range(m):
        for j in range(n):
            if in_degrees[(i, j)] == 0:
                queue.append((i,j))
    # Go through each level(in degree's with 0 first), and then decrement
    # the indegree for all the nodes the current node points to.
    # If that indegree then becomes 0 after decrement its ready to be
    # inserted to the next batch(level)
    # By each level increment the length
    max_len = 0
    while queue:
        max_len += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for new_coord in out_degrees[i,j]:
                in_degrees[new_coord] -= 1
                if in_degrees[new_coord] == 0:
                    queue.append(new_coord)
    return max_len