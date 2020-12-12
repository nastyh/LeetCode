def decimalToBinary(testVariable):
    """"
    straigtforward: keep dividing by 2 until it's zero and save the result of % 2 in a string
    Return the string in an opposite order
    """"
    if testVariable == 0: return '0'
    res = ''
    while testVariable > 0:
        res += str(testVariable % 2)
        testVariable = testVariable // 2
    return res[::-1]


def decimalToBinary_recursive(testVariable):
    """
    Recursive implementation:
    Base case when it's 1. Then just add 1 to the string res and return
    Otherwise, divide by 2 and add the result of n % 2 to the string res.
    Return the string in an opposite order
    """
    if testVariable == 0: return '0'
    def _helper(n, res):
        if n == 1:
        res += str(1)
        return res
        return _helper(n // 2, res + str(n % 2))
    ans = _helper(testVariable, '')
    return ans[::-1]