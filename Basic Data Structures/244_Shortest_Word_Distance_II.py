from collections import defaultdict
class WordDistance(object):  # O(n) both 
    """
    defaultdict with words and indices at which they appear
    Iterate over two lists (they're both in a sorted order)
    After every calculation of res, make a decision what pointer to move. 
    We move the smaller one b/c it might bring us to even better (closer) result.
    """
    def __init__(self, words):
        self.d=defaultdict(list)
        for i, word in enumerate(words):
            self.d[word].append(i)


    def shortest(self, word1, word2):
        indexes1 = self.d[word1]
        indexes2 = self.d[word2]
        i, j, res = 0, 0, math.inf
        while i < len(indexes1) and j < len(indexes2):
            res = min(res, abs(indexes1[i] - indexes2[j]))
            if indexes1[i] < indexes2[j]:
                i += 1
            else:
                j += 1
        return res