def fourSumCount(A, B, C, D):
    m = {}

    def nSumCount(lists):
        addToHash(lists, 0, 0)
        return countComplements(lists, len(lists) // 2, 0)

    def addToHash(lists, i, sum):
        if i == len(lists) // 2:
            m[sum] = m.get(sum, 0) + 1
        else:
            for a in lists[i]:
                addToHash(lists, i + 1, sum + a)

    def countComplements(lists, i, complement):
        if i == len(lists):
            return m.get(complement, 0)
        cnt = 0
        for a in lists[i]:
            cnt += countComplements(lists, i + 1, complement - a)
        return cnt

    return nSumCount([A, B, C, D])


def fourSumCount_alt(A, B, C, D):
    """
    store all the combinations of sum of the elements present in C and D in the d
    also store the number of time a particular sum comes up in C and D as these can be different combinations
    iterate over A and B and check whether the remaining required sum is present in the d
    if present then add the number of times the that particular sum came up in d
    """
    res = 0
    d={}
    for i in C:
        for j in D:
            s = i + j
            if s not in d.keys():
                d[s] = 1
            else:
                d[s] += 1
    for i in A:
        for j in B:
            if 0 - i - j in d.keys():
                res += d[0 - i - j]
    return res


if __name__ == '__main__':
    print(fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
    print(fourSumCount_alt([1, 2], [-2, -1], [-1, 2], [0, 2]))