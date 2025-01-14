from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        """
        O(n) both 
        if a char appears and odd num of times, we can keep only one instance of it 
        if even, we keep two instances: one for the left side, another for the right side
        """
        d = Counter(s)
        delete_counts = 0
        for frequency in d.values():
            if frequency % 2 == 1:
                delete_counts += frequency - 1
            else:
                delete_counts += frequency - 2
        return len(s) - delete_counts