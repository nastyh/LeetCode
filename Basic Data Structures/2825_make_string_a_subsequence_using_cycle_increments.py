class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        O(n+m), strings' lengths 
        O(1)
        two pointers, loop through the strings 
        for each pair of letters check whether
        1. they are the same
        2. you can update a letter by making it the next letter
        3. Z-->A is taken care of, too, by minus 25
        If we can process everything in the second string, we're good 
        """
        str2_ix = 0
        str1_length, str2_length = len(str1), len(str2)
        for str1_ix in range(str1_length): # going over the first string
            if str2_ix < str2_length and (
                str1[str1_ix] == str2[str2_ix] # letters match 
                or 
                ord(str1[str1_ix]) + 1 == ord(str2[str2_ix]) # can update the char to the next one
                or 
                ord(str1[str1_ix]) - 25 == ord(str2[str2_ix]) # it's how we go from A to Z, since it's cyclical
            ):
                str2_ix += 1
        return str2_ix == str2_length # that we can process the whole second string