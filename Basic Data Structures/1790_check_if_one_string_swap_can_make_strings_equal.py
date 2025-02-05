class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        O(s1+s2) need to process both strings
        O(1) max is just two elements inside mismatched_ix
        Go over both 
        If there is a mismatch, get the index where it happens
        If there are more than two, it means that we need to swap more
        than one letter, return False
        if there is one element, it's also bad, it's something like 'ab' 'aa'
        Two elements mean one swap
        Check if by making this swap, the result is two same strings 
        """
        if s1 == s2: return True # nothing needs to be done
        mismatched_ix = []
        for ix in range(len(s1)):
            if s1[ix] != s2[ix]:
                mismatched_ix.append(ix)
        if len(mismatched_ix) > 2 or len(mismatched_ix) == 1:
            return False 
        i, j = mismatched_ix[0], mismatched_ix[1]
        return s1[i] == s2[j] and s1[j] == s2[i]
