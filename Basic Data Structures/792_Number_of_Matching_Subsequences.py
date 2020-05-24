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
