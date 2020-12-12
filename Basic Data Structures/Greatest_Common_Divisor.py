def gcd_euclid(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd_euclid(n2, n1 % n2)


def gcd_recursive(n1, n2):
    if n1 == n2: 
        return n1
    if n1 > n2:
        return gcd_recursive(n1 - n2, n2)
    else:
        return gcd_recursive(n1, n2 - n1)


if __name__ == '__main__':
    print(gcd_euclid(42, 56))
    print(gcd_recursive(42, 56))