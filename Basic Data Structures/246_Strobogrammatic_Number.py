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


def isStrobogrammatic_dict(num):  # O(n) both. Traverse and build new_num
    d = {'0': '0', '1': '1', '6': '9', '8': '8', '9':'6'}
    new_num = ''
    for n in num:
        if n not in d:
            return False
        else:
            new_num += d[n]
    return num == new_num[::-1]


def isStrobogrammatic_pointers(num):  # O(n) and O(1)
    """
    Have two pointers
    Write down cases for False.
    It's either numbers that aren't in a dictionary or a situation when we cannot turn a number properly
    Keep moving and return True at the end
    """
    d = {'0': '0', '1': '1', '6': '9', '8': '8', '9':'6'}
    l, r = 0, len(num) - 1
    while l <= r:
        if num[l] not in d or num[r] not in d:
            return False 
        if num[r] != d[num[l]] or num[l] != d[num[r]]:
            return False
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
    
        
        