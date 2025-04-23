from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        O(nlogn) to calc the sum of all digits 
        same for space 
        """
        d = defaultdict(int)
        for i in range(1, n + 1):
            k = sum([int(x) for x in str(i)])
            d[k] += 1
        max_val = max(d.values())
        res = sum(1 for v in d.values() if v == max_val)
        return res