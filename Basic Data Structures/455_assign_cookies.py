class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        O(nlogn + mlogm) due to sorting of both
        O(m+n)
        sort both 
        process one by one
        If you can give enough to a kid, do it, increment everything
        Otherwise, move to a bigger cookie 
        """
        g.sort()
        s.sort()
        i, j, res = 0, 0, 0
        while i <len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else: j+= 1
        return res