def champagneTower(poured, query_row, query_glass):
    if poured == 0: return 0
    res = [0]*101
    res[0] = poured
    for row in range(1, query_row + 1):
        for i in range(row, -1, -1):
            res[i] = max(0, (res[i]-1)/2)
            res[i+1] += res[i]
            
    return min(1.0, res[query_glass])   


def champagneTower_alt(poured, query_row, query_glass):
    if poured == 0: return 0
    dp = [[0 for _ in range(x)] for x in range(1, query_row + 2)]
    dp[0][0] = poured
    for i in range(query_row):  # going row by row
        for j in range(len(dp[i])):  # going through the glasses that exist in this row
            t = (dp[i][j] - 1) / 2.0
            if t > 0:
                dp[i + 1][j] += t  # going one row below and filling out a left glass with whatever overflows
                dp[i + 1][j + 1] += t  # going one row below and filling out a right glass with whatever overflows
    return dp[query_row][query_glass] if dp[query_row][query_glass] <= 1 else 1