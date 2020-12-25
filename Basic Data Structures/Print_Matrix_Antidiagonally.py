from collections import defaultdict
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


if __name__ == '__main__':
    print(print_antidiagonally([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))