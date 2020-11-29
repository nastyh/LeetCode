def maximalSquare_extra(matrix):
    """
    Build dp one row and one col larger than matrix
    Extra col and rows are zeros
    Start filling out.
    If the respective element in matrix is zero, do nothing
    If it's one, take the min of (element to the left, element on top, element left and up) + 1
    Also keep track of the largest value
    Return the squared value at the end
    """
    dp = [[0] * (len(matrix[0]) + 1) for y in range(len(matrix) + 1)]  
    max_val = 0
    for row in range(1, len(matrix) + 1):
        for col in range(1, len(matrix[0]) + 1):
            if matrix[row - 1][col - 1] == '1':
               dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
               max_val = max(max_val, dp[row][col])
    return max_val**2


if __name__ == '__main__':
    print(maximalSquare_extra([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(maximalSquare_extra([["0"]]))
    print(maximalSquare_extra([["0", "1"]]))