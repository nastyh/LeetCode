def myAtoi(s): # Leetcode's edge cases are weird
    if len(s) == 0:
        return 0
    if s[0].isalpha():
        return 0

    s_stripped = s.strip()
    digits = ''
    digits = ''.join([str(i) for i in s_stripped if i.isdigit()])
    res = int(digits)
    int_min, int_max = -2147483648, 2147483647
    if res <= -2**31:
        return -2**31
    if res >= 2**31 - 1:
        return 2**31 - 1
    return -1 * res if s_stripped[0] == '-' else res

def myAtoi_alt(str):
    index = 0
    if len(str) == 0:
        return 0
    while index != len(str) and str[index] == ' ':
        index+=1
    if index == len(str):
        return 0

    negative = False
    #see if we have a sign
    if str[index] == '+':
        index+=1
    elif str[index] == '-':
        negative = True
        index+=1


    #now we check the rest of the string for numbers
    res = ''
    while index < len(str):
        if str[index] >= '0' and str[index] <= '9':
            res+=str[index]
        else:
            break
        index+=1

    if res is not '':
        integer = int(res)
        if negative is True:
            integer = 0-integer
    else:
        return 0

    if integer < 2**31-1 and integer > -2**31 :
        return integer
    elif integer >= 2*31-1:
        return 2**31-1
    elif integer <= -2**31:
        return -2**31




if __name__ == '__main__':
    print(myAtoi('-91283472332'))
    # print(myAtoi_alt('-91283472332'))
