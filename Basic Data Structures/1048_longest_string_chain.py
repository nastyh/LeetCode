class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        O(n * len(words)^2) and O(n)
        You are given an array of words where each word consists of lowercase English letters.
        wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA
        without changing the order of the other characters to make it equal to wordB.
        For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
        A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a
        predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
        Return the length of the longest possible word chain with words chosen from the given list of words.
        """
        words.sort(key = lambda x: -len(x)) # from longest to shorters
        word_ix = {} # map word to index 
        for i, w in enumerate(words):
            word_ix[w] = i  # word: index of this word in the input
        dp = {} # index o word: length of the longest chain
        def _helper(i):
            """
            recursive func to be executed the number of words in words
            """
            if i in dp: return dp[i]
            if i > len(words): return 0
            res = 1
            for j in range(len(words[i])): # going through the letters
                w = words[i]
                pred = w[:j] + w[j + 1:] # exclude the letter at index j but take everything else
                if pred in word_ix:
                    res = max(res, 1 + _helper(word_ix[pred])) # length of the chain from the curr ix
            dp[i] = res
            return res 
        for i in range(len(words)): # assess every word
            _helper(i)
        return max(dp.values())
