"""
Add the mathematical operators + or - before any of the digits in the decimal numeric string 123456789 such that the
resulting mathematical expression adds up to 100. Return all possible solutions.
"""

class Solution:
    def __init__(self):
        self.ans =[]
    def dfs(self, s, ans, path=""):
        if len(s) == 0 and ans == 100:
            self.ans.append(path)
        for i in range(len(s)):
            self.dfs(s[i + 1:],ans + int(s[:i + 1]),path + "+"+s[:i + 1])
            self.dfs(s[i + 1:],ans - int(s[:i + 1]), path + "-" + s[:i + 1])

a = Solution()
a.dfs("123456789",0)
for i in a.ans:
    print(i)


# Backtracking solution
def combinations(index, sofar, total):
  if index == len(s):
    if total == 100:
      res.append(sofar)
    return

  for i in range(index+1, len(s) + 1):
    combinations(i, sofar+'+' + s[index:i] if sofar else s[index:i], total + int(s[index:i]))
    combinations(i, sofar + '-' + s[index:i], total - int(s[index:i]))

combinations(0, '', 0)

for idx, r in enumerate(res):
  print(idx + 1, r)

