def peakIndexInMountainArray(A):
    return A.index(max(A))

    # alternative
    # for i in range(len(A) - 1):
    #     if A[i + 1] < A[i]:
    #         return i


def peakIndexInMountainArray_bin_search(A):  # O(logn)
    """
    There are three cases:
    1. A[m] is the peak
    2. A[m] is not a peak and is a part of the increasing sequence
    3. A[m] is not a peak and is a part of the decreasing sequence
    """
    l, r = 0, len(A) - 1
    while l < r:
        m = l + (r - l) // 2
        if A[m] > A[m + 1]:  # cases 1. and 3.
            r = m
        else:  # case 2 
            l = m + 1
    return l

if __name__ == '__main__':
    print(peakIndexInMountainArray([3, 4, 5, 1]))

