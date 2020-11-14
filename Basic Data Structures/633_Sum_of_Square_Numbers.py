import math
def judgeSquareSum(c):  # brute force. Times out but works
    for a in range(int(math.sqrt(c)) + 1):
        for b in range(int(math.sqrt(c)) + 1) :
            if a**2 + b**2 == c:
                return True
    return False


def judgeSquareSum_bin_search(c):
    left, right = 0, int(math.sqrt(c))
    while left <= right:
        if left ** 2 + right ** 2 > c:
            right -= 1
        elif left ** 2 + right ** 2 < c:
            left += 1
        else:
            return True
    return False


def judgeSquareSum_another(c):
    if c == 0:
        return True
    for i in range(1, int(math.sqrt(c) + 1)):
        j = c - i ** 2
        if math.sqrt(j) == int(math.sqrt(j)):
        # if int(math.sqrt(j)) ** 2 == j:
            return True
    return False


if __name__ == '__main__':
    print(judgeSquareSum(3))
    print(judgeSquareSum_bin_search(3))
    print(judgeSquareSum_another(5))