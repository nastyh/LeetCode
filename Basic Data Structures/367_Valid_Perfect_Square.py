import math
def isPerfectSquare(num):
    if num < 2: return True
    l, r = 2, num // 2
    while l <= r:
        mid = l + (r - l) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            l = mid + 1
        else:
            r = mid - 1
    return False 


if __name__ == '__main__':
    print(isPerfectSquare(16))       