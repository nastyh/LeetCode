Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):  # O(NK^2 + QK) where N is the number of words, K is the max length of a word and Q is the # of queries. Space O(NK^2)
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            cur = self.trie
            cur[WEIGHT] = weight
            for i, x in enumerate(word):
                #Put all prefixes and suffixes
                tmp = cur
                for letter in word[i:]:
                    tmp = tmp[letter, None]
                    tmp[WEIGHT] = weight

                tmp = cur
                for letter in word[:-i or None][::-1]:
                    tmp = tmp[None, letter]
                    tmp[WEIGHT] = weight

                #Advance letters
                cur = cur[x, word[~i]]
                cur[WEIGHT] = weight

    def search(self, prefix, suffix):
        cur = self.trie
        for a, b in map(None, prefix, suffix[::-1]):
            if (a, b) not in cur: return -1
            cur = cur[a, b]
        return cur[WEIGHT]



import collections
Trie = lambda: collections.defaultdict(Trie)

class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                node = self.trie
                node['weight'] = weight
                word_to_insert = word[i:]+'#'+word
                for c in word_to_insert:
                    node = node[c]
                    node['weight'] = weight
    
    def f(self, prefix, suffix):
        node = self.trie
        for c in suffix + '#' + prefix:
            if c not in node: return -1
            node = node[c]
        return node['weight']