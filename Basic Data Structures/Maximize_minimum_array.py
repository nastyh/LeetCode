"""
We have an array of N positive elements. We can perform M operations on this array. In each operation we have to select a subarray(contiguous) of length W and increase each element by 1. Each element of the array can be increased at most K times. We have to perform these operations such that the minimum element in the array is maximized.
1 <= N, W <= 10^5
1 <= M, K <= 10^5
"""

from collections import deque
def isFeasible(a, w, m, desMin):
    n = len(a)
    added = 0
    # subDeque = [(i1, v1), (i2, v2), ...]
    # means that we should remove v1 from our "added" running
    # sum when we reach index i1. 
    # monotonic increasing in order of index
    subDeque = deque()
    for i,v in enumerate(a):
        if subDeque and subDeque[0][0] == i:
            added -= subDeque.popleft()[1]
        toAdd = max(0, desMin - v - added)
        if toAdd > 0 and toAdd > m:
            return False
        if toAdd > 0: 
            m -= toAdd
            added += toAdd
            subDeque.append((i + w, toAdd))

    return True
# not bothering to take k since min(k,m) is all that matters anyway
def maximizeMinimum(a, w, m):
    mi = min(a)
    i, j = mi, mi + m

    while i < j - 1:
        mid = (i + j) // 2
        
        if isFeasible(a, w, m, mid):
            i = mid
        else:
            j = mid - 1
        
    return j if isFeasible(a, w, m, j) else i