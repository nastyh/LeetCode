from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        O(mn * log(mn)), mn to flatten the grid. Log(mn) for sorting, go through
        the sorted list, apply all the checks to each of the mn elements 
        O(mn) to create flat

        Create a list of numbers from the grid
        All numbers must be congruent modulo x. 
        means (a-b) should be divisible by x 
        The optimal target value to minimize the num of operations is the median of the list 
        Because the sum of abs deviations is minimized at the median
        operations = abs(num - median) / x
        """
        flat = [num for row in grid for num in row]
        remainder = flat[0] % x 
        for num in flat:
            if num % x != remainder: # if remainders are different, not possible 
                return -1 
        flat.sort()
        median = flat[len(flat) // 2]
        res = sum(abs(num - median) // x for num in flat)
        return res