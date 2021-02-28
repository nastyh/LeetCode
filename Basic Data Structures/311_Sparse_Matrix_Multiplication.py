def multiply_brute_force(A, B):  # O(n^3) and O(len(A) * len(B[0])
    """
    Skip multiplying if we have a zero
    """
    mA, nA, nB = len(A),len(A[0]),len(B[0])
    res = [[0]*len(B[0]) for _ in range(mA)]
    for i in range(mA):
        for j in range(nA):
            if A[i][j]:
                for k in range(nB):
                    res[i][k] += A[i][j]*B[j][k]
    return res


def multiply_optmized(A, B):
    """
    Store non-zero in a hashmap of hashmaps 
    """
    m1, n1 = len(A), len(A[0])
    m2, n2 = len(B), len(B[0])
    res = [[0 for i in range(n2)] for j in range(m1)]
    X, Y = [dict() for i in range(m1)], [dict() for j in range(n2)]
    
    for i in range(m1):
        for j in range(n1):
            if A[i][j] != 0:
                X[i][j] = A[i][j]
    
    for i in range(m2):
        for j in range(n2):
            if B[i][j] != 0:
                # watchout (j,i)
                Y[j][i] = B[i][j]
    for i in range(m1):
        for j in range(n2):
            for r in X[i]:
                if r in Y[j]:
                    res[i][j] += X[i][r] * Y[j][r]
    return res


if __name__ == '__main__':
    print(multiply_brute_force([[ 1, 0, 0], [-1, 0, 3]], [[ 7, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 1 ]]))
    print(multiply_brute_force([[1 -5]], [[12], [1]]))