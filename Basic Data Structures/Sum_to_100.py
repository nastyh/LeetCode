"""
Add the mathematical operators + or - before any of the digits in the decimal numeric string 123456789 such that the resulting mathematical expression adds up to 100. Return all possible solutions.
"""

class Solution:
    def __init__(self):
        self.ans =[]
    def dfs(self,s,ans,path=""):
        if len(s)==0 and ans==100:
            self.ans.append(path)
        for i in range(len(s)):
            self.dfs(s[i+1:],ans+int(s[:i+1]),path+"+"+s[:i+1])
            self.dfs(s[i+1:],ans-int(s[:i+1]),path+"-"+s[:i+1])

a = Solution()
a.dfs("123456789",0)
for i in a.ans:
    print(i)

