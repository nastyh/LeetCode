import math
def longest(s):
    if not s: return s
    res = ""
    for i in range(len(s)):
        j = i + 1
        # While j is less than length of string
        # AND res is *not* longer than substring s[i:]
        while j <= len(s) and len(res) <= len(s[i:]):
            # If substring s[i:j] is a palindrome
            # AND substring is longer than res
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                res = s[i:j]
            j += 1
    return res


def longest_bf(s):  # brute force
    glob_l, curr_res = -math.inf, ''
    def _helper(s):
        return s == s[::-1]
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if _helper(s[i:j + 1]):
                if len(s[i:j + 1]) > glob_l:
                    glob_l = len(s[i:j + 1])
                    curr_res = s[i:j + 1]
    return curr_res


def longest_center(s):  # going wide from the center
    def _helper(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
    if len(s) <= 1: return s
    st, en = 0, 0 
    for i in range(len(s)):
        l = max(_helper(s, i, i), _helper(s, i, i + 1))
        if l > en - st:
            st = i - (l - 1) // 2
            en = i + l // 2
    return s[st:en + 1]


def longest_dp(s):
    if len(s) <= 1: return s
    ans = ''
    dp = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):  # filling out the main diagonal
        dp[i][i] = True
        ans = s[i]
    for l in range(len(s) - 1, -1, -1):
        for r in range(l + 1, len(s)):
            if s[l] == s[r]:  # if a palindrome
                if r - l == 1 or dp[l + 1][r - 1]:  # if it's a two character string or everything in between the characters is already a palindrome 
                    dp[l][r] = True
                    if len(ans) < r - l + 1:
                        ans = s[l: r + 1]
    return ans


if __name__ == '__main__':
    print(longest('abababa'))
    print(longest_bf('abababa'))
    print(longest_center('abababa'))
    print(longest_dp('abababa'))
