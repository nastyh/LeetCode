from typing import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        """
        O(n) to iterate 
        O(1) for the dict, since it will have at most 10 elements
        """
        d = Counter(int(n) for n in num)
        for ix in range(len(num)):
            if d[ix] != int(num[ix]):
                return False
        return True
    
    def digitCount_one_liner(self, num: str) -> bool:
        return all(Counter(map(int, num)).get(i, 0) == int(x) for i, x in enumerate(num))