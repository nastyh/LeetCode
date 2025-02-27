from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        """
        O(len(s)), since strings are immutable, each concatenation can bring it to
        O(len(s)^2)

        O(len(s)) -- to create candidate 
        Build candidate by adding words from words
        if candidate becomes s, we're good 
        """
        candidate = ''
        for word in words:
            candidate += word
            if candidate == s:
                return True 
            if len(candidate) >= len(s): # break if we're over
                break
        return False