from collections import deque
def updateMatrix(matrix):  # O(mn) and O(mn)
    """
    Without creating res but modifying matrix itself
    If a cell not in the deque, it means it's 1. 
    """
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    d = deque()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                visited[row][col] = True
                d.append([row, col])  # put only zero cells in the deque
    while d:
        row, col = d.popleft()
        for row_offset, col_offset in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if row_offset >= 0 and row_offset < len(matrix) and col_offset >= 0 and col_offset < len(matrix[0]) and visited[row_offset][col_offset] == False:
                matrix[row_offset][col_offset] = matrix[row][col] + 1
                visited[row_offset][col_offset] = True
                d.append([row_offset, col_offset])
    return matrix


def updateMatrix_alt(matrix):
    """
    dp originally is for tracking unvisited cells but rewriting it iteratively
    """
    dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]  # not visited are -1
    q = deque()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 0:
                q.append([y, x, 0])
                dp[y][x] = 0
    while q:
        i_step, j_step, step = q.popleft()
        for r, c in [(i_step + 1, j_step), (i_step - 1, j_step), (i_step, j_step - 1), (i_step, j_step + 1)]:
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and dp[r][c] < 0:  # check we aren't out of bounds and haven't been to this cell
                if matrix[r][c] == 1:
                    dp[r][c] = step + 1
                    q.append([r, c, step + 1])
    return dp


if __name__ == '__main__':
    print(updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
    print(updateMatrix_alt([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

