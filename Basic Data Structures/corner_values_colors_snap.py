"""
Input: 2D integer array / matrix - MXN >= 2. Given corner values / colors
Fill out the matrix

Output: Matrix with filled in values

A 0 0 0 B
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
C 0 0 0 D 

Input Matrix
50 0 0 0 150
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
150 0 0 0 50 

Expected Output
50 75 100 125 150
75 87 100 112 125
100 100 100 100 100
125 112 100 87 75
150 125 100 75 50 
"""

def fill_matrix_with_corners(matrix):
    """
    O(mn) both to process and for res
    Provided values are in the corners 
    we need to calculate the steps so we can move from a smaller value
    to a larger value in a uniform manner 
    if we have 50 X X X 150 
    the step here is (150 - 50) divided by the number of cells to fill + 1
    so we have 100 / (3 + 1) = 25 
    so we will do 50 + 25 = 75
    75 + 25 = 100
    100 + 25 = 125 
    same vertically 

    bilinear interpolation at cell (i;j): 
    A * (1 - x) * (1 - y) + 
            B * x * (1 - y) + 
            C * (1 - x) * y + 
            D * x * y
        
        x = j / (N - 1)
        y = i / (M - 1)
    """
    M, N = len(matrix), len(matrix[0]) # rows, cols 
    res = [[0] * N for _ in range(M)]
    A = matrix[0][0] # upper left 
    B = matrix[0][N-1] # upper right 
    C = matrix[M-1][0] # lower left
    D = matrix[M-1][N-1] # lower right 

    for i in range(M):
        y = i / (M - 1)
        for j in range(N):
            x = j / (N - 1)
            res[i][j] = round(
                A * (1 - x) * (1 - y) +
                B * x * (1 - y) +
                C * (1 - x) * y +
                D * x * y
            )
    return res

def fill_matrix_with_corners_step_by_step(matrix):
    """
    O(mn) both 
    fill out the sides of the matrix by 
    if we have 50 X X X 150 
    the step here is (150 - 50) divided by the number of cells to fill + 1
    so we have 100 / (3 + 1) = 25 
    so we will do 50 + 25 = 75
    75 + 25 = 100
    100 + 25 = 125 
    """
    M, N = len(matrix), len(matrix[0])
    result = [[0] * N for _ in range(M)]

    # Get corner values
    A = matrix[0][0]          # Top-left
    B = matrix[0][N-1]        # Top-right
    C = matrix[M-1][0]        # Bottom-left
    D = matrix[M-1][N-1]      # Bottom-right

    # Step 1: Fill top row
    for j in range(N):
        if j == 0:
            result[0][j] = A
        elif j == N - 1:
            result[0][j] = B
        else:
            step = (B - A) / (N - 1)
            result[0][j] = round(A + step * j)

    # Step 2: Fill bottom row
    for j in range(N):
        if j == 0:
            result[M - 1][j] = C
        elif j == N - 1:
            result[M - 1][j] = D
        else:
            step = (D - C) / (N - 1)
            result[M - 1][j] = round(C + step * j)

    # Step 3: Fill left column (top to bottom)
    for i in range(M):
        if i == 0 or i == M - 1:
            continue  # already filled
        step = (C - A) / (M - 1)
        result[i][0] = round(A + step * i)

    # Step 4: Fill right column (top to bottom)
    for i in range(M):
        if i == 0 or i == M - 1:
            continue  # already filled
        step = (D - B) / (M - 1)
        result[i][N - 1] = round(B + step * i)

    # Step 5: Fill inner cells by interpolating between left and right values
    for i in range(1, M - 1):
        left = result[i][0]
        right = result[i][N - 1]
        for j in range(1, N - 1):
            step = (right - left) / (N - 1)
            result[i][j] = round(left + step * j)

    return result
