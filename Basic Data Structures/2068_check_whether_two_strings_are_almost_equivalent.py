from collections import defaultdict
import string
from typing import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        """
        O(len(word1) + len(word2)) -- need to process both
        O(1) since it's only 26 elements in both dicts
        alphabet is just a list of lowercase english letters
        build two similar dicts where each letter is 1
        then iterate over words and update the dicts
        Letters that aren't present will have a value of 1 but it doesn't matter
        then just compare values for each letter between the dictionaries
        If at any point the difference > 3 --> False
        True at the end 
        """
        alphabet = list(string.ascii_lowercase)
        d_a, d_b = Counter(alphabet), Counter(alphabet)
        for letter in word1:
            d_a[letter] += 1
        for letter in word2:
            d_b[letter] += 1
        for letter in alphabet:
            if abs(d_a[letter] - d_b[letter]) > 3:
                return False
        return True
    
    def checkAlmostEquivalent_get(self, word1: str, word2: str) -> bool:
        """
        As above but looping fewer times 
        """
        d_a, d_b = Counter(word1), Counter(word2)
        alphabet = list(string.ascii_lowercase)
        for letter in alphabet:
            if abs(d_a.get(letter, 0) - d_b.get(letter, 0)) > 3:
                return False
        return True 
    
    def checkAlmostEquivalent_get_another(self, word1: str, word2: str) -> bool:
        """
        As above but even without alphabet 
        """
        d_a, d_b = Counter(word1), Counter(word2)
        for k, v in d_a.items():
            if abs(d_b.get(k, 0) - v) > 3:
                return False 
        for k, v in d_b.items():
            if abs(d_a.get(k, 0) - v) > 3:
                return False 
        return True 
    
    def checkAlmostEquivalent_one_dict(self, word1: str, word2: str) -> bool:
        """
        O(len(word1))
        O(len of both words)
        none of the chars should have a value outside of [-3;3]
        """
        d = defaultdict(int)
        for i in range(len(word1)):
            d[word1[i]] += 1
            d[word2[i]] -= 1 
        return not any(abs(value) > 3 for value in d.values())


