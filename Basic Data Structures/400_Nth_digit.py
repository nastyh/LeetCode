def findNthDigit(n):
    s, d = 0, 0
    while s < n:
        s += (d + 1) * 9 * 10**d
        d += 1
    n -= s - d * 9 * 10**(d - 1)
    r, s = n % d, 10**(d - 1) + n // d
    return str(s)[r-1] if r > 0 else str(s-1)[-1]