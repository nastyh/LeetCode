def findLength(A, B):
    dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    for a_ix in range(len(A)):
        for b_ix in range(len(B)):
            if A[a_ix] == B[b_ix]:
                dp[a_ix][b_ix] = dp[a_ix - 1][b_ix - 1] + 1
    return max([max(i) for i in dp])
    # return dp

 
def findLength_alt(A, B):  # O(AB) both
    dp = [[0] * (len(A) + 1) for _ in range((len(B) + 1))]  # A cols, B rows
    res = 0
    for row in range(1, len(B) + 1):
        for col in range(1, len(A) + 1):
            if A[col - 1] == B[row - 1]:
                dp[row][col] = 1 + dp[row - 1][col - 1]
                res = max(res, dp[row][col])
    return res


def findLength_efficient(A, B):  # O(AB and O(B)
    res = 0
    dp = [[0] * (len(B) + 1) for _ in range(2)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            dp[i % 2][j] = 0
            if A[i - 1] == B[j - 1]:
                dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
                res = max(res, dp[i % 2][j])
    return res 



if __name__ == '__main__':
    print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
    print(findLength_alt([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength_alt([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
    print(findLength_efficient([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength_efficient([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
        