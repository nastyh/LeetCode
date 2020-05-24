class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = [], []
        for i in num1:
            n1.append(int(i))
        for j in num2:
            n2.append(int(j))
        return str(sum([v*10**k for k,v in enumerate(n1[::-1])]) * sum([v*10**k for k,v in enumerate(n2[::-1])]))
