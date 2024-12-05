class Solution:
    def shortestPalindrome_brute_force(self, s: str) -> str:
        """
        O(n^2) and O(n)
        start from the end of the provided string 
        Check if everything from zero to the current index r is a palindrome 
        if yes, take everything that is to the right from the index r and attach in the beginning
        but turn it with [::-1]
        """
        def _is_pal(inp, l, r):
            while l <= r:
                if inp[l] != inp[r]:
                    return False 
                l += 1
                r -= 1
            return True 
        for r in reversed(range(len(s))):
            if _is_pal(s, 0, r):
                suffix = s[r+1:]
                return suffix[::-1] + s
        return ""
        
    def shortestPalindrome_kmp(self, s: str) -> str:
        """
        O(n) and O(1) ?
        convert strings to integers
        349 is 100^2 + 10^1 + 10^0 (kinda)
        need a base: a -->  1, z --> 26
        aa c e caaa
        11 shift by * 29 
        c = 29^2, a = 29^1, next a = 29^0
        """
        prefix, suffix, base = 0, 0, 29
        last_ix = 0 
        power = 1 

        for i, ch in enumerate(s):
            char = (ord(ch) - ord('a') + 1)
            prefix = prefix * base
            prefix = (prefix + char)

            suffix = suffix + char * power 
            power = power * base 
            if prefix == suffix: 
                last_ix = i 

        suffix = s[last_ix + 1:]
        return suffix[::-1] + s

         