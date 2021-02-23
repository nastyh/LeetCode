 def divide(dividend, divisor):
    if dividend == 0:
        return 0
    sign = 1
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        val, n = divisor, 1
        while val + val <= dividend:
            val += val
            n += n
        res += n
        dividend -= val
    if sign == 1:
        return min(res, 2**31 - 1)
    else: 
        return max(-res, -2**31)


def divide_alt(dividend, divisor):
    def divide_helper(dividend, divisor):
    # edge case so we don't divide a smaller number by a larger one
        if divisor < dividend:
            return 0
        quotient = 1
        sums = divisor
        # python doesn't have fixed int numbers so we ensure we don't bottom out
        # since we're working in negatives, we need to make sure our sums of negatives will not overflow
        # eg: self.min = -20 , sums = -11, -11 + -11 = -22 which overflows
        while (sums + sums > self.min) and (sums + sums > dividend):
            sums +=  sums
            quotient += quotient
        return quotient + divide_helper(dividend - sums, divisor)  # looking for next divisible part
    self.min = -2147483648
    if dividend == self.min and divisor == -1:
        return 2147483647
    # we store the sign so we can return the proper number in the end
    # since we're working entirely in negatives (see bloe)
    sign = (dividend < 0) == (divisor < 0)
    # we need to work in negatives because abs will not work for min_int
    # eg: abs(-2147483648) is out of the range of 2147483647 - -2147483648
    # to avoid this we work entirely in negatives
    if dividend > 0:
        dividend = -dividend
    if divisor > 0:
        divisor = -divisor
    res = divide_helper(dividend, divisor)
    return res if sign else -res
    

from math import log10
def divide_log(D, d):
    D, d, s, t = abs(D), abs(d), (D > 0)-(D < 0), (d > 0)-(d < 0)
    if D < d: return 0
    a = int(round(10**(log10(D) - log10(d)),3))
    return min(a,2**31 - 1) if s > 0 and t > 0 or s < 0 and t < 0 else max(0 - a, 0 - 2**31)