class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d, t_d = {}, {}
        for i in s:
            if i in s_d:
                s_d[i] += 1
            else:
                s_d[i] = 1
        for j in t:
            if j in t_d:
                t_d[j] += 1
            else:
                t_d[j] = 1
        return s_d == t_d
