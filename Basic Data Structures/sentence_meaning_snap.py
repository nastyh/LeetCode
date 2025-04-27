"""
Your are assigned to support the following feature:

Given two sentences and one group of synonyms, decide if the two sentence share the same meaning.

For example
sent1 = "the photo is pretty"
sent2 = "the image is beautiful"
sent3 = "that photo is pretty"
groups_of_syns = [["photo", "image"], ["pretty", "amazing", "nice"], ["nice", "good-looking"], ["good-looking", "beautiful"]]

Should return True for sent1 and sent2, Should return False for sent1 and sent3
"""
from typing import List

"""
Normalize and split each sentence into words.
Build a Union–Find (Disjoint Set) structure over all words in your synonym groups,
so that any two words in the same connected component are considered interchangeable.
Compare the two word lists position by position: for each pair (w1, w2),
accept if w1 == w2 or find(w1) == find(w2); otherwise the sentences differ in meaning.

Building the Union–Find
We do one union per synonym (group size k → k–1 unions) 
Each union/find is effectively O(α(N)), where α is the inverse Ackermann function (practically constant).
Let S = total number of distinct synonym entries; this step is O(S · α(S)).

Comparing the sentences
Splitting and lowercasing is O(L), where L is total number of characters.
Then for each of M word positions we do up to two find calls: overall O(M · α(S+M)).

Space
O(S + M) to store the union‐find parent pointers and the word lists.
This is linear‐time (essentially) in the size of your input, and uses only a small extra hash map for the DSU.
"""

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x: str) -> str:
        # path compression
        if x not in self.parent:
            self.parent[x] = x
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: str, b: str):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa

def sentences_equivalent(
    sent1: str,
    sent2: str,
    groups_of_syns: List[List[str]]
) -> bool:
    # 1. Tokenize (here we assume simple whitespace-split & lowercase)
    words1 = sent1.lower().split()
    words2 = sent2.lower().split()
    if len(words1) != len(words2):
        return False

    # 2. Build DSU over all synonyms
    uf = UnionFind()
    for group in groups_of_syns:
        # union every word in the group with the first one
        first = group[0].lower()
        for w in group[1:]:
            uf.union(first, w.lower())

    # 3. Compare position by position
    for w1, w2 in zip(words1, words2):
        if w1 == w2:
            continue
        # if neither word seen in UF, find() will initialize them to be their own parent
        if uf.find(w1) != uf.find(w2):
            return False

    return True

# Example usage
if __name__ == "__main__":
    sent1 = "the photo is pretty"
    sent2 = "the image is beautiful"
    sent3 = "that photo is pretty"
    groups = [
        ["photo", "image"],
        ["pretty", "amazing", "nice"],
        ["nice", "good-looking"],
        ["good-looking", "beautiful"],
    ]

    print(sentences_equivalent(sent1, sent2, groups))  # True
    print(sentences_equivalent(sent1, sent3, groups))  # False
