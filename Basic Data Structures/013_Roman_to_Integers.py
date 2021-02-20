def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
    l , res = 0, 0
    if len(s) == 0: return None
    if len(s) == 1: return d[s[0]]

    while l < len(s):
        if l + 1 < len(s) and d[s[l]] < d[s[l + 1]]:
            res -= d[s[l]]
            res += d[s[l + 1]]
            l += 2
            # r += 2
        else:
            res += d[s[l]]
            # res += d[s[r]]
            l += 1
            # r += 1
    return res

def romanToInt_alt(s):
    values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
    total = values.get(s[-1])
    for i in reversed(range(len(s) - 1)):
        if values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total


def romanToInt_prev_curr(s): # easiest to follow
    d = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
    prev, curr, res = 0, 0, 0
    if len(s) == 0: return None
    if len(s) == 1: return d[s[0]]

    for ix in range(len(s)):
        curr = d[s[ix]]
        if curr > prev:
            res = res - 2 * prev + curr
        else:
            res = res + curr
        prev = curr
    return res


def romanToInt_left_to_right(s):  # O(1) both b/c the dictionary is small and there is a finite number of roman numerals. Max number that can be written is 3999
    """
    Start iterating and every time if we have more or two digits to process left and the left digit < next digit:
    add right, subtract left and make two steps for the pointer (b/c we processed two digits)
    else: just add the number as it is and make one step
    """
    d = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    i = 0 
    while i < len(s):
        if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
            res = res + d[s[i + 1]] - d[s[i]]
            i += 2
        else:
            res += d[s[i]]
            i += 1
    return res


def romanToInt_right_to_left(s):
    """
    Same as above but right to left 
    """
    d = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    i = len(s) - 1
    while i >= 0:
        if i > 0 and d[s[i]] > d[s[i - 1]]:  # while we have at least two elements to process left and this condition holds true
            res = res + d[s[i]] - d[s[i - 1]]
            i -= 2
        else:
            res += d[s[i]]
            i -= 1
    return res 


if __name__ == '__main__':
    print(romanToInt('LVIII'))
    print(romanToInt_alt('LVIII'))
    print(romanToInt_prev_curr('IX'))
    print(romanToInt_left_to_right('LVIII'))
    print(romanToInt_left_to_right('LVII'))
    print(romanToInt_left_to_right('IX'))
    print(romanToInt_right_to_left('LVIII'))
    print(romanToInt_right_to_left('LVII'))
    print(romanToInt_right_to_left('IX'))
    print(romanToInt_right_to_left("MCDLXXVI"))
