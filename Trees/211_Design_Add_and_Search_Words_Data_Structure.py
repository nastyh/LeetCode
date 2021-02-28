class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:  #O(M) for defined words and O(n*26^M) for the words with a star. Space is O(1) for defined and O(M) for not defined 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(set)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        self.words[(len(word), word[0])].add(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        if word[0] != '.':
            candidates = self.words[(len(word), word[0])]
        else:
            candidates = set()
            for length, c1 in self.words:
                if length == len(word):
                    candidates |= self.words[(length, c1)]  # inpace OR operation for sets
        for w in candidates:
            for i in range(1, len(word)):
                if word[i] not in (w[i], '.'):
                    break
            else:
                return True
        else:
            return False



class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)    

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        
        for letter in word:
            node = node.children[letter]
        
        node.isWord = True

    def search(self, word: str) -> bool:       
        return self.dfs(word, self.root, 0, len(word))
    
    def dfs(self, word: str, node: TrieNode, idx: int, end: int) -> bool:
        if idx >= end:
            if node.isWord:
                return True
            return False
        
        if word[idx] == ".":
            for letter in node.children.values():
                if self.dfs(word, letter, idx + 1, end):
                    return True
        else:
            found = node.children[word[idx]]
            
            if not found:
                return False
            
            if self.dfs(word, found, idx + 1, end):
                return True
        
        return False