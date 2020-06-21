def diagonal(elements): # list of lists
    res = []
    m = len(elements) # rows
    n = len(elements[0]) # columns
    for i in range(m + n - 1):
        row = min(i, m -1)
        col = max(0, i - m + 1)
        curr = []
        while row >= 0 and col < n:
            curr.append(elements[row][col])
            row -= 1
            col += 1
        res.append(curr)
    return res




if __name__ == '__main__':
    print(diagonal([[7, 1, 3, 5],[6, 0, 14, 9], [8, 2, 6, 6]]))

'''
Given various subsequences of an array of unique integers, return the original array:

Example: [1, 3, 5], [1, 3, 9], [9, 5]

1 : 3
3 : 5, 9


Output : [1, 3, 9, 5]

'''
