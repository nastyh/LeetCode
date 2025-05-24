from typing import List


class Solution:
    def findWordsContaining_straightforward(self, words: List[str], x: str) -> List[int]:
        """
        O(mn), m the length of the string, n is the length of the array
        O(1) nothing extra to store, res isn't included into the calculation

        Just word by word
        in each word character by character
        if there is a match, save the index, kill the loop for the current word 
        and move on
        """
        res = []
        for i in range(len(words)):
            for ch in words[i]:
                if ch == x:
                    res.append(i)
                    break
        return res
    
    def findWordsContaining_pythonic(self, words: List[str], x: str) -> List[int]:
        """
        O(mn), m the length of the string, n is the length of the array
        O(1) nothing extra to store, res isn't included into the calculation

        in checks each word, if there is a match, it saves the index and moves 
        to the next word
        """
        res = []
        for ix, word in enumerate(words):
            if x in word:
                res.append(ix)
        return res
    
    def findWordsContaining_oneliner(self, words: List[str], x: str) -> List[int]:
        """
        same as above but in one line
        """
        return [i for i, v in enumerate(words) if x in v]