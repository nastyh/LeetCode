def reverseWords(s):
    def _rev_word(s, st, end): # helper: reverses the string between elements st and end
        while st < end:
            s[st], s[end] = s[end], s[st]
            st += 1
            end -= 1
        return s

    s.reverse() # reverse the whole string
    res = []
    st_ix, en_ix = 0, 0
    while en_ix < len(s):
        if s[en_ix] == " ": # if we find a space, then  reverse a word preceeding the space
            res.append(_rev_word(s, st_ix, en_ix - 1))
            st_ix = en_ix + 1
        elif en_ix == len(s) - 1: # edge case
            res.append(_rev_word(s, st_ix, en_ix))
        en_ix += 1
    return res[0]


def reverseWords_alt(s):
    s.reverse()
    i, j, k = 0, 0, 0
    while j < len(s):
        while j < len(s) and s[j] != ' ':
            j += 1
        k = j - 1
        while i < k:
            s[i], s[k] = s[k], s[i]
            i += 1
            k -= 1
        j += 1
        i = j
    return s


if __name__ == '__main__':
    print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
    print(reverseWords_alt(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))