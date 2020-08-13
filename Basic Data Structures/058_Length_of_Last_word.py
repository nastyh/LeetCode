def lengthOfLastWord(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    res = s.split(' ')

    if res[-1] == '':
        return 1
    else:
        return len(res[-1])

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