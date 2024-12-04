def numMatchingSubseq_optimal(self, s: str, words: List[str]) -> int:
    """
    O(n+m)
    O(m), where n is the length of s and m the lengths of all words
    word_d is first_letter: list of words starting with this letter
    while iterating through letters of S, we will move our words through different buckets.
    """
    res, word_d = 0, defaultdict(list)

    for word in words:
        word_d[word[0]].append(word)
        
    for char in s:
        word_list = word_d[char] # take the list of values for a given letter
        word_d[char] = []
            
        for w in word_list: 
            if len(w) == 1:
                res += 1
            else:
                word_d[w[1]].append(w[1:])
           
    return res

def numMatchingSubseq(s, words):
    res = 0
    if len(words) == 0:
        return 0

    def _helper(s, t): # based on Leetcode 392
        s_ix = 0
        if len(s) == 0:
            return True

        for el in t:
            if el == s[s_ix]:
                s_ix += 1
            if s_ix >= len(s):
                return True
        return False



    for word in words:
        if len(word) > len(s):
            continue
        if _helper(word, s):
            res += 1
    return res


if __name__ == '__main__':
    print(numMatchingSubseq('abcde', ["a", "bb", "acd", "ace"]))
