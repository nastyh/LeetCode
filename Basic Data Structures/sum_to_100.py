class Solution:
    """
    Add the mathematical operators + or - before any of the digits in the decimal
    numeric string 123456789 such that the resulting mathematical expression adds up to 100. Return all possible solutions.
    There are 12 solutions:
    1+2+3-4+5+6+78+9
    1+2+34-5+67-8+9
    1+23-4+5+6+78-9
    1+23-4+56+7+8+9
    12+3+4+5-6-7+89
    12+3-4+5+67+8+9
    12-3-4+5-6+7+89
    123+4-5+67-89
    123+45-67+8-9
    123-4-5-6-7+8-9
    123-45-67+89
    -1+2-3+4+5+6+78+9
    """
    def __init__(self):
        self.ans =[]
    def dfs(self,s,ans,path=""):
        if len(s)==0 and ans==100:
            self.ans.append(path)
        for i in range(len(s)):
            self.dfs(s[i+1:], ans + int(s[:i+1]),path + "+" + s[:i+1])
            self.dfs(s[i+1:], ans - int(s[:i+1]),path + "-" + s[:i+1])
    dfs(s, ans)
    return ans

    def sumTo_pythonic(s: str, target: int) -> List[str]:
        if len(s) == 0:
            return [""] if target == 0 else []

        result = []
        for i in range(len(s) - 1, -1, -1):
            num = int(s[i:])
            r = sumTo(s[0:i], target - num)
            result.extend(map(lambda x: f"{x}+{num}" if x != "" else s[i:], r))

            r = sumTo(s[0:i], target + num)
            result.extend(map(lambda x: f"{x}-{num}", r))
        return result

    def combinations_backtrack(index, sofar, total):
        if index == len(s):
            if total == 100:
            res.append(sofar)
            return

        for i in range(index+1, len(s)+1):
            combinations(i, sofar+'+'+s[index:i] if sofar else s[index:i], total+int(s[index:i]))
            combinations(i, sofar+'-'+s[index:i], total-int(s[index:i]))

        combinations(0, '', 0)

        for idx, r in enumerate(res):
        print(idx+1, r)
