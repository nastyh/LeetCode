def intervalIntersection(A, B):
    res = []
    a, b = 0, 0
    while a < len(A) and b < len(B):
        st = max(A[a][0], B[b][0])
        end = min(A[a][1], B[b][1])

        if st <= end:
            res.append([st, end])
        if A[a][1] < B[b][1]:
            a += 1
        else:
            b += 1
    return res










    # doesn't work with some edge cases
    # res = []
    # combined = sorted(A + B, key = lambda x: x[0])
    # for r in range(len(combined) - 1):
    #     st = max(combined[r][0],combined[r + 1][0])
    #     end = min(combined[r][1],combined[r + 1][1])
    #     if st <= end:
    #         res.append([st,end])
    # return res


if __name__ == '__main__':
    print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
    print(intervalIntersection([[8, 15]], [[2,6], [8, 10], [12,20]]))
