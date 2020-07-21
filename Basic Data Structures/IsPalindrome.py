def isPal(s):
    if len(s) <= 1: return True
    return s == s[::-1]

def isPal_recurs(s):
    if len(s) <= 1: return True
    if s[0] != s[-1]: 
        return False
    return isPal_recurs(s[1:-1]) # all but the first and the last element. Recursive call


if __name__ == '__main__':
    print(isPal('a'))
    print(isPal('rotor'))
    print(isPal('motor'))
    print(isPal_recurs('a'))
    print(isPal_recurs('rotor'))
    print(isPal_recurs('motor'))