def setZeroes(matrix):  # O(n) and O(n)
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)  # rows
    n = len(matrix[0])  # columns
    s = set()
    for i in range(m):  # taking rows
        if not all(matrix[i]):  # if not all numbers in the row are 1
            for j in range(n):  # going through this row one by one (by column, essentially)
                if matrix[i][j] == 0:
                    s.add(j)
                else:
                    matrix[i][j] = 0
    for i in s:
        for r in range(m):
            matrix[r][i]  =0
    return matrix


def setZeroes_another(matrix):  #O(mn) and O(m + n)
    """
    Have two extra lists with the size of row and col of the matrix
    Go through the matrix, if you see 0, put True in respective places in both helper lists
    Then go throuh the row helper. If it True, it means that this row in the matrix should become 0
    Then go throuh the col helper. If it True, it means that this col in the matrix should become 0
    """
    row_helper, col_helper = [False] * len(matrix), [False] * len(matrix[0])
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                row_helper[r] = True
                col_helper[c] = True
    for row_ix in range(len(row_helper)):
        if row_helper[row_ix] == True:
            for col in range(len(matrix[0])):
                matrix[row_ix][col] = 0
    for col_ix in range(len(col_helper)):
        if col_helper[col_ix] == True:
            for row in range(len(matrix)):
                matrix[row][col_ix] = 0
    # print(row_helper)
    # print(col_helper)
    # return matrix


def setZeroes_constant_space(matrix):  # O(mn) and O(1)
    is_col = False
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R):
        # and using matrix[0][0] for the first row.
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, C):
            # If an element is zero, we set the first element of the corresponding row and column to 0
            if matrix[i][j]  == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, R):
        for j in range(1, C):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0
    # See if the first row needs to be set to zero as well
    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0
    # See if the first column needs to be set to zero as well        
    if is_col:
        for i in range(R):
            matrix[i][0] = 0


def setZeroes_efficient(matrix):  # O(mn) and O(1)
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
    # print(setZeroes([[1, 1, 1],[1, 0, 1],[1, 1, 1]]))
    # print(setZeroes([[0, 1, 2, 0],[3, 4, 5, 2],[1, 3, 1, 5]]))
    print(setZeroes_another([[1, 1, 1],[1, 0, 1],[1, 1, 1]]))
    print(setZeroes_another([[0, 1, 2, 0],[3, 4, 5, 2],[1, 3, 1, 5]]))
    # print(setZeroes_efficient([[1, 1, 1],[1, 0, 1],[1, 1, 1]]))
    # print(setZeroes_efficient([[0, 1, 2, 0],[3, 4, 5, 2],[1, 3, 1, 5]]))