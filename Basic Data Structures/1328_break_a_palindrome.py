class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        O(n) both
        iterate over a half
        if not an 'a', update, return
        if all are 'a' in the first half,
        just update the very last to be
        return 
        """
        n = len(palindrome)
        # edge case
        if n == 1:
            return ""
        
        l = list(palindrome) # easier to work with
        for i in range(n//2):
            if l[i] != 'a':
                l[i] = 'a'
                return "".join(l)
        l[-1] = 'b'
        return "".join(l)