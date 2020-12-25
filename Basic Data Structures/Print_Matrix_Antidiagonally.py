from collections import defaultdict, deque
def print_antidiagonally(matrix):
    """
    given 
    1   2   3   4
    5   6   7   8
    9  10  11  12
    13 14  15  16

    print: 1, 2, 5, 3, 6, 9, 4, 7, 10, 13, 8, 11, 14, 12, 15, 16
    """
    d = defaultdict(list)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            d[row + col].append(matrix[row][col])
    values = [v for v in d.values()]
    res = []
    for lst in values:
        for num in lst:
            res.append(num)
    return res


def print_antidiagonally_BFS(matrix):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    res = []
    d = deque()
    d.append((0, 0))
    while d:
        row, col = d.popleft()
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or visited[row][col] == True:
            continue
        res.append(matrix[row][col])
        visited[row][col] = True
        d.append((row, col - 1))
        d.append((row, col + 1))
        d.append((row - 1, col))
        d.append((row + 1, col))
    return res
        



if __name__ == '__main__':
    print(print_antidiagonally([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
    print(print_antidiagonally_BFS([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))