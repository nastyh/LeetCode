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
    for k, v in d.items():  # because the go as a snake
        if k % 2 == 1:
            res.append(v)
        else:
            res.append(v[::-1])
    return [item for sublist in res for item in sublist]  # flattening the list of lists 


if __name__ == '__main__':
    print(findDiagonalOrder([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]))