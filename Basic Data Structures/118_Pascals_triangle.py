def generate(numRows):
    if numRows   == 0: return []
    elif numRows == 1: return [[1]]
    dp = [[1]]
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(dp[i - 1][j - 1] + dp[i - 1][j]) 
        row.append(1)
        dp.append(row)
    return dp


def generate_dp(numRows):
    dp = [[1] * (numRows + 1) for _ in range(numRows+ 1)]
    for i in range(len(dp[0])):
        for j in range(i):
            if j == i and j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp



if __name__ == '__main__':
    print(generate(5))
    print(generate_dp(5))