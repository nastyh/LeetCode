from collections import defaultdict
def findDiagonalOrder(nums):  # if to sum up elements' indices on a given diagonal, the number will be the same
    d = defaultdict(list)
    for r in range(len(nums)):
        for c in range(len(nums[0])):
            if r + c not in d:
                d[r + c] = [nums[r][c]]
            else:
                d[r + c].append(nums[r][c])
    res = []
    # for k, v in d.items():  # because the go as a snake
    #     if k % 2 == 1:
    #         res.append(v)
    #     else:
    #         res.append(v[::-1])
    # return [item for sublist in res for item in sublist]  # flattening the list of lists 
    
    for k, v in d.items():  # another way to unpack the dictionary into a list
        if k % 2 == 0:
            res.extend(reversed([i for i in v]))
        else:
            res.extend([j for j in v])
    return res


def findDiagonalOrder_simulation(matrix):
    n, m = len(matrix), len(matrix[0]) if matrix else 0
    i, j, result = 0, 0, []
    if not (n or m):
        return []
    if n == 1:
        return matrix[0]
    if m == 1:
        return [matrix[i][0] for i in range(n)]
    # Traverse the matrix diagonally based on current traversing direction (calculated using
    # Manhattan distance)
    while i * j <= (n - 1) * (m - 1):
        # First, add the number to the results list
        result.append(matrix[i][j])
        # Second, get the Manhattan distance
        manhattan = i + j
        # Based on Manhattan distance, find the traversing direction
        if not manhattan % 2:
            # Direction from bottom-left to top-right
            if not i and j + 1 < m:
                j = j + 1
            elif j == m - 1:
                i = i + 1
            else:
                i, j = i - 1, j + 1
        else:
            # Direction from top-right to bottom-left
            if not j and i + 1 < n:
                i = i + 1
            elif i == n - 1:
                j = j + 1
            else:
                i, j = i + 1, j - 1
    return result

 
if __name__ == '__main__':
    print(findDiagonalOrder([[ 1, 2, 3], [4, 5, 6], [ 7, 8, 9]]))
    print(findDiagonalOrder_simulation([[ 1, 2, 3], [4, 5, 6], [ 7, 8, 9]]))