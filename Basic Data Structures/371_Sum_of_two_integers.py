def getSum(a, b):
    """
    x^y is the answer without a carry
    (x & y) << 1 is a carry 

    x^y is the answer to x - y without a borrow
    ((~x) & y)  << 1 is a boorw
    """
     x, y = abs(a), abs(b)
    # ensure that abs(a) >= abs(b)
    if x < y:
        return self.getSum(b, a)
    # abs(a) >= abs(b) --> 
    # a determines the sign
    sign = 1 if a > 0 else -1
    if a * b >= 0:
        # sum of two positive integers x + y
        # where x > y
        while y != 0:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
    else:
        # difference of two integers x - y
        # where x > y
        while y != 0:
            answer = x ^ y
            borrow = ((~x) & y) << 1
            x, y = answer, borrow
    return x * sign