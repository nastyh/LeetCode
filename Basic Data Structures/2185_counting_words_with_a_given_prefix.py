from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        O(nm), lenghts of words * len(pref)
        O(1)
        pref_ix iterates over pref again and again for each word
        If there is no match, break and move to another word
        If there is match, keep moving 
        the logic here is a bit non-obv. Imagine prefix is "abc"
        while loop runs till pref_ix < 3
        So pref_ix is 0 (a), 1 (b), 2 (c)
        But after it became 2, it will still get git hit by pref_ix += 1
        so it becomes 3, and it's == len(pref), so we build the answer
        """
        res = 0
        pref_ix = 0
        for word in words:
            if len(pref) > len(word): continue # potential edge case
            while pref_ix < len(pref):
                if pref[pref_ix] != word[pref_ix]:
                    break
                else:
                    pref_ix += 1
                if pref_ix == len(pref): res += 1
            pref_ix = 0 # restart for the next word 
        return res

    def prefixCount_pythonic(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if word.startswith(pref):
                res += 1
        return res 
    
    def prefixCount_one_liner(self, words: List[str], pref: str) -> int:
        return sum(1 for w in words if w.startswith(pref))
    
    def prefixCount_trie(self, words: List[str], pref: str) -> int:
        """
        O(n*l+m), words * max length of anything in words + pref
        O(n*l) for the size structure of the trie
        """
        trie = self._Trie()

        # Add all words to trie
        for word in words:
            trie._add_word(word)
        return trie._count_prefix(pref)

    class _Trie:
        # Node class represents each character in Trie
        class _Node:
            def __init__(self):
                # Links to child nodes
                self.links = [None] * 26
                # Number of strings having prefix till this node
                self.count = 0

        def __init__(self):
            self.root = self._Node()

        # Add word to trie and update prefix counts
        def _add_word(self, word: str) -> None:
            curr = self.root
            for c in word:
                idx = ord(c) - ord("a")
                if curr.links[idx] is None:
                    curr.links[idx] = self._Node()
                curr = curr.links[idx]
                curr.count += 1  # Increment count for this prefix

        # Return count of strings having pref as prefix
        def _count_prefix(self, pref: str) -> int:
            curr = self.root
            for c in pref:
                idx = ord(c) - ord("a")
                if curr.links[idx] is None:
                    return 0  # Prefix not found
                curr = curr.links[idx]
            return curr.count  # Return count at last node