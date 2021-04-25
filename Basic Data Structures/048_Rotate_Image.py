def rotate(matrix):  # O(n^2) and O(1)
    """
    First transpose, then reverse rows
    """
    for row in range(len(matrix[0])):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    for row in range(len(matrix)):
        matrix[row].reverse()

    
def rotate_recur(matrix):
    start = 0
    length = len(matrix)
    def rotate_recu(matrix, start, length):
        if length <= 1:
            return
        # process outer level
        for i in range(0, length - 1):
            tmp = matrix[start + length - 1 - i][start]
            matrix[start + length - 1 - i][start] = matrix[start + length - 1][start + length - 1 - i]
            matrix[start + length - 1][start + length - 1 - i] = matrix[start + i][start + length - 1]
            matrix[start + i][start + length - 1] = matrix[start][start + i]                
            matrix[start][start + i] = tmp
        # process inner level
        rotate_recu(matrix, start + 1, length - 2)
    
    rotate_recu(matrix, start, length)


def rotate_short(matrix):
    matrix[:] = list(zip(*matrix[::-1]))


def rotate_another(matrix):
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = [0] * 4
            row, col = i, j
            for k in range(4):
                tmp[k] = matrix[row][col]
                row, col = col, n - 1 - row
            # rotate 4 elements   
            for k in range(4):
                matrix[row][col] = tmp[(k - 1) % 4]
                row, col = col, n - 1 - row
    return matrix