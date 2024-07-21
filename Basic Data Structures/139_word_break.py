class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
        Output: 0
        Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
        """
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        # fill out from the back
        for i in range(len(s) -1, -1, -1):
            # assess each word
            for w in wordDict:
                # if there are enough elements to work with and everything before has already matched
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:  # means the word w from wordDict is found
                    break
        return dp[0]

    def wordBreak_deque(self, s: str, wordDict: List[str]) -> bool:
        """
        O(n^3 + m * k), n == len(s), m = len(wordDict), k -- av length of a word in the dict
        n nodes, iterate over the nodes in front of the current one, create a substring that costs O(n)
        O(n + m * k). n for the deque and for ix_false. O(m * k) for word_set

        Starting and ending indices go through the string s and build up
        a substring that, hopefully, will look like one of the words in the dict
        keep track of indices from which a substring starts but we already know that 
        this substring won't become True (i.e. a word from the dict cannot be formed from this position)
        """
        word_set = set(wordDict)
        q = deque()
        ix_false = set() # this keeps track of the indexes that have False as an answer
        q.append(0)
        ix_false.add(0)
        while q:
            st_ix = q.popleft()
            if st_ix == len(s):
                return True
            for end_ix in range(st_ix + 1, len(s) + 1):
                if end_ix in ix_false:
                    continue
                if s[st_ix:end_ix] in word_set:
                    q.append(end_ix) # pushing repetitive starting indexes: substrings from here are False
                    ix_false.add(end_ix)        
        return False

    
    def wordBreak_bottoms_up(self, s: str, wordDict: List[str]) -> bool:
        """
        O(nmk), len(s), len(dict), average word length
        O(n) to create a dp and another for a set

        dp[start_ix] shows whether there is a word created up to this index (inclusive)
        dp[end_index] is whether we created adjacent words up to this index
        """
        word_dict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for end_index in range(1, len(s) + 1):
            for start_index in range(end_index):
                if dp[start_index] is True and s[start_index:end_index] in word_dict:
                    dp[end_index] = True # adjacent words up to end_index
                    break
        return dp[-1] # reached the end of s with adjacent words 
    
    def wordBreak_recursion(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        @cache # wrapper to cache what's been calculated already
		def _helper(st_ix):
            if st_ix == len(s):
                return True
            for end_ix in range(st_ix + 1, len(s) + 1):
                candidate = s[st_ix:end_ix]
                if candidate in word_set and _helper(end_ix):
                    return True
            return False
        return _helper(0)