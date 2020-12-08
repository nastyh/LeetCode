def isToeplitzMatrix(matrix):  # checking element vs. its neighbor up and to the left
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


def isToeplitzMatrix_difference(matrix):
    """
    if there are two elements to be compared: [row1][col1] and [row2][col2]
    They're on the same diagonal if row1 - col1 = row2 - col2
    Save values of diagonals to the dict and return False if come across a mismatch
    """
    groups = {}
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if r - c not in groups:
                groups[r - c] = val
            elif groups[r - c] != val:
                return False
    return True


if __name__ == '__main__':
    print(isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))