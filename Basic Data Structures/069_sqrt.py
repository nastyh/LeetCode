import math
def mySqrt(x):  # using log 
    if x < 2:
        return x 
    l = int(math.e ** (0.5 * math.log(x)))
    r = l + 1
    return l if r * r > x else r


def mySqrt_alt(x):  # binary search
    if x < 2: 
        return x 
    l, r = 2, x // 2
    while l <= r:
        mid = l + (r - l) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            l = mid + 1
        else:
            r = mid - 1
    return r


if __name__ == '__main__':
    print(mySqrt(16))
    print(mySqrt(4))
    print(mySqrt(8))
    print(mySqrt_alt(4))
    print(mySqrt_alt(8))   