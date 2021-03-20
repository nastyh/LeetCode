def largeGroupPositions(s):
    res = []
    l, r = 0, 0
    while r < len(s):
        while r < len(s) and s[l] == s[r]:
            r += 1 
        if r - l >= 3:
            res.append([l, r - 1])
        l = r 
        r += 1
    return res
    

if __name__ == '__main__':
    print(largeGroupPositions('abbxxxxzyy'))
    print(largeGroupPositions(''))
    print(largeGroupPositions('abcdddeeeeaabbbcd'))
    print(largeGroupPositions('aba'))
    