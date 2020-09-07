def addToArrayForm(A, K):  # most Pythonic
    added = int(''.join([str(i) for i in A])) + K
    res = []
    res.append([i for i in str(added)])
    return list(map(int, res[0]))


def addToArrayForm_alt(A, K):
    if len(A) < len(str(K)):
        for i in range(len(str(K)) - len(A)):
            A.insert(0, 0)
    res, carry = [], 0
    for i in range(len(A) - 1, -1, -1):
        curr_res = 0
        number = A[i] + K % 10 + carry 
        carry = number // 10
        curr_res = number % 10
        res.append(curr_res)
        K = K // 10
    if carry != 0:
        res.append(1)
    return res[::-1]


def test(A, K):
    if len(A) < len(str(K)):
        for i in range(len(str(K)) - len(A)):
            A.insert(0, 0)
    return A


if __name__ == '__main__':
    # print(addToArrayForm([1, 2, 0, 0], 34))
    print(addToArrayForm_alt([1, 2, 0, 0], 34))
    print(addToArrayForm_alt([2, 7, 4], 181))
    print(addToArrayForm_alt([2, 1, 5], 806))
    print(addToArrayForm_alt([9,9,9,9,9,9,9,9,9,9], 1))
    print(addToArrayForm_alt([0], 23))
    # print(test([0], 23))