def addToArrayForm(A, K):  # most Pythonic
    added = int(''.join([str(i) for i in A])) + K
    res = []
    res.append([i for i in str(added)])
    return list(map(int, res[0]))

def addToArrayForm_pythonic(A, K):
    """
    List to integer
    Sum numbers and save to res
    Make a list from res
    Edge case is for [0], 0 b/c ans in this case is []
    """
    num = int(''.join(str(i) for i in A))
    res = num + K
    ans = []
    base = 0
    while res != 0:
        num = res % 10
        res = res // 10
        ans.append(num)
    return ans[::-1] if len(ans) > 0 else [0]


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

def addToArrayForm_alt_different(A, K):
    """
    Key here is to make A and K of the same length.
    Otherwise some edge cases would failt (such as [0], 23). We need to make [0, 0], 23
    """
    res = []
    carry = 0
    if len(A) < len(str(K)):
        for i in range(len(str(K)) - len(A)):
            A.insert(0, 0)
    for digit in A[::-1]:
        num = digit + K % 10 + carry  # 5 + 6 + 0 
        res.append(num % 10)
        K = K // 10
        carry = num // 10
    if carry != 0:
        res.append(1)
    return res[::-1]



if __name__ == '__main__':
    # print(addToArrayForm([1, 2, 0, 0], 34))
    print(addToArrayForm_alt([1, 2, 0, 0], 34))
    print(addToArrayForm_alt([2, 7, 4], 181))
    print(addToArrayForm_alt([2, 1, 5], 806))
    print(addToArrayForm_alt([9,9,9,9,9,9,9,9,9,9], 1))
    print(addToArrayForm_alt([0], 23))