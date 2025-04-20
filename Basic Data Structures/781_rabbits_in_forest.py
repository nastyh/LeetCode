import math
from typing import Counter, List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        O(n) both to go over and counter
        if a rabbit answers k, there are k+1 rabbits of this color (including the one who responded)
        answers with the same value should be partitioned into groups of size k + 1
        any partially filled group still implies k+1 rabbits 
        """
        d, res = Counter(answers), 0 # color_index: how many times it's used. Say for [10, 10, 10], it's {10:3}
        for k, cnt in d.items():
            group_size = k + 1 # say it's 10 + 1 = 11
            groups = math.ceil(cnt / group_size) # 3/11 and round up gives us 1
            res += groups * group_size # 1 * 11 = 11 
        return res