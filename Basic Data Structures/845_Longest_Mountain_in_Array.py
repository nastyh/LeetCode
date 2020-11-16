def longestMountain(A):
    """
    Traverse the list while you find a (local) peak
    Once you found it, go left and right: check while statement, they're some tricky conditions
    Keep track of the best result
    """
    if len(A) < 3: return 0
    if len(set(A)) == 1: return 0
    res = 0
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            l = i - 1
            r = i + 1
            while l > 0 and A[l - 1] < A[l]:
                l -= 1
            while r < len(A) - 1 and A[r + 1] < A[r]:
                r += 1
            res = max(res, r - l + 1)
    return res


if __name__ == '__main__':
    print(longestMountain([2, 1, 4, 7, 3, 2, 5]))
    print(longestMountain([0, 1, 0]))
    print(longestMountain([2, 0, 2, 0]))