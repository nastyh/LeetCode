class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        O(n) both
        set is for faster access
        split into a list of words 
        iterate over each word and over each letter
        if found a bad letter, decrement res and don't process this word anymore, it's already enough
        """
        broken_s = set(brokenLetters)
        text_clean = text.split(" ")
        res = len(text_clean)
        for word in text_clean:
            for ch in word:
                if res == 0: return res
                if ch in broken_s:
                    res -= 1
                    break 
        return res
