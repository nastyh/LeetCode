def spiralOrder_recur(matrix):
    """
    take the first line of the matrix, then rotate it 90 degrees counter clockwise
    and apply the same procedure to the new matrix and combine the first line with the previous first line.
    """
    first = list(matrix[0]) 
    if len(matrix) == 1:
        return first
    else:
        left = matrix[1:]
        # The following two lines will rotate the left matrix 90 degrees counter-clockwise
        left = list(zip(*left)) # rotate 90 degrees to the right
        left.reverse() # rotate 180 degrees to the left
        return first + spiralOrder(left)


def spiralOrder(matrix):  # O(N) both, where N is the total number of elements 
    res = []
    h = len(matrix)
    if h < 1:
        return res
    w = len(matrix[0])
    # pointers we will use to iterate round the matrix
    top = 0
    bottom = h - 1
    left = 0
    right = w - 1
    while top <= bottom and left <= right:
        # TOP section: left to right
        l = left
        while l <= right:  # and left <= right: <-- we will never reach that condition
            res.append(matrix[top][l])
            l += 1
        # move lower
        # because: added all from the top area
        top += 1
        # RIGHT section: top to bottom
        t = top
        while t <= bottom:  # and top <= bottom: <-- we will never reach that condition
            res.append(matrix[t][right])
            t += 1
        # move pointer to the left
        # done with right-most section
        right -= 1
        # BOTTOM section: right to left
        # on the last of the spiral, char: right = left, therefore, r = left
        # so the while loop might run again
        r = right
        while r >= left and top <= bottom:
            res.append(matrix[bottom][r])
            r -= 1
        bottom -= 1
        # LEFT section: bottom to top
        # on the last of the spiral, char: bottom = top, therefore, b = top
        # so the while loop might run again
        # that's why we have the extra condition
        b = bottom
        while b >= top and left <= right:
            res.append(matrix[b][left])
            b -= 1
        left += 1
    return res