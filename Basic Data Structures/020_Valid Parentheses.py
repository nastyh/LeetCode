def isValid(s):
    op, l = ['(','{','['], []
    if len(s) == 0:   # edge cases
        return True
    if len(s) == 1:   # edge cases
        return False
    def _isMatch(l, r):  # helper function used in the main portion of the code
        if l == '(' and r == ')':
            return True
        elif l == '{' and r == '}':
            return True
        elif l == '[' and r == ']':
            return True
        else:
            return False
    for el in range(len(s)):
        if s[el] in op:
            l.append(s[el])
        else:
            try:
                p = l.pop()
            except IndexError:
                return False
            if _isMatch(p, s[el]):
                continue
            else:
                return False
    return len(l) == 0


if __name__ == '__main__':
    print(isValid('()'))
