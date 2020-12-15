def peakIndexInMountainArray(A):
    return A.index(max(A))

    # alternative
    # for i in range(len(A) - 1):
    #     if A[i + 1] < A[i]:
    #         return i


def peakIndexInMountainArray_bin_search(A):
    l, r = 0, len(A) - 1
    while l < r:
        m = l + (r - l) // 2
        if A[m] > A[m + 1]:
            r = m
        else:
            l = m + 1
    return l

if __name__ == '__main__':
    print(peakIndexInMountainArray([3, 4, 5, 1]))

