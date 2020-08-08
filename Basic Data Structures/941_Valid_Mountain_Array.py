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


if __name__ == '__main__':
    print(validMountainArray([2, 1]))
    print(validMountainArray([3, 5, 5]))
    print(validMountainArray([0, 3, 2, 1]))
    print(validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))