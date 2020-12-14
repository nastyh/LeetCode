 def searchMatrix(matrix, target):  # O(m + n) O(1)
     """
     Start from bottom left of the matrix. 
     If current value > target, move up
     If smaller, move right
     """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    height = len(matrix)
    width = len(matrix[0])
    # start our "pointer" in the bottom-left
    row = height - 1
    col = 0
    while col < width and row >= 0:
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:
            return True
    return False


def searchMatrix_bin_search(matrix, target):  # O(nlogn), O(logn)
    if not matrix:
        return False
    def search_rec(left, up, right, down):
        # this submatrix has no height or no width.
        if left > right or up > down:
            return False
        # `target` is already larger than the largest element or smaller
        # than the smallest element in this submatrix.
        elif target < matrix[up][left] or target > matrix[down][right]:
            return False
        mid = left + (right-left) // 2
        # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
        row = up
        while row <= down and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True
            row += 1