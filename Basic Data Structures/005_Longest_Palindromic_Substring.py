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
    if len(s) <= 1: return s
    if len(s) == len(set(s)): return s[0]
    def _helper(st):
        return st == st[::-1]
    gl_res = -math.inf
    res = ''
    for l in range(len(s) - 1):
        for r in range(l + 1, len(s)):
            if _helper(s[l:r + 1]):
                if len(s[l:r + 1]) > gl_res:
                    gl_res = len(s[l:r + 1])
                    res = s[l:r + 1]
    return res if res != '' else s[0]
                        

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


def longest_dp(s):  # O(n^2) and O(n^2)
    """
    At the main diagonal, put True 
    Start from the second last character
    End is the staring index + 1
    If elements at these indices are equal:
    if they're next to each other (bb) or everything in between is already a palindrome (bacab),
    this is what we need 
    Also save the answer in ans
    """
    if len(s) <= 1: return s
    ans = ''
    dp = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):  # filling out the main diagonal
        dp[i][i] = True
        ans = s[i]
    for l in range(len(s) - 2, -1, -1):
        for r in range(l + 1, len(s)):
            if s[l] == s[r]:  # if a palindrome
                if r - l == 1 or dp[l + 1][r - 1]:  # if it's a two character string or everything in between the characters is already a palindrome 
                    dp[l][r] = True
                    if len(ans) < r - l + 1:
                        ans = s[l: r + 1]
    return ans


# if we need length:
def longest_length_dp(s):
    dp = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):  # diagonals are True
        dp[i][i] = True
    res = 1
    for st in range(len(s) - 1, -1, -1):
        for en in range(st + 1, len(s)):
            if s[st] == s[en]:
                if en - st == 1 or dp[st + 1][en - 1]:
                    dp[st][en] = True
                    res = max(res, en - st + 1)
    return res


if __name__ == '__main__':
    print(longest('abababa'))
    print(longest('ab'))
    print(longest_bf('abababa'))
    print(longest_center('abababa'))
    print(longest_dp('abababa'))
    print(longest_length_dp('cddpd'))
