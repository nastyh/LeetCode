class WordDictionary:
    """
    O(M) for well defined words, M is the key length
    O(N*26^N) for not defined words, n -- number of keys
    Space is O(1) for well defined and O(m) for not defined 
    Trie approach
    go character by character and create a dict inside 
    a dict for each new character. If we saw it already, update.
    $ sign means the end of a word
    """

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node["$"] = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == ".":
                        for x in node:
                            if x != "$" and search_in_node(
                                word[i + 1 :], node[x]
                            ):
                                return True

                    # If no nodes lead to an answer
                    # or the current character != '.'
                    return False
                else:
                    node = node[ch]
            return "$" in node

        return search_in_node(word, self.trie)