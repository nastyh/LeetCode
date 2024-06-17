"""
If we put all the sentences in a trie, we can walk through every sentence simultaneously with each call to input.

We will use a TrieNode class to represent the trie nodes. The AutocompleteSystem class will be initialized with a TrieNode root.
At each trie node, we have a hash map. This hash map holds all the sentences that have the current path as a prefix.
Because we need to return the sentences that have been typed the most, we need to map each sentence to its count.


Given nnn as the length of sentences, kkk as the average length of all sentences, and mmm as the number of times input is called,

Time complexity: O(n * k + m * (n + m/k) * log (n + m/k))
We initialize the trie, which costs O(n⋅k)O(n \cdot k)O(n⋅k) as we iterate over each character in each sentence.
​Space complexity: O(k⋅(n⋅k+m))O(k \cdot (n \cdot k + m))O(k⋅(n⋅k+m))
The worst-case scenario for the trie size is when no two sentences share any prefix. The trie will initially have a size of n⋅kn \cdot kn⋅k. Then, each call to input would create a new node.

Each of these trie nodes has children and sentences hash maps. The size of children is limited to 26, so we will ignore it.
The size of sentences is variable, but in the case described, each node will only have 1 entry (because no two sentences share any prefix,
so no trie node is visited by more than one sentence). This 1 entry will have a size of O(k)O(k)O(k).
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
            
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            curr_sentence = "".join(self.curr_sentence)
            self.add_to_trie(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]
        sentences = self.curr_node.sentences
        sorted_sentences = sorted(sentences.items(), key = lambda x: (-x[1], x[0]))
        
        ans = []
        for i in range(min(3, len(sorted_sentences))):
            ans.append(sorted_sentences[i][0])
        
        return ans

    def add_to_trie(self, sentence, count):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentences[sentence] += count


# WITH HEAP

import heapq

"""
O(n *k + m * (n + m/k))
We initialize the trie, which costs O(n⋅k)O(n \cdot k)O(n⋅k) as we iterate over each character in each sentence.
After we call input m times, we could add m/k new sentences
Heapify gives O(n + m/k)
​
  new sentences.
O(k * (n * k + m))
The worst-case scenario for the trie size is when no two sentences share any prefix.
The trie will initially have a size of n⋅kn \cdot kn⋅k. Then, each call to input would create a new node.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
            
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            curr_sentence = "".join(self.curr_sentence)
            self.add_to_trie(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]
        items = [(val, key) for key, val in self.curr_node.sentences.items()]
        ans = heapq.nsmallest(3, items)
        return [item[1] for item in ans]

    def add_to_trie(self, sentence, count):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentences[sentence] -= count