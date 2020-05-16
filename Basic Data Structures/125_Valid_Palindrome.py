def isPalindrome(self, s: str) -> bool:
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


if __name__ == '__main__':
    print(isPalindrome('@dfb564*#'))


# "A man, a plan, a canal: Panama"     race a car


