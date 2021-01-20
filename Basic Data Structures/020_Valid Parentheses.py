def isValid_optimal(s):  # O(n) both
    """
    Keep adding brackets till they're opening
    If you see a closing:
    if there is nothing in the stack, return False
    otherwise, check if the last element in the stack and the current element from the same family
    if no, return False
    if yes, pop and proceed
    """
    opening = ['(', '[', '{']
    def _helper(l, r):
        if l == '(' and r == ')':
            return True
        elif l == '[' and r == ']':
            return True
        elif l == '{' and r == '}':
            return True
        else:
            return False 
    if len(s) % 2 == 1: return False
    st = []
    for ch in s:
        if ch in opening:
            st.append(ch)
        else:
            if len(st) == 0:
                return False
            elif _helper(st[-1], ch):
                st.pop()
            else:
                return False
    return len(st) == 0 


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
    print(isValid_optimal('()'))
    print(isValid('()'))
