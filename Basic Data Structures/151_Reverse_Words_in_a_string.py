def reverseWords(s):  # Pythonic
    s = s.strip()
    r = [i for i in s.split()]
    return ' '.join(j for j in r[::-1])


def reverseWords_manually(s):
    """
    Need to take care of edge cases: spaces in the beginning and the end of the string
    More than one space in the middle of the string should become only one
    reverse the whole string getting read of the spaces in the beginning and end
    Then reverse every word back
    """
    res, l , r = '', 0, len(s)
    while l < len(s):
        while l < len(s) and s[l] == ' ':
            l += 1
        if l >= len(s):
            break
        r = l + 1
        while r < len(s) and s[r] != ' ':
            r += 1
        w = s[l:r]
        if len(res) == 0:
            res = w
        else:
            res = w + ' ' + res
        l = r + 1
    return res
    

if __name__ == '__main__':
    print(reverseWords_manually('   hello world   '))