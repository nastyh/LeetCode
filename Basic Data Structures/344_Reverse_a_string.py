def reverseList(s):
    if len(s) == 0: return []
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s

def reverseList_recur(s):
    if len(s) == 0: return ''
    return s[-1] + reverseList_recur(s[:-1])

if __name__ == '__main__':
    print(reverseList(['h','e','l','l','o']))
    print(reverseList_recur(['h','e','l','l','o']))
