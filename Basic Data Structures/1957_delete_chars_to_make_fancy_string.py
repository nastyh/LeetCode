class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        O(n) both
        start building the answer
        If we haven't processed 2 characters and the last != second last != current,
        it's a good one
        it means we don't have something like "aaa"
        """
        res = []
        for ch in s:
            if len(res) < 2 or not (res[-1] == res[-2] == ch):
                res.append(ch)
        return ''.join(c for c in res)