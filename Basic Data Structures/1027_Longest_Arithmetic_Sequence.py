from collections import defaultdict
def longestArithSeqLength_dp(A):  # O(n^2) and O(n)
    dp = [defaultdict(int) for _ in range(len(A))]
    res = 2
    for i in range(1, len(A)):
        for j in range(i):
            diff = A[i] - A[j]
            dp[i][diff] = max(2, dp[j][diff]+1)
            res = max(res, dp[i][diff])
    return res


def longestArithSeqLength_dict(A):  # O(n^2) and O(n)
    ans = 0
    dp = defaultdict(lambda: 1)
    for i in range(len(nums) -1, -1, -1):
        for j in range(i + 1, len(nums)):
            d = nums[j] - nums[i]
            dp[i, d] = max(dp[i, d], 1 + dp[j, d])
            ans = max(dp[i, d], ans)
    return ans


def longestArithSeqLength_brute_force(A):  # O(n^3) TLE
    if len(A) == 2: return 2
    res = 2
    for l in range(len(A) - 1):
        for r in range(l + 1, len(A)):
            diff = A[r] - A[l]
            target = A[r] + diff
            curr_res = 2
            for j in range(r + 1, len(A)):
                if A[j] == target:
                    curr_res += 1
                    res = max(res, curr_res)
                    target += diff
    return res


if __name__ == '__main__':
    print(longestArithSeqLength_brute_force([3, 6, 9, 12]))
    print(longestArithSeqLength_brute_force([9, 4, 7, 2, 10]))
    print(longestArithSeqLength_brute_force([20, 1, 15, 3, 10, 5, 8]))
    print(longestArithSeqLength_brute_force([83, 20, 17, 43, 52, 78, 68, 45]))
            