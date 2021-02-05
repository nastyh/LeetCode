def numWays_bf(steps, arrLen):  # DFS. Time: O(3^N) Space: O(1).
    def dfs(steps, arrLen, pos):
        if pos < 0 or pos >= arrLen:
            return 0
        if steps == 0:
            return 1 if pos == 0 else 0
        return dfs(steps - 1, arrLen, pos - 1) + dfs(steps - 1, arrLen, pos) + dfs(steps - 1, arrLen, pos + 1)
    if steps is None or steps < 0 or not arrLen:
        return 0
    return dfs(steps, arrLen, 0)


def numWays_memo(steps, arrLen):  #  O(steps * min(arrLen, steps + 1)), Space: O(steps * min(arrLen, steps + 1))
    def dfs(steps, arrLen, pos, memo):
        if (steps, pos) in memo:
            return memo[(steps, pos)]
        if pos < 0 or pos > arrLen - 1:
            memo[(steps, pos)] = 0
            return 0
        if steps == 0:
            return 1 if pos == 0 else 0
        memo[(steps, pos)] = dfs(steps - 1, arrLen, pos - 1, memo) + dfs(steps - 1, arrLen, pos, memo) \
                            + dfs(steps - 1, arrLen, pos + 1, memo) 
        return memo[(steps, pos)] % (10 ** 9 + 7)

    if steps is None or steps < 0 or not arrLen:
        return 0
    memo = {}
    return dfs(steps, arrLen, 0, memo)


def numWays_optimized(steps, arrLen):  #  O(steps * min(arrLen, steps + 1)) Space: O(steps * min(arrLen, steps + 1))
    if steps is None or steps < 0 or not arrLen:
        return 0
    arrLen = min(arrLen, steps + 1)
    prev = [1] + [0] * (arrLen - 1)
    for i in range(1, steps + 1):     
        cur = [0] * arrLen
        for j in range(arrLen):
            cur[j] += prev[j]
            if j > 0:
                cur[j] += prev[j - 1]
            if j < arrLen - 1:
                cur[j] += prev[j + 1]
        prev = cur
    return prev[0] % (10 ** 9 + 7)


def numWays_optimized_alt(steps, arrLen):  # O(steps * min(arrLen, steps + 1)) Space: O(min(arrLen, steps + 1))
    if steps is None or steps < 0 or not arrLen:
        return 0
    arrLen = min(arrLen, steps + 1)
    prev = [1] + [0] * (arrLen - 1)
    cur = [0] * arrLen
    for i in range(1, steps + 1):     
        for j in range(arrLen):
            cur[j] = 0
            cur[j] += prev[j]
            if j > 0:
                cur[j] += prev[j - 1]
            if j < arrLen - 1:
                cur[j] += prev[j + 1]
        prev, cur = cur, prev
    return prev[0] % (10 ** 9 + 7)


def numWays_minimal(steps, arrLen):  # 
    arrLen = min(arrLen, steps + 1) 
    f = [1] + [0] * (arrLen - 1) # f[0] = 1

    for i in range(1, steps + 1):
        old = 0 
        for j in range(arrLen):
            old_left = old
            old = f[j]
            if j > 0:
                f[j] += old_left      
            if j < arrLen - 1:
                f[j] += f[j + 1]   
    return f[0] % (10 ** 9 + 7) 


def min_ways_dp_2d(steps, arrLen):  # TLE  O(steps*arrLen) both 
    dp = [[0] * arrLen for _ in range(steps + 1)]
    dp[0][0] = 1
    for row in range(1, steps + 1):
        for col in range(arrLen):
            if col == 0:
                dp[row][col] = dp[row - 1][col] + dp[row - 1][col + 1]
            elif col == arrLen - 1:
                dp[row][col] = dp[row - 1][col] + dp[row - 1][col - 1]
            else:
                dp[row][col] = dp[row - 1][col] + dp[row - 1][col - 1] + dp[row - 1][col + 1]
    return dp[steps][0] % (10 ** 9 + 7)


if __name__ == '__main__':
    print(min_ways_dp_2d(3, 2))
    print(min_ways_dp_2d(2, 4))
    print(min_ways_dp_2d(4, 2))