from collections import Counter
def findTheDifference(s, t):  # most optimal solution: O(n) and O(1) 
    res = 0
    for ch in s:
        res ^= ord(ch)
    for ch in t:
        res ^= ord(ch)
    return chr(res)
    

def findTheDifference_dict(s, t):  # straightforward but uses extra space
    s_d, t_d = Counter(s), Counter(t)
    for k, v in t_d.items():
        if s_d[k] != t_d[k]:
            return k


def findTheDifference_dict_optimized(s, t):  # slight modification, uses only one dictionary instead of two
    t_d = Counter(t)
    for ch in s:
        if ch in t_d:
            t_d[ch] -= 1
    return [k for (k, v) in t_d.items() if v == 1][0]


def test(s, t):
    res = 0
    for letter in s:
        res ^= ord(letter)
        print(chr(res))
    return chr(res)
    # return 32 ^ 32
    # return 0 ^ ord(s), ord(s), ord(t), ord(s) ^ ord(t), chr((ord(s) ^ ord(t)))


if __name__ == '__main__':
    # print(findTheDifference('abcd', 'abcde'))
    # print(findTheDifference('a', 'aa'))
    # print(findTheDifference_dict('abcd', 'abcde'))
    # print(findTheDifference_dict('a', 'aa'))
    # print(findTheDifference_dict_optimized('abcd', 'abcde'))
    # print(findTheDifference_dict_optimized('a', 'aa'))
    print(test('atb', 'b'))
