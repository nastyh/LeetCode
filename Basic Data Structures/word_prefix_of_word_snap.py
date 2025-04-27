"""
https://leetcode.com/discuss/post/5351874/snap-seattle-phone-by-anonymous_user-wtwx/
Given a list of strings find if the word is prefix of any word 

Example:
['world', 'word', 'would', 'wont', 'which', 'hello']
prefix : 'wo'
"""

from typing import List

def has_prefix_brute_force(words: List[str], prefix: str) -> bool:
    """
    O(nk), n is the num of words, k is the length of the prefix
    O(1) nothing to store
    Just Python func
    """
    for w in words:
        if w.startswith(prefix):
            return True
    return False

# TRIE approach

class TrieNode:
    """
    Build time: O(N × L), N = number of words, L = average word length
    Query time: O(k) for prefix length k
    Space: O(total characters in all words)
    """
    __slots__ = ('children', 'is_end')
    
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Build trie
trie = Trie()
for w in words:
    trie.insert(w)

# Query
print(trie.starts_with('wo'))  # True
print(trie.starts_with('ha'))  # False
