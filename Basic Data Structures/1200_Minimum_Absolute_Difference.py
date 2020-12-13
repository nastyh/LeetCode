import math
def minimumAbsDifference(arr):
    arr.sort()
    target = math.inf
    for i in range(1, len(arr)):
        target = min(target, abs(arr[i] - arr[i - 1]))
    res = []
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) == target:
            res.append([arr[i - 1], arr[i]])
    return res