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
    

def countNegatives_brute_force(grid):  # O(row * col) and O(1)
    for row in range(len(grid)):  # rows
        for col in range(len(grid[0])):  # cols
            if grid[row][col] < 0:  
                res += 1
    return res


def countNegatives_bin_search(grid):  # O(row * log(col)) and O(1)
    """
    for every row, get the index of the first negative number. Then len(row) - this number gives the number of negative elements
    Edge case: when the whole row consists of positive numbers. We take care of it by checking nums[-1] in the return statement 
    """
    res = 0
    def _helper(nums): 
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= 0:
                l = m + 1
            else:
                r = m
        return len(nums) - r if nums[-1] < 0 else 0
    for row in grid:
        res += _helper(row)
    return res


if __name__ == '__main__':
    print(countNegatives_bin_search([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])) 
    print(countNegatives_bin_search([[3, 2], [1, 0]]))
