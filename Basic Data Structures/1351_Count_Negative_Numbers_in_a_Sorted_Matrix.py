def countNegatives(grid):
    res = 0
    def _helper(arr):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right-left) // 2
            if row[mid] < 0:
                right = mid
            else:
                left = mid + 1
        return len(row) - left
    for row in grid:
        res += _helper(row)
    return res
    

def countNegatives_brute_force(grid):
    for row in range(len(grid)):  # rows
        for col in range(len(grid[0])):  # cols
            if grid[row][col] < 0:  
                res += 1
    return res