def isStrobogrammatic(num):
    if len(num) == 0:
        return True
    if any(int(i) in [2, 3, 4, 5, 7] for i in num):
        return False
    if len(num) == 1:
        if int(num[0]) in [2, 3, 4, 5, 6, 7, 9]:
            return False
        else:
            return True
    d = {0: 0, 1: 1, 6: 9, 9: 6, 8: 8}
    l, r = 0, len(num) - 1
    while l < r:
        if d[int(num[l])] != int(num[r]):
            return False
        else:
            l += 1
            r -= 1
    return True


if __name__ == '__main__':
    print(isStrobogrammatic('69'))
    print(isStrobogrammatic('88'))
    print(isStrobogrammatic('962'))
    print(isStrobogrammatic('1'))
    print(isStrobogrammatic('18'))
    print(isStrobogrammatic('60809'))
    
        
        