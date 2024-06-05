class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        ss is a set with the letters that have odd counts
        set contains non-paired letters
        then we take the whole length (it includes odd and even),
        remove the odd counts except one of them (thus, plus 1)
        since we can play one odd letter in the middle 
        """
        ss = set()
        for ch in s:
            if ch not in ss:
                ss.add(ch)
            else:
                ss.remove(ch)
        if len(ss) != 0: # if we have any letters with the odd counts
            # we take the length of the string (it includes evens), get rid of all 
            # but one even and it's the answer
            return len(s) - len(ss) + 1
        else:
            return len(s)