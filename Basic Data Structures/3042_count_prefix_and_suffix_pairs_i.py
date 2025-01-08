class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Pythonic
        O(n^2)
        O(1)
        l and r pointers, r is always to the right 
        important to have the line w/ continues for cases like "aa" and "cbdw" to keep looking
        They want the left candidate be both the prefix and the suffix, thus, 
        .startswith() and .endswith()
        """
        res = 0
        if len(words) == 0: return 0
        l, r = 0, 1
        while l < len(words) - 1:
            left_candidate = words[l]
            for r in range(l+1, len(words)):
                right_candidate = words[r]
                if len(left_candidate) > len(right_candidate): continue
                if right_candidate.startswith(left_candidate) and right_candidate.endswith(left_candidate):
                    res += 1
            l += 1
        return res

    ## TRIE


from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True
    
    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Solution:
    """
    O(n*m^2 + n^2 * m), where n is the num of words and m is the ave length
    each word O(m^2) to build the suffix trie
    O(m) for quering the pair-suffix match

    Space
    O(n*m^2)
    for all the suffixes: n words w/ the length of m 
    """
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)
        count = 0
        suffix_tries = [Trie() for _ in words]  # Create a suffix trie for each word

        count = 0
        suffix_tries = [Trie() for _ in words]  # Create a suffix trie for each word
        
        # Build suffix tries
        for i, word in enumerate(words):
            reversed_word = word[::-1]
            for j in range(len(reversed_word)):
                suffix_tries[i].insert(reversed_word[j:])  # Insert all suffixes

        # Check each pair (i, j) where i < j
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

    

        return count
