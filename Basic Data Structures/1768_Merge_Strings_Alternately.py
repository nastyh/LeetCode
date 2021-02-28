def mergeAlternately(word1, word2):  # O(m + n) both where m and n are lengths
    """
    Linked list approach. Process till the shorter ends.
    Then check if we have anything left.
    """
    res = ''
    i, j = 0, 0
    while i != len(word1) and j != len(word2):
        res += word1[i]
        i += 1
        res += word2[j]
        j += 1
    if i != len(word1):
        res += word1[i:]
    if j != len(word2):
        res += word2[j:]
    return res 