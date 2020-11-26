def minFallingPathSum(A): # falling edge cases
    dp = A
    for i in range(1, len(A)):
        # dp[i][0] = min(A[i][0], A[i][1]) + min(dp[i - 1][0], dp[i - 1][1])
        dp[i][0] = A[i][0] + min(dp[i - 1][0], dp[i - 1][1])
        # dp[i][-1] = min(A[i][-1], A[i][-2]) + min(dp[i - 1][-1], dp[i - 1][-2])
        dp[i][-1] = A[i][-1] + min(dp[i - 1][-1], dp[i - 1][-2])
    for n in range(1, len(A[0]) - 1):
        for m in range(1, len(A[0])):
            dp[m][n] = min(A[m][n - 1], A[m][n], A[m][n + 1]) + min(dp[m - 1][n - 1], dp[m - 1][n], dp[m - 1][n + 1])
    return min(dp[-1])


def minFallingPathSum_alt(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr[0])):
            if j == 0:  # first col
                arr[i][j] += min([arr[i - 1][j + 1], arr[i - 1][j]])
            elif j == len(arr[0]) - 1:  # last col
                arr[i][j] += min([arr[i - 1][j - 1], arr[i - 1][j]])
            else:  # all other cols
                arr[i][j] += min([arr[i - 1][j - 1], arr[i - 1][j], arr[i - 1][j + 1]])
    return min(arr[-1])


def minFallingPathSum_straigthforward(arr):
    dp = [[0] * len(arr) for i in range(len(arr[0]))]  # dp with zeroes
    for col in range(len(arr[0])):  # filling out the first row with original numbers
        dp[0][col] = arr[0][col]
    for row in range(1, len(arr)):
        for col in range(len(arr[0])):
            if col == 0:  # filling out the first column starting from the second row
                dp[row][col] = arr[row][col] + min(dp[row - 1][col], dp[row - 1][col + 1])
            elif col == len(arr[0]) - 1:   # filling out the rightmost column from the second row
                dp[row][col] = arr[row][col] + min(dp[row - 1][col], dp[row - 1][col - 1])
            else:  # everything in between
                dp[row][col] = arr[row][col] + min(dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1])
    return min(dp[-1])  # return the smallest number in the last row


if __name__ == '__main__':
    # print(minFallingPathSum([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
    # print(minFallingPathSum([[-19, 57],[-40, -5]])) # doesn't work with this one
    # print(minFallingPathSum_alt([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
    # print(minFallingPathSum_alt([[-19, 57],[-40, -5]]))
    print(minFallingPathSum_straigthforward([[-19, 57],[-40, -5]]))
    print(minFallingPathSum_straigthforward([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
    print(minFallingPathSum_straigthforward([[-51, -35, 74],[-62, 14, -53],[94, 61, -10]]))
    print(minFallingPathSum_straigthforward([[1, 1, 1],[5, 3, 1],[2, 3, 4]]))

