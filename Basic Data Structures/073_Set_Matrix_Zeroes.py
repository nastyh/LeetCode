def setZeroes(matrix):  # O(n) and O(n)
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)  # rows
    n = len(matrix[0])  # columns
    s = set()
    for i in range(m):
        if not all(matrix[i]):
            for j in range(n):
                if matrix[i][j] == 0:
                    s.add(j)
                else:
                    matrix[i][j] = 0
    for i in s:
        for r in range(m):
            matrix[r][i]=0
    return matrix


def setZeroes_efficient(matrix):
    """
    If you see a zero, update the left column and the up-most row to a zero. 
    Traverse again along the left and the upper edges and update the values in respective rows and columns
    """
    m = len(matrix)
    n = len(matrix[0])
    first_row_has_zero = False
    first_col_has_zero = False
    # iterate through matrix to mark the zero row and cols
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row == 0:
                    first_row_has_zero = True
                if col == 0:
                    first_col_has_zero = True
                matrix[row][0] = matrix[0][col] = 0
    # iterate through matrix to update the cell to be zero if it's in a zero row or col
    for row in range(1, m):
        for col in range(1, n):
            matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
    # update the first row and col if they're zero
    if first_row_has_zero:
        for col in range(n):
            matrix[0][col] = 0
    if first_col_has_zero:
        for row in range(m):
            matrix[row][0] = 0
    return matrix


if __name__ == '__main__':
    print(setZeroes([[1, 1, 1],[1, 0, 1],[1, 1, 1]]))
    print(setZeroes([[0, 1, 2, 0],[3, 4, 5, 2],[1, 3, 1, 5]]))
    print(setZeroes_efficient([[1, 1, 1],[1, 0, 1],[1, 1, 1]]))
    print(setZeroes_efficient([[0, 1, 2, 0],[3, 4, 5, 2],[1, 3, 1, 5]]))