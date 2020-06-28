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



if __name__ == '__main__':
    print(romanToInt('LVIII'))
    print(romanToInt_alt('LVIII'))
    print(romanToInt_prev_curr('IX'))
