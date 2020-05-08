class Solution:
    def reverseWords(self, s: str) -> str:
        working = s.split(' ')
        return ' '.join([i[::-1] for i in working])
