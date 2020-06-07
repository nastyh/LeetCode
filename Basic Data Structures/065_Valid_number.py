import re
def isNumber(s):
        return re.match("^((([-+]?\d+)(\.\d+)?)|([-+]?\.\d+)|([-+]?\d+\.))(e[-+]?\d+)?$", s.strip()) is not None


def isNumber_alt(s):
    valid_chs = ['0','1','2','3','4','5','6','7','8','9','e','.']
    s = s.strip()
    if not s:
        return False
    hasDigit, hasSign, hasPoint, hasE = False, False, False, False
    parts = s.split('e')
    if len(parts) > 2:
        return False

    def valid(ss,hasE=False):
        if not ss:
            return False
        #signs can be only the first character
        if ss[0] in ['+','-']:
            ss = ss[1:]
        hasDigit, hasPoint = False, False
        for i, ch in enumerate(ss):
            if ch not in valid_chs:
                return False
            elif ch.isdigit():
                hasDigit = True
            elif ch == '.':
                if not hasE and not hasPoint:
                    hasPoint = True
                else:
                    return False
        #exclude cases like '+' or '.'; cases like '.3' or '1.' are possible
        return hasDigit
    if len(parts) == 1:
        return valid(parts[0])
    else:
        #treat the second string exceptionally
        return valid(parts[0]) and valid(parts[1],True)

if __name__ == '__main__':
    print(isNumber("0"))
    print(isNumber("e3"))
    print(isNumber("-+3"))
    print(isNumber("53.5e93"))
    print(isNumber_alt("0"))
    print(isNumber_alt("e3"))
    print(isNumber_alt("-+3"))
    print(isNumber_alt("53.5e93"))
