def countSubstrings(s):  # brute force (O(n*2)), time limit exceeded but works well
    if len(s) <= 1: return len(s)
    def _helper(element, st, e):
        while st < e:
            if element[st] != element[e]:
                return False
            st += 1
            e -= 1
        return True
    l, r, res = 0, 0, len(s)
    while l < len(s) - 1:
        for r in range(l + 1, len(s)):
            if _helper(s, l, r):
                res += 1
        l += 1
    return res 


def countSubstrings_middle(s):  #starting from the middle, also times out
    ans = 0
    def _helper(s, l, r):
        res = 0
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
    for ix in range(len(s)):
        ans += _helper(s, ix, ix) + _helper(s, ix, ix + 1)
    return ans


def countSubstrings_dp(s):  # DP, O(n*2) for both complexity and space
    dp = [[None] * len(s) for _ in range(len(s))]
    res = 0
    for i in range(len(s)):
        res += 1
        dp[i][i] = 1
    for j in range(1, len(s)):
        for i in range(0, j):
            if s[i] == s[j] and j - i <= 2:
                dp[i][j] = 1
                res += 1
            elif s[i] == s[j] and j - i > 2:
                if dp[i + 1][j - 1]:
                    res += 1
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = None
    return  res
    

def countSubstrings_dp_from_the_end(s):  # O(n^2) and O(n^2)
    dp = [[False] * len(s) for _ in range(len(s))]
    res = 0
    for i in range(len(s)):
        res += 1
        dp[i][i] = 1
    for st in range(len(s) - 2, -1, -1):
        for en in range(st + 1, len(s)):
            if s[st] == s[en]:
                if en - st == 1 or dp[st + 1][en - 1]:
                    dp[st][en] = True
                    res += 1
    return res


def countSubstrings_helper(s):  # O(n^2) and O(1)
    """
    Choose all possible centers for palindromes 
    If a string is of the odd length, every character is a center
    If a string is of the even length, every pair of characters is a center
    """
    ans = 0
    def _helper(st, l, r):
        res = 0
        while l >= 0 and r < len(st):
            if st[l] != st[r]:
                break
            l -= 1
            r += 1
            res += 1
        return res
    for i in range(len(s)):
        ans += _helper(s, i, i)
        ans += _helper(s, i, i + 1)
    return ans


if __name__ == '__main__':
    # print(countSubstrings('abc'))
    # print(countSubstrings('aaa'))
    # print(countSubstrings_middle('aaa'))
    # print(countSubstrings_middle('aaa'))
    print(countSubstrings_dp('abc'))
    print(countSubstrings_dp('aaa'))
    print(countSubstrings_dp_from_the_end('abc'))
    print(countSubstrings_dp_from_the_end('aaa'))