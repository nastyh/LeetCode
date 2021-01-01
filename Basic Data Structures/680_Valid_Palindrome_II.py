def validPalindrome(s):
    def _isPal(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return _isPal(s, l + 1, r) or _isPal(s, l, r - 1)
        l += 1
        r -= 1
    return True


def validPalindrome_alt(s):  # for some reason, works slower but passes everything 
    if len(s) <= 1: return True
    def _helper(string, l, r):
        return string[l: r + 1] == string[l: r + 1][::-1]
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            if _helper(s, l + 1, r) or _helper(s, l, r - 1):
                l += 1
                r -= 1
            else:
                return False
        l += 1
        r -= 1
    return True


if __name__ == '__main__':
    print(validPalindrome('abca'))
    print(validPalindrome_alt('abca'))
