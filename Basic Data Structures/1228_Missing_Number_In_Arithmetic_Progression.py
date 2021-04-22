def missingNumber(arr):  # O(n) and O(1)
    """
    Cover an edge case
    We need to find a step between an element and a missing element. There are two scenarios:
    if it's an increasing sequence, the step is the largest difference [3, 5, 9, 11] --> step will be 4
    if it's a decreasing sequence, the step is the smallest difference [16, 13, 7, 4] --> among [-3, -6, -3] --> step will be -6
    This is a step between element __something_missing__ another element
    So this step is twice as large as a normal one.
    Now go over arr and add this step to an element and check whether what you get is equal to what you see in arr.
    """
    if len(set(arr)) == 1: return arr[0]
    step = 0
    for ix in range(1, len(arr)):
        if arr[ix] - arr[ix - 1] >= 0:
            step = max(step, arr[ix] - arr[ix - 1])
        else:
            step = min(step, arr[ix] - arr[ix - 1])
    for ix in range(1, len(arr)):
        candidate = arr[ix - 1] + step // 2
        if candidate != arr[ix]:
            return candidate
    return step


def missingNumber_binary_search(arr):  # O(logn) and O(1)
    chg = (arr[-1] - arr[0])//len(arr)
    lo, hi = 0, len(arr)
    while lo < hi: 
        mid = lo + hi >> 1
        if arr[mid] == arr[0] + mid * chg: lo = mid + 1
        else: hi = mid
    return arr[0] + lo * chg


if __name__ == '__main__':  
    print(missingNumber([15, 13, 12]))
    print(missingNumber([5, 7, 11, 13]))