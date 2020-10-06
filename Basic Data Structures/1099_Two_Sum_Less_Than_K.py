import math
def twoSumLessThanK(A, K):
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


if __name__ == '__main__':
    print(twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60))
    print(twoSumLessThanK([10, 20, 30], -1))