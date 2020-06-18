import math

def twoSumLessThanK(self, A: List[int], K: int) -> int:
    A.sort()
    res = -math.inf
    l, r = 0, len(A) - 1
    while l < r:
        if A[l] + A[r] < K:
            res = max(res, A[l] + A[r])
            l += 1
        else:
            r -= 1
    return res if res != -math.inf else -1
