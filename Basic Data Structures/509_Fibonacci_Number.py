def fib_dp(n):  # O(n) both
    if n <= 1: return n
    dp = [None] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[-1]


def fib_brute_force(n):  # O(2^N) and O(n) for the stack
    if n <= 1: return n
    else:
        return fib_brute_force(n - 2) + fib_brute_force(n - 1)


def fib_recurs_memoization(n):   # O(n) both
    d = {0: 0, 1: 1}
    if n in d: return d[n]
    else:
        d[n - 2] = fib(n - 2)
        d[n - 1] = fib(n - 1)
        return d[n - 2] + d[n - 1]


def fib_3_vars(n):  # O(n) and O(1)
    """
    Need to keep track of two past variables: at indices n - 2 (l) and n - 1 (r)
    """
    if n <= 1: return n
    l, r, res = 0, 1, 0
    for _ in range(2, n + 1):
        res = l + r
        l = r
        r = res
    return res


def fib_matrix(n):  # O(logN) both
    if n <= 1: return n
    A = [[1, 1], [1, 0]]

     def multiply(A, B):
        x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        w = A[1][0] * B[0][1] + A[1][1] * B[1][1]
        A[0][0] = x
        A[0][1] = y
        A[1][0] = z
        A[1][1] = w
    
    def matrix_power(A, n):
        if (n <= 1):
            return A

        matrix_power(A, n // 2)
        multiply(A, A)
        B = [[1, 1], [1, 0]]
        if (n % 2 != 0):
            multiply(A, B)

    matrix_power(A, N - 1)
    return A[0][0]


def fib_golden_ratio(n):  # O(1) both 
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** N + 1) / 5 ** 0.5)