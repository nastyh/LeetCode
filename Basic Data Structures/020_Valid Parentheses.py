# Valid Parentheses. Used pretty much everywhere
def isValid(s):
    op, l = ['(','{','['], []
    if len(s) == 0:   # edge cases
        return True
    if len(s) == 1:   # edge cases
        return False

    def _isMatch(l, r):  # helper function used in the main portion of the code
        if l == '(' and r == ')':
            return True
        if l == '{' and r == '}':
            return True
        if l == '[' and r == ']':
            return True

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
    return len(s) == 0

    # Testing the function

    isValid('(')





