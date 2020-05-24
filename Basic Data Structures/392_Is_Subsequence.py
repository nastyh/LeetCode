def isSubsequence(s, t):
    s_ix = 0
    if len(s) == 0:
        return True

    for el in t:
        if el == s[s_ix]:
            s_ix += 1
        if s_ix >= len(s):
            return True
    return False






    # s_ix = 0
    # for el in t:
    #     if el == s[s_ix]:
    #         s_ix += 1
    # return s_ix == len(s)

    # for el in t:
    #     while s:
    #         if el in s:
    #             s = s[:s.index(el)] + s[s.index(el) + 1:]
    #     return True
    # return False

if __name__ == '__main__':
    # print(isSubsequence('abc','anbgdc'))
    print(isSubsequence('axc','ahbgdc'))

