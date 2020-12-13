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

def twoSumLessThanK_bin_search(A, K):
    A.sort()
    res = -1
    for i, num in enumerate(A):
        l, r = i + 1, len(A) - 1
        target = K - num 
        nextLargest = math.inf
        while l < r - 1:
            m = l + (r - l) // 2
            if A[m] < target:
                l = m
            else:
                r = m - 1
        if l < len(A) and A[l] < target:
            otherOne  = A[l]
            if A[r] < target:
                otherOne = max(otherOne, A[r])
            res = max(res, num + otherOne)
    return res


if __name__ == '__main__':
    print(twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60))
    print(twoSumLessThanK([10, 20, 30], -1))
    print(twoSumLessThanK_bin_search([34, 23, 1, 24, 75, 33, 54, 8], 60))
    print(twoSumLessThanK_bin_search([10, 20, 30], -1))