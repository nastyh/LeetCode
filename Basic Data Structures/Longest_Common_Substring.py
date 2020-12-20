def longest_common_substring_dp_bottoms_up(s1, s2):  # O(NM) both
    res = 0
    dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]  # s1 along the cols, s2 along the rows
    for row in range(1, len(s2)):
        for col in range(1, len(s1)):
            if s1[col - 1] == s2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
                res = max(res, dp[row][col])
    return res


def longest_common_substring_dp_bottoms_up_efficient(s1, s2):  # O(NM) and O(M), where N and M are lengths 
    res = 0
    dp = [[0] * (len(s2) + 1) for _ in range(2)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i % 2][j] = 0
            if s1[i - 1] == s2[j - 1]:
                dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
                res = max(res, dp[i % 2][j])
    return res 


def longest_common_substring_dp_top_down(s1, s2):
    n1, n2 = len(s1), len(s2)
    maxLength = min(n1, n2)
    dp = [[[-1 for _ in range(maxLength)] for _ in range(n2)] for _ in range(n1)]
    def _helper(dp, s1, s2, i1, i2, count):
        if i1 == len(s1) or i2 == len(s2):
            return count
        if dp[i1][i2][count] == -1:
            c1 = count
            if s1[i1] == s2[i2]:
                c1 = _helper(dp, s1, s2, i1 + 1, i2 + 1, count + 1)
            c2 = _helper(dp, s1, s2, i1, i2 + 1, 0)
            c3 = _helper(dp, s1, s2, i1 + 1, i2, 0)
            dp[i1][i2][count] = max(c1, max(c2, c3))
        return dp[i1][i2][count]
    return _helper(dp, s1, s2, 0, 0, 0)
    

if __name__ == '__main__':
    print(longest_common_substring_dp_bottoms_up('abdca', 'cbda'))
    print(longest_common_substring_dp_bottoms_up('passport', 'ppsspt')) 
    print(longest_common_substring_dp_bottoms_up_efficient('abdca', 'cbda'))
    print(longest_common_substring_dp_bottoms_up_efficient('passport', 'ppsspt')) 
    print(longest_common_substring_dp_top_down('abdca', 'cbda'))
    print(longest_common_substring_dp_top_down('passport', 'ppsspt')) 