import math
def shortestToChar(s, c):  # O(n) both but technically O(3n)
    """
    Brute force like
    Iterate from left to right, if you see c in s, save its index to prev_ix_from_left. Next time, when you see a non c character, calculate
    the difference between its index and prev_ix_from_left and put into the respective spot in from_left
    Iterate from right to left, do the same but this time save the differences in from_right
    Iterate over both lists, choose a smaller value and put into res 
    """
    res = [None] * len(s)
    from_left, from_right = [0] * len(s), [0] * len(s)
    prev_ix_from_left = -math.inf
    for k, v in enumerate(s):
        if v == c:
            prev_ix_from_left = k
        from_left[k] = k - prev_ix_from_left
    prev_ix_from_right = math.inf
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev_ix_from_right = i
        from_right[i] = prev_ix_from_right - i
    # print(from_left)
    # print(from_right)
    for i in range(len(s)):
        res[i] = min(from_left[i], from_right[i])
    return res


def shortestToChar_optimized(s, c):
    """
    Same as above but saving some space by not having from_right 
    """
    res = [None] * len(s)
    prev_ix_from_left = -math.inf
    for k, v in enumerate(s):
        if v == c:
            prev_ix_from_left = k
        res[k] = k - prev_ix_from_left
    prev_ix_from_right = math.inf
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev_ix_from_right = i
        res[i] = min(res[i], prev_ix_from_right - i)
    return res


if __name__ == '__main__':
    # print(shortestToChar('loveleetcode', 'e'))
    # print(shortestToChar('aaab', 'b'))
    print(shortestToChar_optimized('loveleetcode', 'e'))
    print(shortestToChar_optimized('aaab', 'b'))