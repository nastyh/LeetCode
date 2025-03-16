import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        O(m) where m mechanics per iteration
        and O(log(cars)) for bin search
        O(m * log(cars))
        O(1) nothing to store 
        determine if in a given time t the mechanics can repair at least cars cars.
        For a mechanic with rank r, the maximum number of cars they can repair in time t is given by:
        n = sqrt(t/r)
        for each candidate time compute the sum 
        sqrt(t/r) for each r in ranks
        and check if totalcars >= cars
        The binary search ranges from a low of 0 up to a high of
        min(ranks) * cars^2 b/c the fastest mechanic (with the min rank) would
        take at most that many mins to repair all the cars alone 
        """
        def _can_repair(time):
            total = 0
            for r in ranks:
                total += int(math.sqrt(time / r)) # how many cars they can fix 
                if total >= cars:
                    return True
            return total >= cars
        
        l, h = 0, min(ranks) * cars * cars
        res = h
        while l <= h: 
            m = l + (h - l) // 2
            if _can_repair(m):
                res = m
                h = m - 1 
            else:
                l = m + 1 
        return res