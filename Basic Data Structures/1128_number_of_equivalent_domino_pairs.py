from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs_another(self, dominoes: List[List[int]]) -> int:
        """
        O(n)
        O(1)

        [1;2] and [2;1] are siblings. We need to count them under the same key.
        Go over the dominoes
        See one, calculate 12 and its opposite, 21.
        Key will be the min of the two (might be the max, it's arbitrary)
        Update res
        Add to the dict how many times we've seen this or (opposite) element
        Return res 
        """
        d, res = defaultdict(int), 0
        for dom in dominoes:
            candidate = 10*dom[0] + dom[1]
            opposite = 10*dom[1] + dom[0]
            key = min(candidate, opposite)
            res += d[key]
            d[key] += 1
        return res
    
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        O(n)
        O(1)

        """
        d, res = defaultdict(int), 0
        for dom in dominoes:
            key = (dom[0], dom[1]) if dom[0] <= dom[1] else (dom[1], dom[0])
            res += d[key]
            d[key] += 1
        return res
    
    