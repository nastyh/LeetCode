class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        O(n)
        O(1) since the set will have 26 at most 
        palindromes of length 3 look as 
        character; any other/or same char; character as in the first place
        so we need to find an occurance of a char from left, the first occurance of
        the same char from right and put anything in between them 
        """
        letters, res = set(s), 0
        for letter in letters:
            l_ix = s.index(letter)
            r_ix = s.rindex(letter)
            letters_between = set()
            for k in range(l_ix + 1, r_ix):
                letters_between.add(s[k])
            res += len(letters_between)
        return res
    
    def countPalindromicSubsequence_no_index(self, s: str) -> int:
        """
        as above but rewrote the index part
        """
        letters, res = set(s), 0
        for letter in letters:
            # Find the first and last occurrence of the current letter
            l_ix = -1
            r_ix = -1
            for i, char in enumerate(s):
                if char == letter:
                    if l_ix == -1:
                        l_ix = i  # First occurrence
                    r_ix = i  # Keep updating with the last occurrence
            
            if r_ix > l_ix + 1:  # Ensure there is a range to count letters between
                letters_between = set()
                for k in range(l_ix + 1, r_ix):
                    letters_between.add(s[k])
                res += len(letters_between) 
        return res