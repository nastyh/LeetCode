class Solution:
    def isPrefixOfWord_pythonic(self, sentence: str, searchWord: str) -> int:
        """
        O(n) both
        split words and save in words
        use the built-in func startswith() to go over the words
        and return the index of the first word where the match is identified 
        Otherwise return -1
        """
        words = [w for w in sentence.split()]
        for w_ix in range(len(words)):
            if words[w_ix].startswith(searchWord):
                return w_ix + 1
        return -1
    
    def isPrefixOfWord_another(self, sentence: str, searchWord: str) -> int:
        """
        Split 
        For each word check that the first search_length chars match those
        from searchWord
        Return immediately 
        """
        words = sentence.split() 
        search_length = len(searchWord)
        for ix, word in enumerate(words):
            if word[:search_length] == searchWord:
                return ix + 1 
        return -1

    def isPrefixOfWord_helper(self, sentence: str, searchWord: str) -> int:
        """
        O(n) both 
        all checks in the helper
        takes two strings: checks that the first letters are the same 
        that the current word is not shorter than the searchWord
        Then just apply the function to every word in sentence 
        """
        words = [w for w in sentence.split()]
        def _helper(a, b):
            if len(a) < len(b): return False 
            if a[0] != b[0]: return False
            for i in range(len(b)):
                if a[i] != b[i]: return False 
            return True 

        words = [w for w in sentence.split()]
        print(f"list of words is {words}")
        for word_ix, word in enumerate(words):
            if _helper(word, searchWord):
                return word_ix + 1
        return -1

    def isPrefixOfWord_one_by_one(self, sentence: str, searchWord: str) -> int:
        """
        O(nm), n number of words in sentence, m is length of searchWord
        O(n) space to create the list words

        Split into the list of words 
        go over this list 
        if a current word's length < searchWord, it isn't good, searchWord cannot be a prefix
        Move to the next candidate in words
        compare char by char. If doesn't match, break
        If it didn't break, means we found a perfect match
        Return the index of the word 
        """
        words = [w for w in sentence.split()] 
        for ix, word in enumerate(words):
            if len(word) < len(searchWord):
                continue 
            for j in range(len(searchWord)):
                if word[j] != searchWord[j]:
                    break 
            else:
                return ix + 1
        return -1




    
