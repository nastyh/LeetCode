from typing import List


class Solution:
    def findMissingAndRepeatedValues_math(self, grid: List[List[int]]) -> List[int]:
        """
        O(n^2) to go over grid
        O(1) since seen will have only one item
        We need to calculate
        1. the proper sum of the numbers from 1 to n^2
        2. the sum of all elements in the grid. Do it in the loop
        3. the sum of the unique elements in the grid. Track these using the set seen
        then sum up what is inside seen
        the repeating value is the diff between the grid sum and the unique (set) sum.
        Makes sense since we didn't put the repeating value in the set so it doesn't contribute
        to the set sum
        The missing value is the difference between the ideal sum (all_nums_sum) and the sum of the unique 
        values obtained from grid --> it's the set sum
        Makes sense since the the set sum has a value that is missing from the ideal sum
        """
        grid_sum = 0 
        seen = set()
        all_nums_sum = sum([i for i in range(1, len(grid)**2 + 1)])
        res = [None] * 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid_sum += grid[r][c]
                seen.add(grid[r][c])
        seen_sum = sum([i for i in seen])
        res[0] = abs(grid_sum - seen_sum)
        res[1] = abs(all_nums_sum - seen_sum)
        return res
    
    def findMissingAndRepeatedValues_xor(self, grid: List[List[int]]) -> List[int]:
        """
        O(n^2)
        O(1)
        XOR all numbers in the grid and also XOR with every number from 1 to n². 
        This gives you the XOR of the duplicate (let’s call it x) and the missing number (y):
        xor_all = x XOR y.

        Find a set bit (usually the rightmost set bit) in xor_all.
        This bit will be different between x and y, so you can partition all numbers
        into two groups based on whether they have that bit set. XORing within each group
        (both for the grid and for the numbers 1 to n²) will yield two candidates.
        Since one candidate is the repeated number and the other is missing,
        use a count over the grid (or the sum approach) to decide which is which.
        """
        n = len(grid)
        total = n * n
        
        # Step 1: Compute XOR of all grid elements and numbers 1 through total.
        xor_all = 0
        for row in grid:
            for num in row:
                xor_all ^= num
        for num in range(1, total + 1):
            xor_all ^= num
        
        # xor_all now equals duplicate XOR missing.
        # Step 2: Find the rightmost set bit in xor_all.
        set_bit = xor_all & -xor_all
        
        # Partition numbers into two groups and XOR separately.
        x = 0  # one candidate
        y = 0  # the other candidate
        for row in grid:
            for num in row:
                if num & set_bit:
                    x ^= num
                else:
                    y ^= num
        for num in range(1, total + 1):
            if num & set_bit:
                x ^= num
            else:
                y ^= num
        
        # Now, x and y are the two candidates, one is the duplicate and the other is missing.
        # Step 3: Determine which candidate is the duplicate using a count over the grid.
        count_x = sum(num == x for row in grid for num in row)
        if count_x == 2:
            duplicate, missing = x, y
        else:
            duplicate, missing = y, x
        
        return [duplicate, missing]

    def findMissingAndRepeatedValues_dict(self, grid: List[List[int]]) -> List[int]:
        """
        O(n^2) due to going over grid
        O(n^2) due to the dict that can grow to the size of grid
        d is the dict that has 1: 0, 2: 0, all the way to n^2: 0
        go over grid
        if the value is zero, it's a brand new number, update the count
        if the value is > 0, it means, we saw this number, put it into res 
        at the end, the key in the dict that still has a 0 value, is the missing number
        put it into res, too
        return 
        """
        res = [None] * 2
        d = {i: 0 for i in range(1, len(grid)**2+1)}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if d[grid[r][c]] == 0:
                    d[grid[r][c]] = 1
                elif d[grid[r][c]] > 0:
                    d[grid[r][c]] += 1
                    res[0] = grid[r][c]
        missing_val = [k for k, v in d.items() if v == 0][0]
        res[1] = missing_val
        return res

    def findMissingAndRepeatedValues_brute_force(self, grid: List[List[int]]) -> List[int]:
        """
        O(n^2), size of the grid
        O(n^2) due to all_nums that can contain all the nums from grid in the worst case

        Do what it asked
        s is needed to catch the repeating number. If we're about to add something
        that is already is s, this is the repeating number. Put it into res
        seen is needed so that we don't traverse the grid one more time to find the missing value
        all_nums contains numbers from 1 to n^2 and needed to find the missing value
        go over all_nums: if a number from there isn't in seen, it's the missing value
        add it to res
        return res 
        """
        res = [None] * 2
        s = set()
        all_nums = set([i for i in range(1, len(grid)**2+1)])
        seen = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] not in s:
                    s.add(grid[r][c])
                else:
                    res[0] = grid[r][c]
                seen.add(grid[r][c])
                
        for n in all_nums:
            if n not in seen:
                res[1] = n
        return res
        