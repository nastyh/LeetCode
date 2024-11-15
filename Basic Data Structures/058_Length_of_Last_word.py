def lengthOfLastWord(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    res = s.split(' ')

    if res[-1] == '':
        return 1
    else:
        return len(res[-1])

def lengthOfLastWord_pointer(s):
    """
    O(n) and O(1)
    start from the right
    if we haven't seen any letters (res = 0), it means there are spaces.
    Keep moving to the left.
    Otherwise, increment res and keep moving to the left
    The tricky thing is to stop once we processed the last word.
    It means that res is not 0 anymore and we just hit a space. Then break it
    """
    r = len(s) - 1
    res = 0
    while r >= 0:
        if res == 0:
            if s[r] == ' ':
                r -= 1
            else:
                res += 1
                r -= 1
        else:
            if s[r] != ' ':
                res += 1
                r -= 1
            else:
                break
    return res

def lengthOfLastWord_alt(s):
    s = s.strip()
    if len(s) == 0: return 0
    res = ''
    for ch in s[::-1]:
        if ch != ' ':
            res += ch
        else:
            break
    return len(res)

if __name__ == '__main__':
    print(lengthOfLastWord('Hello World'))
    print(lengthOfLastWord_alt('Hello World'))
