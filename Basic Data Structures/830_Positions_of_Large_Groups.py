def largeGroupPositions(s):  # O(n) and O(1) (not incl. space for the answer)
    """
    Move r while it matches what is at l. 
    Once the size is large enough, append it to res 
    """
    res = []
    l, r = 0, 1
    while r < len(s):
        while r < len(s) and s[l] == s[r]:
            r += 1 
        if r - l >= 3:
            res.append([l, r - 1])  # be accurate here with r - 1
        r += 1
    return res
    

if __name__ == '__main__':
    print(largeGroupPositions('abbxxxxzyy'))
    print(largeGroupPositions(''))
    print(largeGroupPositions('abcdddeeeeaabbbcd'))
    print(largeGroupPositions('aba'))
    