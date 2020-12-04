def kthFactor(n, k):  # O(n) and O(n)
    """
    Brute force: collect all numbers, don't forget the number itself
    Return the res at the right index
    """
    res = []
    for i in range(1, n //2 + 1):
        if n % i == 0:
            res.append(i)
    res.append(n)
    if len(res) < k:
        return -1
    else:
        return res[k - 1]


def kthFactor_alt(n, k):  # O(n//2) and O(1)
    count, res = 0, -1
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            if count < k:
                res = i
                count += 1
            else:
                break
    if k == count + 1:
        return n
    elif k > count + 1:
        return -1
    else:
        return res


if __name__ == '__main__':
    # print(kthFactor(12, 3))
    # print(kthFactor(7, 2))
    # print(kthFactor(4, 4))
    # print(kthFactor(1, 1))
    # print(kthFactor(1000, 3))
    print(kthFactor_alt(12, 3))
    print(kthFactor_alt(7, 2))
    print(kthFactor_alt(4, 4))
    print(kthFactor_alt(1, 1))
    print(kthFactor_alt(1000, 3))