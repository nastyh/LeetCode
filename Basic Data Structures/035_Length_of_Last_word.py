class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        res = s.split(' ')

        if res[-1] == '':
            return 1
        else:
            return len(res[-1])
