class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s, res = set(), len(words)
        for ch in allowed:
            s.add(ch)
        for word in words:
            for ch in word:
                if ch not in s:
                    res -= 1
                    break
        return res