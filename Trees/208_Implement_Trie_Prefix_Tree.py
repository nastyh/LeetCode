class Trie(object):

    def __init__(self):
        self.head = {}

    def insert(self, word):  # O(m) both, where m is the key length       
        """
        Iterate over a word. If it's a new letter, add it to the dictionary, as its value create a new dictionary
        If this is an already existing letter, make current this letter's value (in the dictionary)
        Finally, add an asterix as a value to show that it's the word's end
        """
        current = self.head
        for character in word:
            if character not in current:
                current[character] = {}
            current = current[character]
        current['*'] = True            # '*' marks the end of word
        
    def search(self, word):  # O(m) and O(1)
        """
        Iterate over a word. If at any moment, a character doesn't exist in a current dictionary, return False
        If we arrived to an asterix, then the word is present, return True
        Finally return False, b/c you're looking for a word, not part of the word
        """
        current = self.head
        for character in word:
            if character not in current:
                return False
            current = current[character]
        if '*' in current:
            return True
        return False
        
    def startsWith(self, prefix):  # O(m) and O(1)
        """
        Exactly as above but without the last return False
        """
        current = self.head
        for character in prefix:
            if character not in current:
                return False
            current = current[character]
        return True
        

class Trie_another:
    """
    More classical implementation
    """
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26

    def insert(self, word):
        curr = self
        for w in word:
            if curr.children[ord(w) - ord('a')]  == None:  # if the letter isn't present, create an instance for it
                curr.children[ord(w) - ord('a')] = Trie_another()
            curr = curr.children[ord(w) - ord('a')]  # step into this letter
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