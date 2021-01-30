import math
def shortestWordDistance(words, word1, word2):  # O(n^2) and O(n)
    """
    Collect indices to two lists.
    Iterate over both lists calculating the abs difference if indices aren't the same
    Allows to solve edge cases such as [a, a], word1 = a, word2 = a. Answer is 1
    Lists are [0, 1] and [0, 1]. We will get the smallest difference of 1 (not zero b/c 0 - 0 won't happen)
    """
    res = math.inf
    w1_list, w2_list = [], []
    for k, v in enumerate(words):
        if v == word1:
            w1_list.append(k)
        if v == word2:
            w2_list.append(k)
    for i in w1_list:
        for j in w2_list:
            if i != j:
                res = min(res, abs(i - j))
    return res


def shortestWordDistance_optimized(words, word1, word2):
    i = j = -1
    res = math.inf
    for k, v in enumerate(words):
        if v == word1:
            i = k
            if j != -1 and i != j:
                res = min(res, abs(i - j))
        if v == word2:
            j = k
            if i != -1 and i != j:
                res = min(res, abs(i - j))
    return res