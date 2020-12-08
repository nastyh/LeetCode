def searchMatrix_brute_force(matrix, target):  # O(logmn) + O(mn) to build a list. O(nm) to store
    """
    Flatten a matrix into a list, do binary search
    """
    new_l = []
    for row in matrix:
        for num in row:
            new_l.append(num)
    l, r = 0, len(new_l) - 1
    while l <= r:
        m = l + (r - l) // 2
        if new_l[m] == target:
            return True
        elif new_l[m] < target:
            l = m + 1
        else:
            r = m - 1
    return False


def searchMatrix_efficient(matrix, target):
    """
    using rows and cols as it is
    """
     if len(matrix) == 0:
        return False
    l, r = 0, len(matrix) * len(matrix[0]) - 1
    while l <= r:
        m = (l + r) // 2
        m_ix = matrix[m // len(matrix[0])][m % len(matrix[0])]
        if target == m_ix:
            return True
        elif target < m_ix:
            r = m - 1
        else:
            l = m + 1
    return False

