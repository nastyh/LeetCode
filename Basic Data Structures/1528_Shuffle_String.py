def restoreString(s, indices):  # O(n) both
    """
    Accurately with indices, need to think what goes where 
    """
    res = [None] * len(s)
    for letter_ix in range(len(s)):
        res[indices[letter_ix]] = s[letter_ix]
    return ''.join(res)