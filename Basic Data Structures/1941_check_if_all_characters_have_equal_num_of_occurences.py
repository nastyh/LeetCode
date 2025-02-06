from typing import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        O(n)
        O(1) since it's 26 in both dict and set
        Count frequencies in d 
        start iterating and adding to the set
        if the set is empty (it's the beginning), just add
        later on,
        if the incoming number is the same, continue
        otherwise, False
        True at the end 
        """
        d = Counter(s)
        print(d)
        s = set()
        for v in d.values():
            if len(s) == 0:
                s.add(v)
            else:
                if v in s:
                    continue
                else:
                    return False
        return True