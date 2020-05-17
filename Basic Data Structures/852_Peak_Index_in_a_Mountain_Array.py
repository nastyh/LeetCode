def peakIndexInMountainArray(A):
    return A.index(max(A))
    # res = [0] * len(A)
    # for i in range(len(A) - 1):
    #     if A[i + 1] > A[i]:
    #         res[i + 1] = 1

    # return [k for k,v in enumerate(res) if v == 1][0]

if __name__ == '__main__':
    print(peakIndexInMountainArray([3, 4, 5, 1]))

