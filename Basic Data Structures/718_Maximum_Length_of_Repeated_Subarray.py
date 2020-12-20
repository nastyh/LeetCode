def findLength(A, B):
    dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    for a_ix in range(len(A)):
        for b_ix in range(len(B)):
            if A[a_ix] == B[b_ix]:
                dp[a_ix][b_ix] = dp[a_ix - 1][b_ix - 1] + 1
    return max([max(i) for i in dp])
    # return dp


def findLength_alt(A, B):
    dp = [[0] * (len(A) + 1) for _ in range((len(B) + 1))]  # A cols, B rows
    



if __name__ == '__main__':
    print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
        