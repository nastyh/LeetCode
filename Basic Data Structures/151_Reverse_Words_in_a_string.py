 class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        r = [i for i in s.split()]
        return ' '.join(j for j in r[::-1])
