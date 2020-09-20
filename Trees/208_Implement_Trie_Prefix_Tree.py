class Trie(object):

    def __init__(self):
        self.head = {}
        """
        Initialize your data structure here.
        """
        

    def insert(self, word):        
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.head
        for character in word:
            if character not in current:
                current[character] = {}
            current = current[character]
        current['*'] = True            # '*' marks the end of word
        

    def search(self, word):
        current = self.head
        for character in word:
            if character not in current:
                return False
            current = current[character]
        if '*' in current:
            return True
        return False
		
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        current = self.head
        for character in prefix:
            if character not in current:
                return False
            current = current[character]
        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

class Trie_another:
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26
    

    def insert(self, word):
        curr = self
        for w in word:
            if curr.children[ord(w) - ord('a')]  == None:
                curr.children[ord(w) - ord('a')] = Trie_another()
            curr = curr.children[ord(w) - ord('a')]
        curr.endOfWord = True

    
    def search(self, word):
        curr = self
        for w in word:
            curr = curr.children[ord(w) - ord('a')]
            if not curr:
                return False
            else:
                continue
        if curr.endOfWord:
            return True
        return False 

    
    def startsWith(self, prefix):
        curr = self
        for p in prefix:
            curr = curr.children[ord(p) - ord('a')]
            if not curr:
                return False
            else:
                return True


if __name__ == '__main__':
    t = Trie_another()
    t.insert('apple')
    print(t.search('apple'))
    print(t.search('app'))
    print(t.startsWith('app'))
    t.insert('app')
    print(t.startsWith('app'))