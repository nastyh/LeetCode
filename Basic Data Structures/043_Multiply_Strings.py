def multiply(num1, num2):
    n1, n2 = [], []
    for i in num1:
        n1.append(int(i))
    for j in num2:
        n2.append(int(j))
    return str(sum([v*10**k for k, v in enumerate(n1[::-1])]) * sum([v*10**k for k, v in enumerate(n2[::-1])]))


def multiply_ord(num1, num2):  # O(n) and O(1)
    int_num1 = 0
    for i in num1:
        int_num1 = int_num1 * 10
        int_num1 += (ord(i) - ord('0'))

    int_num2 = 0
    for i in num2:
        int_num2 = int_num2 * 10
        int_num2 += (ord(i) - ord('0'))
    return str(int_num1 * int_num2)


def multiply_one_by_one(num1, num2):
    res = ''
    carry = 0
    if len(num1) < len(num2):
        shorter = num1
        longer  = num2
    else:
        shorter = num2xs
        longer = num1
    # i = len(longer) - 1
    i = max(len(num1), len(num2)) - 1
    while i != 0:
        try:
            digit1 = int(num1[i])
        except IndexError:
            digit1 = 1
        try:
            digit2 = int(num2[i])
        except IndexError:
            digit2 = 1 
        prelim = digit1 * digit2 + carry
        print(prelim)
        res += str(prelim % 10)
        carry = prelim // 10
        i -= 1
    if carry != 0:
        res += str(carry)
    return  res


if __name__ == '__main__':
    print(multiply_ord('2', '3'))
