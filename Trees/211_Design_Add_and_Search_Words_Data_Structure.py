class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.isWord=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_word(word, node):
            for i, letter in enumerate(word):
                if letter not in node.children:
                    if letter == ".":
                        for each_node in node.children:
                            if  search_word(word[i + 1:], node.children[each_node]):
                                return True
                    return False
                else:       
                    node = node.children[letter]
            return node.isWord
        node = self.root
        return search_word(word, node)