from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            # Only add word if we have fewer than 3 suggestions
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
    
    def get_suggestions(self, prefix):
        node = self.root
        result = []
        for ch in prefix:
            if node:
                node = node.children.get(ch)
            if node:
                result.append(node.suggestions)
            else:
                result.append([])
        return result


class Solution:
    def suggestedProducts_search(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        O(n log n + m log n + m²), n -- num of products, m -- length of a search word
        O(n+m), n for sort, m for the output
        using search
        """
    # Sort products lexicographically
        products.sort()
        result = []
        prefix = ""

        def bisect_left_custom(arr, target):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                # If the middle element is less than the target, narrow the search to the right half.
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        for ch in searchWord:
            prefix += ch
            # Find the starting index of products that could match the prefix using our custom binary search
            i = bisect_left_custom(products, prefix)
            suggestions = []
            
            # Check the next three products from index i to see if they match the prefix
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
            result.append(suggestions)
        return result
    
    def suggestedProducts_trie(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        # Build the trie by inserting each product
        for product in products:
            trie.insert(product)
        
        # Generate suggestions for every prefix of searchWord
        return trie.get_suggestions(searchWord)
