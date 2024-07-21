class TrieNode:
    def __init__(self, par = None):
        #words that can be made by adding given letters to this word
        self.children = {}
        #whether the given word exists in words
        self.exists = 0
        #keeps track of parent node. Used to prune the tree when 
        self.par = par

class Trie:
    def __init__(self):
        self.root = TrieNode()

    #adds a word to the trie
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode(par=node)
            node = node.children[c]
        node.exists = 1
    
    #removes the word from the tree and removes the path to it
    #if the current letter is saved in each node, could optimize node removal
    def remove(self, node):
        node.exists = 0
        #Only prune the trie if there are no other words along that path.
        while (not node.exists) and (not node.children):# and node.par:
            par = node.par
            #O(1); 26 keys maximum in children
            for c in node.par.children:
                if node.par.children[c] == node:
                    node.par.children.pop(c)
                    break
            node = par
        return

    #given a word, returns whether it can be created using words in the array
    #
    def isConcat(self, word):
        #cached dfs using a node in the tree and an index in the word
        @lru_cache(maxsize=None)
        def dfs(i):
            node = self.root
            if i == len(word): return 1
            found = 0
            depth = 0
            while i+depth < len(word) and word[i+depth] in node.children:
                node = node.children[word[i+depth]]
                depth+=1 #depth increases by 1 when node goes to its child
                if node.exists:
                    if depth == len(word):
                        if found: self.remove(node)
                        return found
                    if not found:
                        found |= dfs(i+depth)
                    #^^doesn't break because we still want to remove the word's node
            return found
        return dfs(0)

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        [trie.add(word) for word in words]
        words.sort(key=lambda x: len(x))
        return [word for word in words if trie.isConcat(word)]


# ANOTHER

    def findAllConcatenatedWordsInADict_memo(self, words: List[str]) -> List[str]:
        """
        O(all words' length ^ 2 * O(n))
        O(n)
         Maximum number of words from words that can make up words[i:]
        Iterate through all possible word lengths in dfs(i), upon word match shift i pointer by word length characters.
        For each word if the number of splits is greater than 1 then this word can be broken down into more than one
        words from words list, then we can add it to the result list.
        """
        s = set(words)
        lengths = set(map(len, words))
        @cache
        def dfs(i, word):
            if i == len(word):
                return 0
            splits = -inf
            for length in lengths:
                if word[i:i+length] in s:
                    splits = max(splits, dfs(i+length, word) + 1)
            return splits
        return [word for word in words if dfs(0, word) > 1] 