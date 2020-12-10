def validMountainArray( A):
    if len(A) < 3: return False
    m_ix = A.index(max(A))
    if m_ix == 0 or m_ix == len(A) - 1: return False
    ll, rl = [], []
    ll.append(A[m_ix])
    rl.append(A[m_ix])

    for i in range(m_ix - 1, -1, -1):
        if ll[-1] > A[i]:
            ll.pop()
            ll.append(A[i])
        else:
            ll.append(A[i])
    for j in range(m_ix + 1, len(A)):
        if rl[-1] > A[j]:
            rl.pop()
            rl.append(A[j])
        else:
            rl.append(A[j])
    return len(ll) == 1 and len(rl) == 1


def validMountainArray_alt(A):
    """
    Cover edge cases.
    Start iterating through the list looking for the max number.
    If it's in the beginning or very end, return False
    Store the value in decreasing_val
    Every value after it should be lower. But also we need to update itself, so that we avoid saddle points
    b/c every further value should be strictly lower than one to the left
    """
    if len(A) < 3: return False
    if len(set(A)) == 1: return False
    top_ix = -1
    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            top_ix = i + 1
        else: break
    if top_ix == 0 or top_ix == len(A) - 1:
        return False
    decreasing_val = A[top_ix]
    for j in range(top_ix + 1, len(A)):
        if A[j] < decreasing_val:
            decreasing_val = A[j]
        else:
            return False
    return True
        


if __name__ == '__main__':
    print(validMountainArray([2, 1]))
    print(validMountainArray([3, 5, 5]))
    print(validMountainArray([0, 3, 2, 1]))
    print(validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(validMountainArray_alt([2, 1]))
    print(validMountainArray_alt([3, 5, 5]))
    print(validMountainArray_alt([0, 3, 2, 1]))
    print(validMountainArray_alt([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(validMountainArray_alt([0, 1, 2, 1, 2]))