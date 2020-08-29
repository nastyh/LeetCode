def titleToNumber(s):
    res = 0
    val = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d = dict(zip(letters, val))
    for ch in s:
        rem = d[ch]
        res = rem + res * 26
    return res


if __name__ == '__main__':
    print(titleToNumber('ZY'))