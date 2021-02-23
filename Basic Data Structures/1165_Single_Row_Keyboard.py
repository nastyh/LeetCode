def calculateTime(keyboard, word):  # O(n) and O(k) where n is the length of word and k is the length of keyboard
    """
    Do what is says to do.
    At the end, do res += d[word[0]] b/c we start from zero and need to include a jump from zero to the first character
    """
    d = {}
    for k, v in enumerate(keyboard):
        d[v] = k
    res = 0
    for ch_ix in range(1, len(word)):
        res += abs(d[word[ch_ix]] - d[word[ch_ix - 1]])
    res += d[word[0]]
    return res