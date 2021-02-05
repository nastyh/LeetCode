def searchMatrix_brute_force(matrix, target):  # O(logmn) + O(mn) to build a list --> o(mn). O(nm) to store
    """ 
    _bin() does binary search
    make a list and apply _bin() to it 
    """
    def _bin(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
    
    vals = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            vals.append(matrix[row][col])
    return _bin(vals, target)


def searchMatrix_easy(matrix, target):  # O(log(nm)) and O(1)
    row = 0
    for r in range(len(matrix)):
        if target == matrix[r][0] or target == matrix[r][-1]:
            return True
        elif target > matrix[r][0] and target < matrix[r][-1]:
            row = r
            break
    l, r = 0, len(matrix[row]) - 1
    while l <= r:
        m = l + (r - l) // 2
        if matrix[row][m] == target:
            return True
        elif matrix[row][m] < target:
            l = m + 1
        else:
            r = m - 1
    return False


def searchMatrix_efficient(matrix, target):  # O(log(nm)) and O(1)
    """
    using rows and cols as it is
    """
    if len(matrix) == 0:
        return False
    l, r = 0, len(matrix) * len(matrix[0]) - 1
    while l <= r:
        m = (l + r) // 2
        # we cannot write matrix[m] and need to express m in terms of rows (or cols)
        m_ix = matrix[m // len(matrix[0])][m % len(matrix[0])]  # row is (m // # of cols). col is (m % # of cols) 
        if target == m_ix:
            return True
        elif target < m_ix:
            r = m - 1
        else:
            l = m + 1
    return False


if __name__ == '__main__':
    print(searchMatrix_efficient([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 23))
    print(searchMatrix_efficient([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0))
