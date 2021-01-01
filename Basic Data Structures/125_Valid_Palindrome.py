def isPalindrome(s):
    if len(s) == 0:
        return True

    s = s.lower()
    q = ''.join([c for c in s if c.isalpha() or c.isdigit()])

    l, r = 0, len(q) - 1
    while l < r:
        if q[l] != q[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


def isPalindrome_no_space(s):  # O(n) and O(1)
    if len(s) == 0:
        return True
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True


def isPalindrome_no_space_alt(s):  # O(n) and O(1)
    if len(s) == 0:
        return True
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalpha() and not s[l].isdigit():
            l += 1
        elif not s[r].isalpha() and not s[r].isdigit():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True


if __name__ == '__main__':
    print(isPalindrome('@dfb564*#'))
    print(isPalindrome_no_space('@dfb564*#'))
    print(isPalindrome_no_space_alt('@dfb564*#'))
    print(isPalindrome_no_space_alt('A man, a plan, a canal: Panama'))
    print(isPalindrome_no_space_alt('race a car'))


# "A man, a plan, a canal: Panama"     race a car


