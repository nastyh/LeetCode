from math import log
def isPowerOfThree(n):  # O(log3(n)) and O(1)
    """
    Essentially, it's a brute force
    Keep dividing by three. Eventually you should arrive to 1 
    """
    if n < 1: return False
    while n % 3 == 0:
        n //= 3
    return n == 1


def isPowerOfThree_another(n):
    """
    Because n is int, we can just write down all cubes that fit into an int
    """
    power_list = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
    return n in power_list


def isPowerOfThree_log(n):
    """
    Using the property of logs 
    """
    if n < 1: return False
    return round(log(n, 3),9) == round(log(n, 3))