def tribonacci(n):
    if n == 0: return 0
    if n <= 2: return 1
    dp = [None] * (n + 1)
    dp[0], dp[1], dp[2] = 0, 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    return dp[n]


if __name__ == '__main__':
    print(tribonacci(4))
    print(tribonacci(0))