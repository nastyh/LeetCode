def peakIndexInMountainArray(A):
    return A.index(max(A))

    # alternative
    # for i in range(len(A) - 1):
    #     if A[i + 1] < A[i]:
    #         return i

if __name__ == '__main__':
    print(peakIndexInMountainArray([3, 4, 5, 1]))

