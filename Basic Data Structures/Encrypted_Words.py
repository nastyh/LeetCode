def findEncryptedWord(s):  # O(n) both 
    """
    First, base conditions
    Second, index
    Third, build an answer
    """
    curr_ix = 0
    def _helper(curr_str):
        nonlocal curr_ix
        if len(curr_str) == 0:
            return ''
        if len(curr_str) == 1:
            return curr_str
        curr_ix = (0 + len(curr_str) - 1) // 2
        return curr_str[curr_ix] + _helper(curr_str[:curr_ix]) + _helper(curr_str[curr_ix + 1:]) 
    return _helper(s)


def findEncryptedWord_short(s):
    if len(s) == 0:
        return ''
    l, r = 0, len(s) - 1
    m = l + (r - l) // 2
    return s[m] + findEncryptedWord_short(s[:m]) + findEncryptedWord_short(s[m + 1:])

if __name__ == '__main__':   
    print(findEncryptedWord('abc'))
    print(findEncryptedWord_short('abc'))