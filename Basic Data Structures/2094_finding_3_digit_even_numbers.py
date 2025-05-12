from typing import Counter, List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        O(n)
        O(1) -- at most 900 elements
        a -- hundreds, cannot be 0
        c -- ones, must be even 
        count frequencies of the digits
        loop over each possible triple 
        collect the answers in a set and return 
        """
        freq, res = Counter(digits), set()
        for a in range(1, 10):
            if freq[a] == 0:
                continue
            for b in range(10):
                if freq[b] == 0:
                    continue
                for c in (0, 2, 4, 6, 8):
                    if freq[c] == 0:
                        continue 

                    need = Counter((a, b, c))
                    if all(need[d] <= freq[d] for d in need):
                        res.add(100*a + 10*b + c)
        return sorted(res)