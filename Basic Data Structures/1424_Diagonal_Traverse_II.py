from collections import defaultdict
def findDiagonalOrder(nums):
    """
    dict where keys are sums of indices and values are elements but in the opposite order 
    """
    res = []
    d = defaultdict(list)
    for i in range(len(nums)):  # rows
        for j in range(len(nums[i])):  # cols in a given moment
            d[i + j].append(nums[i][j])
    elements = [v[::-1] for v in d.values()]
    for element in elements:
        for digit in element:
            res.append(digit)
    return res
    # return [v for k in d.keys() for v in reversed(d[k])]  # also works 


if __name__ == '__main__':
    print(findDiagonalOrder([[1, 2 ,3],[4, 5, 6],[7, 8, 9]]))
