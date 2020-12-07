def generateMatrix(n):
	steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	direction = 0
	res = [[None] * n for _ in range(n)]
	x, y = 0, 0
	for i in range(1, n * n + 1):
		res[x][y] = i
		a, b = steps[direction]
		if not (n > x + a >= 0 <= y + b < n and not res[x + a][y + b]):
			direction = (direction + 1) % 4
			a, b = steps[direction]
		x = x + a
		y = y + b
	return res


def generateMatrix_alt(n):
    """
    If direction == 0: Move from left to right in top row
    If direction == 1: Move from top to bottom in right column
    If direction == 2: Move from right to left in bottom row
    If direction == 3: Move from bottom to top in left column
    """
    if not n:
        return []
    if n == 1:
        return [[1]]
    
    ans = [[0]* n for _ in range(n)]
    
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    
    k = 1
    direction = 0
    
    while left <= right and top <= bottom:
        # from left to right in top row
        if direction == 0:
            for j in range(left, right + 1):
                ans[top][j] = k
                k += 1
            top += 1
            direction = 1
        elif direction == 1:
            # from top to bottom in right column
            for i in range(top, bottom+1):
                ans[i][right] = k
                k += 1
            right -= 1
            direction = 2
        elif direction == 2:
            # from right to left in bottom row
            for j in range(right, left - 1, -1):
                ans[bottom][j] = k
                k += 1
            bottom -= 1
            direction = 3
        else:
            # bottom to top in left column
            for i in range(bottom, top - 1, -1):
                ans[i][left] = k
                k += 1
            left += 1
            direction = 0
    return ans