def numDecodings(s):
    if s == '0': return 0
    if len(s) == 1: 
        return len(s)
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    if s[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1
    for ix in range(2, len(s) + 1):
        if int(s[ix - 1:ix]) >= 1:
            dp[ix] += dp[ix -1]
        if 26 >= int(s[ix - 2:ix]) >= 10:
            dp[ix] += dp[ix - 2]
    return dp[-1]


if __name__ == '__main__':
    print(numDecodings('226'))