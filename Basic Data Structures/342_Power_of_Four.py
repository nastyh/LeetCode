import math
def isPowerOfFour(num):
    if num <= 0: return False
    if num == 1: return True
    return int(math.log(num, 4)) == math.log(num, 4)


if __name__ == '__main__':
    print(isPowerOfFour(4))
    print(isPowerOfFour(0))
    print(isPowerOfFour(-4))
    print(isPowerOfFour(1))
    print(isPowerOfFour(16))