class Solution:
    def robotWithString(self, s: str) -> str:
        """
        O(n) one pass to build min_suf and another to process s
        O(n) for min_suf, t, res 
        Move the first character of s to the end of string t.
        Pop the last character of t and write it to the result string p.
        Interleave these operations to get the smallest p possible.

        Either move the next character from s to t, or
        Pop from t to res, if the top of t is ≤ the smallest remaining character in s.
        """
        n = len(s)
        min_suf = [''] * n # the smallest character in the remaining part of s.
        min_suf[-1] = s[-1]
        
        # Build min suffix array: min_suf[i] is the min character from s[i:]
        for i in range(n - 2, -1, -1):
            min_suf[i] = min(s[i], min_suf[i + 1])
        
        t = []  # robot's string buffer
        res = []  # written result
        for i, c in enumerate(s):
            t.append(c)
            # Pop from t while top is <= the smallest char left in s
            while t and (i == n - 1 or t[-1] <= min_suf[i + 1]):
                res.append(t.pop())
        
        return ''.join(res)