def minSteps(n):  # O(n) both
    if n == 1:
        return 0
    if n == 2:
        return 2
    dp = [float('inf')] * (n + 1)  # dp[i] denote minimal operations for i 'A'
    dp[1] = 0
    dp[2] = 2
    for i in range(3, n + 1):
        for j in range(1, i):
            # copy from anywhere when the number of missing 'A' (i-j)
            # is dividable by the number of existing 'A' (j)
            # the bottom line is when j == 1
            # 1 copy + (i-j)/j paste
            if (i - j) % j == 0:
                dp[i] = min(dp[i], dp[j] + 1 + (i-j) // j)
    return dp[n]


def minsteps_math(n):  # O(sqrt(n)) and O(1)
    """
    Takes advantage of prime factors
    """
    ans = 0
    d = 2
    while n > 1:
        while n % d == 0:
            ans += d
            n /= d
        d += 1
    return ans


