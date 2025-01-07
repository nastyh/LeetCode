"""
You are given a 2D integer array board of size m x n, where each row
contains exactly 3 distinct numbers. For each row, find the second most frequent
number and return an array containing these numbers for all rows.
"""
def second_most_frequent(board):
    """
    O(m *(n + log(k))) --> O(mn), sizes of board
    O(k) for dict, k is num of dist elements (3 here)
    """
    res = []
    for row in board:
        d_row = Counter()
        sorted_numbers = sorted(d_row.items(), key = lambda x: (-x[1], x[0]))
        if len(sorted_numbers) > 1:
            res.append(sorted_numbers[1][0]) # the second most frequent num
        else:
            res.append(None)
    return res