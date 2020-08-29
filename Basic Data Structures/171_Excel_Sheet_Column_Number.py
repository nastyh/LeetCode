def titleToNumber(s):
    res = 0
    val = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d = dict(zip(letters, val))
    for ch in s:
        # rem = d[ch]
        # res = rem + res * 26
        res = res * 26 + d[ch]
    return res

def titleToNumber_recur(s):
    val = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d = dict(zip(letters, val))
    def _helper(s, res, d):
        if not s: return res
        res = res * 26 + d[s[0]]
        return _helper(s[1:], res, d)
    return _helper(s, 0, d)


def str2num(s):  # the same approach as to "string to number"
    res = 0
    for digit in s:
        res = res * 10 + int(digit)
    return res


def str2num_recursively(s):  # string to number recursively
    def _helper(s, res):
        if not s: return res
        res = res * 10 + int(s[0])
        # return _helper(s[1:], res * 10 + int(s[0]))
        return _helper(s[1:], res)
    return _helper(s, 0)
       

if __name__ == '__main__':
    print(titleToNumber('ZY'))
    print(titleToNumber_recur('ZY'))
    # print(str2num('123'))
    # print(str2num('66'))
    # print(str2num_recursively('67'))