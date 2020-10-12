def buddyStrings(A, B):
    if A == B:
        if len(A) > len(set(A)):
            return True
    if len(A) != len(B): return False 
    if len(A) < 2 or len(B) < 2: return False
    res = []
    for i in range(len(A)):
        if A[i] != B[i]:
            res.append(i)
    if len(res) == 0:
        return False 
    if len(res) != 2:
        return False
    else:
        if A[res[0]] == B[res[-1]] and B[res[0]] == A[res[-1]]:
            return True
        else:
            return False


if __name__ == '__main__':
    print(buddyStrings('ab', 'ab'))
    print(buddyStrings('aa', 'aa'))