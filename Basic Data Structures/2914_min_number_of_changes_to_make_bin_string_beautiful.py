class Solution:
    def minChanges(self, s: str) -> int:
        """
        O(n) and O(1)
        process in pairs
        s = "1001"
        look at 1 and 0. One change is needed: 1 to 0 or vice versa
        look at 0 and 1. One change is needed: 1 to 0 or vice versa
        Overall, two changes 
        """
        res = 0
        for ix in range(1, len(s), 2):
            if s[ix-1] != s[ix]:
                res += 1
        return res