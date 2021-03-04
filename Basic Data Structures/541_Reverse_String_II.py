def reverseStr(s, k):  # O(N) both
    new_str = ''
    for i in range(len(s)//k + 1)):
        if i % 2 == 1:
            # the second k of 2k which keep original order
            new_str +=  s[k*i:k*(i+1)]
        else:
            # the first k of 2k which will use reverse order
            if i > 0:
                new_str += s[(k * (i + 1) - 1):(k * i - 1):-1]
            else:
                new_str += s[k-1::-1]
    return new_str


def reverseStr_recur(s, k):
    if len(s) < k: return s[::-1]
    if len(s) < 2 * k: return (s[:k][::-1] + s[k:])
    return s[:k][::-1] + s[k:2*k] + reverseStr_recur(s[2*k:], k)


def reverseStr(s, k):
    letters = list(s)
    for i in range(0, len(letters), 2 * k):
        letters[i:i + k] = reversed(a[i:i + k])
    return "".join(letters)