import math
def isPerfectSquare(num):  # O(Log(N)) and O(1)
    """
    Using binary search to make the calculations faster
    """
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


def isPerfectSquare_newton_method(num):  # O(Log(N)) and O(1)
    """
    the question is to find a root of x^2 - num = 0
    The idea of Newton's algorithm is to start from a seed (= initial guess)
    and then to compute a root as a sequence of improved guesses.
    Take num / 2 as a seed.
    While x * x > num, compute the next guess using Newton's method: 1/2 * (x + num / x)
    """
    if num < 2:
        return True
    x = num // 2
    while x * x > num:
        x = (x + num // x) // 2
    return x * x == num


def isPerfectSquare_brute_force(num):  # TLE
    """
    Just iterate element by element. 
    """
    if num < 2: return True
    for candidate in range(1, num // 2 + 1):  # +1 is required to handle cases such as 4
        if candidate * candidate == num:
            return True
    return False


if __name__ == '__main__':
    print(isPerfectSquare(16))       