"""
Given a binary M × N row-wise sorted matrix, find a row that contains the maximum number of 1's in linear time.
"""
def row_with_max_ones(matrix):
    """
    O(r+c) --> top most row containing the most 1s
    O(1)
    If the current cell has value 1, continue moving left till we encounter 0, or all columns are processed;
    If the current cell has value 0, continue moving down till we encounter 1, or all rows are processed.
    return the row index of the last cell in which we have seen 1
    """
    r, c = len(matrix), len(matrix[0]) # rows and cols
    res = -1
    i, j = 0, len(matrix[0]) - 1 # curr row and col index
    while i < r and j >= 0: # start at the top right corner
        if matrix[i][j] == 1: # found a 1 farther left than any we’ve seen so far
            res = i 
            j -= 1 # move left to see if there are even more 1’s in this row
        else: # No 1’s in this column of the current row
            i+= 1 # go to the next row
    return res
