import math
def depthSumInverse(nestedList):
    max_d = -math.inf
    def _helper(curr, numofList, depth):
        nonlocal max_d
        max_d = max(max_d, depth)
        for obj in curr:
            if isinstance(obj, int):
                numofList.append((depth, obj))
                continue
            _helper(obj, numofList, depth + 1)
    numofList = []
    _helper(nestedList, numofList, 1)
    res = 0
    for depth, num in numofList:
        res += (max_d - depth + 1) * num
    return res

if __name__ == '__main__':
    print(depthSumInverse([[1,1],2,[1,1]]))
