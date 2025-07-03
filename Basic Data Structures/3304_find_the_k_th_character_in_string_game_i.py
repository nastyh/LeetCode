class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        O(k) to run k times
        O(k) to build up res to the length of k
        """
        res = 'a'
        while len(res) < k:
            addition = ''.join(chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in res) 
            res += addition
        return res[k-1]
    
    def kthCharacter_recursive(self, k: int) -> str:
        """
        O(k) to process strings
        O(k) for string and O(log(k)) for the recursion stack 
        """
        def _helper(s: str) -> str:
            return ''.join(chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in s)
        
        word = "a"
        if k == 1:
            return "a"
        while len(word) < k:
            word += _helper(word)
        return word[k - 1]