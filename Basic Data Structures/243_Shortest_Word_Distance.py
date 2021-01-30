import math
def shortestDistance(words, word1, word2):  # O(n) and O(1)
    """
    Key here is to initialize ix_1 and ix_2 w/ something weird and only calculate the difference 
    when both words are found
    """
    res = math.inf
    ix_1, ix_2 = math.inf, math.inf
    for k, v in enumerate(words):
        if v not in (word1, word2): continue
        if v == word1:
            ix_1 = k
        elif v == word2:
            ix_2 = k
        if ix_1 != math.inf and ix_2 != math.inf:
            res = min(res, abs(ix_1 - ix_2))
    return res


def shortestDistance_brute_force(words, word1, word2):  # O(n^2) and O(1)
    """
    Collect indices into two lists and then iterate in a double loop over both lists looking for the smallest difference 
    """
    w1_list, w2_list = [],[]
    res = math.inf
    for k, v in enumerate(words):
        if v == word1:
            w1_list.append(k)
        if v == word2:
            w2_list.append(k)
    for i in w1_list:
        for j in w2_list:
            res = min(res, abs(i - j))
    return res 


if __name__ == '__main__':
    print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice'))
    print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))
    print(shortestDistance(['a', 'a', 'b', 'b'], 'a', 'b'))