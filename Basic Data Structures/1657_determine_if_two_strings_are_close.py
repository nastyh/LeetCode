class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool: # O(w1 + w2) both 
        # we need to have the same number of unique letters in each word
        # these letters should also have the same counts since it's a 
        # one to one transformation
        w1, w2 = Counter(word1), Counter(word2)
        return set(word1) == set(word2) and Counter(w1.values()) == Counter(w2.values())