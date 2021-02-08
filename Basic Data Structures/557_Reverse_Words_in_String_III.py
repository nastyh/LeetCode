def reverseWords(s):  # O(n) both
    """
    Using built-in functions:
    split by whitespace, get a list with strings
    join these reversed strings into a result
    """
    working = s.split(' ')
    return ' '.join([i[::-1] for i in working])


def reverseWords_manual(s):  # O(n) both
    """
    Can do it manually. A bunch of edge cases, though
    Have two pointers. Move r. If it's a letter, keep moving.
    If it's a space, then we need to handle the word.
    Take a chunk from the l-th index to the r-th index (will include a space), reverse and append to res
    Move r and l. (now they both point to the next element after a whitespace)
    After the loop ends, we haven't added the last word. l points to the first letter of the last word,
    r point to the last letter.
    Need to manually add a space and the reversed word
    When returning res, the first element is space, skip it. 
    """
    res = ''
    l, r = 0, 0
    while r < len(s):
        if s[r] != ' ':
            r += 1
        elif s[r] == ' ':
            res += s[l:r + 1][::-1]
            r += 1
            l = r
    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]