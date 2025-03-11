class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        O(n) to process s
        O(1) since it's just a dictionary of the three letters 
        two pointers, dict at zero
        start moving the right pointer (j)
        and update the dict
        start the while portion that will move the left pointer (i)
        while the current window contains at least one of each chars 
        add len(s) - j because every extension from right to the end of the string will maintain the validity of the substring.
        then update the dict by removing the instance from the left pointer
        move the left pointer
        """
        d, i, res = {'a': 0, 'b': 0, 'c':0}, 0, 0
        for j, ch in enumerate(s):
            d[ch] += 1
            while d['a'] > 0 and d['b'] > 0 and d['c'] > 0: # current window contains at least one of each chars 
                res += (len(s) - j)
                d[s[i]] -= 1
                i += 1
        return res 
        