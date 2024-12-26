class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        O(n) both 
        helper to go over paragraph and get the actual words,
        make them lowercase, and such 
        """
        d = {}
        def _extract(corpus):
            res = []
            current_word = ""
            for char in corpus.lower():
                if char.isalpha():
                    current_word += char
                elif current_word:
                    # non-alphabetic character (like a space, punctuation, etc.) after a sequence of letters.
                    res.append(current_word)
                    current_word = "" 
            if current_word: # finished processing but there is something left in current_word 
                res.append(current_word) 
            return res
        all_words = _extract(paragraph)
        banned_set = set(banned)
        d = Counter(w for w in all_words if w not in banned_set) # frequencies if a word isn't banned
        return max(d, key=d.get) # get a key with the max value 
