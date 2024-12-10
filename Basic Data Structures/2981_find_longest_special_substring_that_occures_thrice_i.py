class Solution:
    def maximumLength(self, s: str) -> int:
        """
        O(n^2)
        O(n)
        two loops and a dict where you build letters and times ther repeat
        """
        if len(s) == len(set(s)): return -1 
        for i in range(len(s) - 3, -1, -1):
            d = {}
            count = 0
            for j in range(i, len(s)):
                if len(set(s[count:j + 1])) == 1:
                    if s[count:j+1] not in d:
                        d[s[count:j + 1]] = 1
                    else:
                        d[s[count:j + 1]] += 1
                        if d[s[count:j + 1]] == 3:
                            return len(s[count:j + 1])
                count += 1 
        return -1