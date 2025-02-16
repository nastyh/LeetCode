from typing import Counter, List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        O(n) both
        counter for each word 
        compare counters: prev and curr. 
        If same, save curr index
        End up with indices that you don't want to have 
        iterate over words, take only indices you want 
        """
        res = []
        ix_to_delete = set()
        if len(words) <= 2: return words
        dicts = []
        for w in words:
            dicts.append(Counter(w))
        for ix in range(1, len(words)):
            if dicts[ix-1] == dicts[ix]:
                ix_to_delete.add(ix)
        for i in range(len(words)):
            if i not in ix_to_delete:
                res.append(words[i])
        return res
