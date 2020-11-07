def findNumbers(nums):
    """
    Pythonic
    go elemement by element, turn each into string, calculate string's length
    If it's even, increment the counter res
    """
    res = 0
    for num in nums:
        curr_res = 0
        curr_res = len(str(num))
        if curr_res % 2 == 0:
            res += 1
    return res 


def findNumbers_math(nums):
    res = 0
    for num in nums:
        curr_res = 0
        while num > 0:
            num = num // 10
            curr_res += 1
        if curr_res % 2 == 0:
            res += 1
    return res


if __name__ == '__main__':
    print(findNumbers([12, 345, 2, 6, 7896]))
    print(findNumbers([555, 901, 482, 1771]))
    print(findNumbers_math([12, 345, 2, 6, 7896]))
    print(findNumbers_math([555, 901, 482, 1771]))

        