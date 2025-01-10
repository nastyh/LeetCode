from collections import Counter
def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    """
    O(mk + nl), m num of words in words2, k ave length of those
    n num of words in words1, l ave length of those
    we go over each word in words1. If there is a character that also exists
    in any of words2, then this character's count should be >= of the respective 
    count from the merged dictionary created from words2.
    What is the merged dictionary?
    It's the max count of each character that are used in all words in words2.
    Thus, first, create this aggressive/merged dict.
    Then iterate over words in words1. If there is a char that doesn't exist in the merged dict,
    it's ok. If there is a match, the count should be >=
    """
    max_w2_d = Counter()
    res = []
    for word in words2:
        curr_d = Counter(word)
        for k, v in curr_d.items():
            max_w2_d[k] = max(max_w2_d[k], v) # each char: max count word by word
    for word in words1:
        curr_d = Counter(word)
        if all(curr_d[ch] >= count for ch, count in max_w2_d.items()):
            res.append(word)
    return res
def wordSubsets(A, B):  # O(A + B) both
    maxB = Counter()
    for b in B:
        temp = Counter(b)
        for key in temp:
            maxB[key] = max(maxB.get(key, 0), temp[key])
    ans = []
    for a in A:
        # is maxB subset of me?
        temp = Counter(a)
        subset = True
        for key in maxB:
            if key not in temp or (key in temp and temp[key] < maxB[key]):
                subset = False
        if subset:
            ans.append(a)
    return ans  


if __name__ == '__main__':   
    print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
