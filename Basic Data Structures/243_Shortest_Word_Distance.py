import math
def shortestDistance(words, word1, word2):
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


if __name__ == '__main__':
    print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice'))
    print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))
    print(shortestDistance(['a', 'a', 'b', 'b'], 'a', 'b'))