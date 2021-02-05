def myAtoi(self, s: str) -> int:
    i = 0
    sign = '+'
    result = 0
    # ignore leading whitespaces
    while i < len(s) and s[i] == ' ':
        i += 1
    # locking for result sign
    if i < len(s) and s[i] in {'-', '+'}:
        sign = s[i]
        i += 1
    # read characters until the next non-digit charcter
    while i < len(s) and s[i].isdigit():
        result *= 10
        result += int(s[i])
        i += 1
    result = result if sign == '+' else result * -1
    int_min_value, int_max_value = (-2 ** 31), (2 ** 31) - 1
    if result < int_min_value:
        return int_min_value
    if int_max_value < result:
        return int_max_value  
    return result


def myAtoi_alt(str):
    index = 0
    if len(str) == 0:
        return 0
    while index != len(str) and str[index] == ' ':
        index += 1
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
    if integer < 2**31 - 1 and integer > -2**31 :
        return integer
    elif integer >= 2*31 - 1:
        return 2**31 - 1
    elif integer <= -2**31:
        return -2**31




if __name__ == '__main__':
    print(myAtoi_alt('-91283472332'))
